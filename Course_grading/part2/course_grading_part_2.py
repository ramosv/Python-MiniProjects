# wwite your solution here
## Working with two csv files.
## Info about students id;first;last
## number of exercises completed id;exercises;more


student_info = input("Student file: ")
excercise_data = input("Excercises Completed: ")
exam_points = input("Exam Points: ")

# if False:
#     student_info = input("Student file: ")
#     excercise_data = inout("Excercises Completed: ")
# else:
#     student_info = "students1.csv"
#     excercise_data = "exercises1.csv"
#     exam_points = "exam_points1.csv"



names = {}
with open(student_info) as new_file:
    for line in new_file:
        part = line.strip().split(";")
        # Ignore first column
        if part[0] == "id":
            continue
        names[part[0]] = part[1] +" " + part[2]

work = {}
with open(excercise_data) as new_file:
    for line in new_file:
        part = line.strip().split(";")
        # Ignore first column
        if part[0] == "id":
            continue
        work[part[0]] = part[1:]
def calculate_points(percent):
    total = 0
    if percent <=19 and percent > 10:
        total = 1
    elif percent < 30:
        total = 2
    elif percent < 40:
        total = 3
    elif percent < 50:
        total = 4
    elif percent < 60:
        total = 5
    elif percent <70:
        total = 6
    elif percent <80:
        total = 7
    elif percent <90:
        total = 8
    elif percent <100:
        total = 9
    elif percent == 100:
        total = 10
    else:
        total = 0
    return total

points = {}
for id, name in names.items():
    if id in work:
        asNums = [int(num) for num in work[id]]
        summa = sum(asNums)
        percentage = (summa /40)*100
        pointsr = calculate_points(percentage)
        points[id] = pointsr
        
        #print(f"{name} {summa} {pointsr}")

exam = {}
with open(exam_points) as new_file:
    for line in new_file:
        line = line.strip().split(";")
        if line[0] == "id":
            continue
        exam[line[0]] = line[1:]
#print(exam)

def final_grade(test,exer):
    #print(f"{test} and {exer}")
    total = test+exer
    #print(total)
    if total <15:
        total = 0
    elif total < 18:
        total = 1
    elif total < 21:
        total =2
    elif total < 24:
        total =3
    elif total < 28:
        total = 4
    elif total >=28:
        total =5
    return total


for id, name in names.items():
    if id in exam:
        asNums = [int(num) for num in exam[id]]
        summa = final_grade(sum(asNums),points[id])
        print(f"{name} {summa}")




# if False:
#     student_info = input("Student file: ")
#     excercise_data = inout("Excercises Completed: ")
# else:
#     student_info = "student1.csv"
#     exercise_data = "exercises1.csv"
