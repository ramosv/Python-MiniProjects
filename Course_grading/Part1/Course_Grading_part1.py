## Working with two csv files.
## Info about students id;first;last
## number of exercises completed id;exercises;more


student_info = input("Student file: ")
excercise_data = input("Excercises Completed: ")

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

for id, name in names.items():
    if id in work:
        asNums = [int(num) for num in work[id]]
        summa = sum(asNums)
        print(f"{name} {summa}")

if False:
    student_info = input("Student file: ")
    excercise_data = inout("Excercises Completed: ")
else:
    student_info = "student1.csv"
    exercise_data = "exercises1.csv"
