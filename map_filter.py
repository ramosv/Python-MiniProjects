## Map and filter funtions are high order functions that operate on a list

## Example of Map

def times_two(x):
    return x*2

nums = [18,36,50,100,150]
answer = list(map(times_two,nums))
print(answer)

## Using lambda function

answer = list(map(lambda x: x*2, nums))
print(answer)

## Using map to capitalize all words of a list
names = ['alfred', 'tabitha', 'william', 'arla',"kevin"]

uppered_names = list(map(str.upper, names))
print(uppered_names)

## Using map with round() function which takes two arguments
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

answer = list(map(round,circle_areas,range(1,7)))

##first iteration will be, round(3.56773,1) rounding to the first decimal
##Second iteration will be, round(5.57668,2) rounding to the second decimal and so on...

## Using filter and lambda to print all evens from a list

all = [11,22,33,44,55,66,77]
answer = list(filter(lambda x: x%2==0,all))
print(answer)

## Using filter with a built function

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def over_B(score):
    return score > 80

over_80 = list(filter(over_B,scores))
print(over_80)

## Using filter to check if a word is a palindrome

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes))


