# Calculate factorials and save them to a dictionary

def factorinals(x):
    dicto = {}
    result = 1
    count = 1

    while count <= x:
        result *= count
        dicto[count] = result
        count +=1

    return dicto

if __name__ == "__main__":
    print(factorinals(6))