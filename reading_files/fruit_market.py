def read_fruits():
    dicto = {}
    with open("fruits.csv") as new_line:
        for line in new_line:
            line = line.replace("\n","")
            fruit = line.split(";")
            dicto[fruit[0]] = float(fruit[1])
    
    return dicto

if __name__ == "__main__":
    print(read_fruits())
    