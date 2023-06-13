# Write your solution here
def filter_solutions():
    #Deleting contents from a file
    #Open
    correct = []
    incorrect = []

    with open('solutions.csv') as file: 
        for row in file:
            parts = row.strip().split(";")
            
            if ("-" in parts[1]):
                numOne = parts[1].strip().split("-")
            else:
                numOne = parts[1].strip().split("+")

            if (int(numOne[0]) + int(numOne[1])) == int(parts[2]):
                correct.append(f"{parts[0]};{parts[1]};{parts[2]}")
            elif (int(numOne[0]) - int(numOne[1])) == int(parts[2]):
                correct.append(f"{parts[0]};{parts[1]};{parts[2]}")
            else:
                incorrect.append(f"{parts[0]};{parts[1]};{parts[2]}")

    with open('correct.csv','w') as file:
        pass
        for part in correct:
            file.write(f"{part}\n")
    
    with open('incorrect.csv','w') as file:
        pass
        for part in incorrect:
            file.write(f"{part}\n")

if __name__ == "__main__":
    filter_solutions()
