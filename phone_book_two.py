def search(book):
    name = input("name:")
    if name in book.keys():
        numbers = book[name]
        for i in numbers:
            print(i)
    else:
        return print("no number")

def add(book):
    name = input("name:")
    num = input("number:")
    if name in book.keys():
        numbers = book[name]
    else:
        numbers = []
    numbers.append(num)
    book[name] = numbers
    print("ok!")

def main():
    book = {}
    while True:
        num = input("command (1 search, 2 add, 3 quit):"
        )
        if num == "1":
            search(book)
        elif num == "2":
            add(book)
        elif num == "3":
            print("quitting...")
            break

main()