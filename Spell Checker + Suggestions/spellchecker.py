from difflib import get_close_matches

def spellchecker(word):
    with open('wordlist.txt') as file:
        all_words =  []
        for row in file:
            all_words.append(row.strip())

    text = ""
    parts = word.split(" ")
    suggest = {}


    for x in parts:
        if x not in all_words:
            text += f"*{x}* "
            suggest[x] = get_close_matches(x,all_words)      
        else:
            text += f"{x} "

    print(text)
    print('Suggestions:')
    for k,v in suggest.items():
        print(f"{k}: {', '.join(str(x)for x in v)}")
    
    

if __name__ == "__main__":
    word = input("write text:")
    spellchecker(word)