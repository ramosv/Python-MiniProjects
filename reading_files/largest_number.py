
def largest():
    with open("numbers.txt") as new_file:
        num = 0
        for line in new_file:
            if int(line) > num:
                num = int(line)

    print(num)

largest()