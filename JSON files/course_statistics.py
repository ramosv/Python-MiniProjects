import urllib.request
import json
import math

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")

    data = json.loads(my_request.read())

    enabled = []
    names = []

    for course in data:
        if course['enabled'] == True:
            enabled.append((course['fullName'], course['name'], course['year'], sum(course['exercises'])))
            names.append(course['name'])

    return enabled

def retrieve_course(course):
    url = f'https://studies.cs.helsinki.fi/stats-mock/api/courses/{course}/stats'

    my_request = urllib.request.urlopen(url)
    data = json.loads(my_request.read())

    information = {}

    maximum = 0
    hours= 0
    students =0
    exercises=0
    
    for x in data:
        if maximum < data[str(x)]['students']:
                maximum = data[str(x)]['students']

        hours += data[str(x)]['hour_total']
        students += data[str(x)]['students']
        exercises += data[str(x)]['exercise_total']
    


    information['weeks'] = len(data)
    information['students'] = maximum
    information['hours']  = hours
    information['hours_average'] = math.floor(hours/maximum)
    information['exercises'] = exercises
    information['exercises_average'] = math.floor(exercises/maximum)

    return information

    
if __name__ == "__main__":
    retrieve_all()
    print(retrieve_course("docker2019"))
    print(retrieve_course("CCFUN"))