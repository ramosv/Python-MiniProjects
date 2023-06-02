# Please write a function named dict_of_numbers(), 
# which returns a new dictionary. The dictionary should 
# have the numbers from 0 to 99 as its keys. The value 
# attached to each key should be the number spelled out in words. 
# Please have a look at the example below:

# numbers = dict_of_numbers()
# print(numbers[2])
# print(numbers[11])
# print(numbers[45])
# print(numbers[99])
# print(numbers[0])
from num2words import num2words

def dict_of_numbers():
    dicto = {}

    for i in range(0,99):
        dicto[i] = num2words(i)

    return dicto

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[45])


#########################################
### Solution without using library ###

def dict_of_numbers():
    numbers = {}

    singles = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}

    whole_tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

    #0 - 9
    for i in range(10):
        numbers[i] = singles[i]
    
    # 10 - 19 are special cases
    numbers[10] = "ten"
    numbers[11] = "eleven"
    numbers[12] = "twelve"
    numbers[13] = "thirteen"
    numbers[14] = "fourteen"
    numbers[15] = "fifteen"
    numbers[16] = "sixteen"
    numbers[17] = "seventeen"
    numbers[18] = "eighteen"
    numbers[19] = "nineteen"

    # 20 - 99
    for i in range(2,10):
        numbers[i * 10] = whole_tens[i]
        for j in range(1,10):
            numbers[i * 10 +j] = whole_tens[i] + "-" + singles[j]
    
    return numbers 

if __name__ == "__main__":

    print(dict_of_numbers())



    
