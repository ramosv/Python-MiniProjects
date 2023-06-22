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
