## Count each character of a word and display it using stars(*)

def histogram(s):
    dictS = {}

    for i in range(len(s)):
        # Character from string = 1 + the current value of that key(character) or 0 if not in dictionary
        dictS[s[i]] = 1 + dictS.get(s[i],0)

    for k,v in dictS.items():
        star= "*"
        print(f"{k} {star* v}")

if __name__ == "__main__":
    histogram("statistically")