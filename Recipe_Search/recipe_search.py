def reading_file(filename):
    ## this should return a dcitonary
    foods = []
    with open(filename) as file:
        for row in file:
            foods.append(row.strip())
    foods.append(0)
    #print(foods)
    dicto = {}
    key = 0
    val = 1
    last = foods[-1]
    for x in foods:
        #print(f"food = {x}")
        if x == '' or x == last:
            if x == last:
                dicto[foods[key]] = foods[val:foods.index(0)]
                break
            dicto[foods[key]] = foods[val:foods.index('')]
            #Reassigning indexes
            key = foods.index('') 
            val = foods.index('') +1
            foods.remove('')
    return dicto

def search_by_name(filename, word):
    dicto = reading_file(filename)

    #print(dicto)
    answer = []
    for x in dicto:
        if word.lower() in x.lower():
            answer.append(x)
    return answer

def search_by_time(filename, num):
    dicto = reading_file(filename)

    answer = []
    for x in dicto:
        if int(dicto[x][0]) <= num:
            answer.append(f"{x}, preparation time {int(dicto[x][0])} min")
    return answer
def search_by_ingredient(filename,word):
    dicto = reading_file(filename)      

    answer = []
    for x in dicto:
        if word in dicto[x]:
            answer.append(f"{x}, preparation time {dicto[x][0]} min")
    return answer


if __name__ == "__main__":
    print(search_by_ingredient("recipes1.txt","milk"))
    
## Part 1
#text = input()
#search_by_name("recipes1.txt",text)

## part 2
#time = input()
#search_by_time("recipes1.txt", 60)
#search_by_ingredient("recipes1.txt","eggs")