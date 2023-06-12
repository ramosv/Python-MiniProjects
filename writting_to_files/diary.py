

def diary(num,text=""):
    if num ==1:
        with open("diary.txt", "a") as file:
            file.write(entry + "\n")
        print("Diary saved\n")
    if num == 2:
        with open("diary.txt") as file:
            for line in file:
                print(line.strip())
        


while(True):
    print("1 - add an entry, 2 - read entries, 0 - quit")
    choice = int(input("Function: "))
    if choice == 1:
        entry = input("Diary entry: ")
        diary(1, entry)
    elif choice == 2:
        print("Entries:")
        diary(2)
    elif choice == 0:
        print("Bye now!")
        break
    else: break
