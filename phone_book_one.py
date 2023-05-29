phonebook = {}

while True:
    command = input("command(1 search, 2 add, 3 quit):")
    if command == "3":
        print("quitting...")
        break
    
    elif command == "1":
        name = input("name:")
        if name in phonebook:
            print(phonebook[name])
        else:
            print("no number")
    elif command == "2":
        nam = input("name:")
        numer = input("number")
        phonebook[nam] = numer
        print("ok!")