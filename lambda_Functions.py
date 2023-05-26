## Lambda functions 


## These two functions are the same 

#Named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

##Lambda
print((lambda x: x**2 + 5*x +4) (-4))

## Lambda function to calculate percentage of price
price = int(input())
percentage = int(input())

answer = (lambda x,y: (x*y)/100)(price,percentage)

print(answer)

## Lambda function using Map and filter

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than 
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

map_result = list(map(lambda x: round(x**2,3),my_floats))
filter_results = list(filter(lambda name: len(name)<=7, my_names))


