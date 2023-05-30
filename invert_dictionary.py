
def invert(dicto):
    for k, v in dicto.copy().items():
        del dicto[k]
        dicto[v] = k
def main():
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)

main()

