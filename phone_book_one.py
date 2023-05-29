phonebook = {}

while True:
    command = input("1 search, 2 add, 3 quit")
    if command == 3:
        print("quitting...")
    
    elif command == 1:
        name = input()
        if name in phonebook:
            print(phonebook[name])
        else:
            print("no number")
    elif command == 2:
        nam = input()
        numer = input()
        phonebook[nam] = numer
