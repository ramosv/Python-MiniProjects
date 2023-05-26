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

## Lambda function using Map, filter and reduce

