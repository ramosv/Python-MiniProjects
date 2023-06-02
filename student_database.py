## build a student database to using dictionaries tuples and lists
def add_student(students, name):
    students[name] = ("no completed courses",0)


def print_student(students, name):
    if name in students:
        if students[name][0]== "no completed courses":      
            print(f"{name}:\n {students[name][0]}")
        else:
            summa = 0
            length = 0
            
            for x in students[name]:
                summa += x[1]
                length += 1

            print(f"{name}:\n {length} completed courses:")
            for x in students[name]:
                print(f"  {x[0]} {x[1]}")
            print(f" average grade {summa / length}")
    else:
        print(f"{name}: no such person in the database")

def add_course(students, name, course): 
    courses = []

    if type(students[name]) is list:
        flag = False
        for x in students[name]:
            courses.append(x)
            if x[0] == course[0] and x[1] > course[1]:
                flag = True
            if x[0] == course[0] and x[1] < course[1]:
                flag = False
                courses.remove(x)
   
        if course[1]!=0 and flag == False:
            courses.append(course)
            students[name] = courses
    else:
        if course[1] !=0:
            students[name] = [course]

    ## check for repeated
    



def summary(students):
    size = len(students)
    finalgrade = 0
    name2=""

    completed = 0
    name1 = ""

    final = {}

    for x in students:
        temp = []
        for j in students[x]:  
            temp.append(j[1])
        final[x] = temp
            
    for x in final:
        best_grade = 0
        if completed < len(final[x]):
            completed = len(final[x])
            name1 = x 
        for j in final[x]:
            best_grade += j
        if best_grade/len(final[x]) > finalgrade:
            finalgrade = best_grade/len(final[x])
            name2 = x
        
    
    print(f"students {size}\nmost courses completed {completed} {name1}\nbest average grade {finalgrade} {name2}")


if __name__ == "__main__":
    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # print_student(students, "Peter")
    # print_student(students, "Eliza")
    # print_student(students, "Jack")
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    # add_course(students, "Peter", ("Introduction to Programming", 2))
    # print_student(students, "Peter")
    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    # add_course(students, "Peter", ("Introduction to Programming", 1))
    # add_course(students, "Peter", ("Advanced Course in Programming", 1))
    # add_course(students, "Eliza", ("Introduction to Programming", 5))
    # add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    # summary(students)
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    print_student(students, "Peter")