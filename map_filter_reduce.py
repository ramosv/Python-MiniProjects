## Map filter and reduce funtions are high order functions that operate on a list

## Example of Map

def times_two(x):
    return x*2

nums = [18,36,50,100,150]
answer = list(map(times_two,nums))
print(answer)