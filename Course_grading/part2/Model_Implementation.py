student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

#Calculating final grade
def grades(points):
    grade = 0
    limits = [15,18,21,24,28]
    while grade < 5 and points >=limits[grade]:
        grade+=1
    return grade

#Excersise values to points
def to_points(number):
    return number //4

students={}
with open(student_data) as file:
    for row in file:
        parts = row.split(';')
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
print(students)

exercises = {}
with open(exercise_data) as file:
    for row in file:
        parts = row.split(';')
        if parts[0] == "id":
            continue
        exercise_sum = 0
        for i in range(1,8):
            exercise_sum += int(parts[1])
        exercises[parts[0]] = exercise_sum

print(exercises)

exams = {}
with open(exam_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        exam_sum = 0
        for i in range(1,4):
            exam_sum += int(parts[i])
        exams[parts[0]] = exam_sum

print(exams)

for student_id, name in students.items():
    total = exams[student_id] + to_points(exercises[student_id])
    print(f"{name} {grades(total)}")
