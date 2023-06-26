import json

def print_persons(filename):
    
    with open(filename) as file:
        data = file.read()
        
    work = json.loads(data)

    for dicto in work:
        hobbies = ', '.join(dicto['hobbies'])
            
        print(f"{dicto['name']} {dicto['age']} years ({hobbies})")


    #print(work)

if __name__ == "__main__":
    print_persons('file1.json')