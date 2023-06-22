from random import randint

def words(size, start):
    with open('words.txt') as file:
        inx = 0
        length = len(start)
        words = []
        for row in file:
            ## Could have used row.startswith(start)
            if start == row[0:length]:
                words.append(row.strip())

        if len(words) < size:
            raise ValueError
        
        ## Could have used random.sample(words,size)
        rand_words = []
        for i in range(size):
            rand_indx = randint(0, len(words)-1)
            rand_words.append(words[rand_indx])   
          
        return rand_words

""" Model Solution.

def words(n: int, beginning: str):
    word_list = []
    with open("words.txt") as file:
        for word in file:
            word = word.replace("\n","")
            if word.startswith(beginning):
                word_list.append(word)

    if len(word_list) < n:
        raise ValueError("Not enough suitable words can be found!")
        
    return random.sample(word_list, n)
"""

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
