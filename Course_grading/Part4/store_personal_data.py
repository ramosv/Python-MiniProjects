
def store_personal_data(tup):
    name,age,height = tup

    with open('people.csv','a') as file:
        file.write(f"{name};{age};{height}\n")

if __name__ == "__main__":
    tup = ("Paul Paulson", 37, 175.5)
    store_personal_data(tup)