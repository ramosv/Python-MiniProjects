# Write your solution here


def addWord():
    fin = input("The word in Finnish: ")
    eng = input("The word in English: ")
    
    with open('dictionary.txt','a')as file:
        file.write(f"{fin};{eng}\n")

    print("Dictionary entry added")

def search():
    term = input("Search term: ")
    with open('dictionary.txt') as file:
        for row in file:
            parts = row.split(";")

            if term in parts[0] or term in parts[1]:
                print(f"{parts[0]} - {parts[1]}")
            else:
                break

while(True):
    print("1 - Add word, 2 - Search, 3 - Quit")
    func = input("Function: ")
    if func == "1":
        addWord()
    elif func == "2":
        search()
    else:
        print("Bye!")
        break