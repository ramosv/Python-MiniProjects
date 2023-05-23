## With in a range print all numbers that are prime using yield
def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2,x):
        if x % n ==0:
            return False
    return True

def primeGenerator(x,y):
    for n in range(x,y):
        if isPrime(n) is True:
            yield n

start = int(input())
end = int(input())

print(list(primeGenerator(start,end)))

##Example output
#10
#22
#[11, 13, 17, 19]