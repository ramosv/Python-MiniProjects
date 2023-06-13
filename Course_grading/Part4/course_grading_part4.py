## Writing results to txt and csv file

student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")
course_info = input("Course information: ")

# student_data = "students1.csv"
# exercise_data = "exercises1.csv"
# exam_data = "exam_points1.csv"
# course_info = "course1.txt"

def grade(points):
    a = 0
    limits = [15,18,21,24,28]
    while a < 5 and points >= limits[a]:
        a += 1
    
    return a

def to_points(number):
    return number // 4

students = {}
with open(student_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"

exercises = {}
with open(exercise_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        exercise_sum = 0
        for i in range(1,8):
            exercise_sum += int(parts[i])
        exercises[parts[0]] = exercise_sum

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

course = []
with open(course_info) as file:
    for row in file:
        parts = row.split(":")
        course.append(parts[1].strip())
        
        


word1 = "name"
word2 = "exec_nbr"
word3 = "exec_pts."
word4 = "exm_pts."
word5 = "tot_pts."
word6 = "grade"

course = f"{course[0]}, {course[1]} credits"
line = "======================================"
head = f"{word1:<30}{word2:<10}{word3:<10}{word4:<10}{word5:<10}{word6:<10}"

with open('results.txt','w') as file:
    pass
    file.write(f"{course}\n")
    file.write(f"{line}\n")
    file.write(f"{head}\n")
with open('results.csv','w')as file:
    pass

print(f"{course[0]},{course[1]} credits")
print("======================================")
print(f"{word1:<30}{word2:<10}{word3:<10}{word4:<10}{word5:<10}{word6:<10}")
for student_id, name in students.items():
    total = exams[student_id] + to_points(exercises[student_id])
    save = f"{name:<30}{exercises[student_id]:<10}{to_points(exercises[student_id]):<10}{exams[student_id]:<10}{total:<10}{grade(total):<10}"
    print(save)
    with open('results.txt','a') as file:
        file.write(f"{save}\n")
    with open('results.csv','a')as file:
        file.write(f"{student_id};{name};{grade(total)}\n")


