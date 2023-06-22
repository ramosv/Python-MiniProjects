## Python password generator.
## def generate_strong_password(length of pass, want numbers?, special characters)

## Python password generator.
## def generate_strong_password(length of pass, want numbers?, special characters)

from string import ascii_letters, punctuation,digits
from random import randint, choice

def generate_strong_password(size,numbers = False,special = False):
    password = ""
    
    for x in range(size):
        rand = randint(1,3)
        if rand == 1:
            password += choice(ascii_letters)
        elif rand == 2 and numbers == True:
            password += choice(digits)
        elif rand == 3 and special == True:
            password += choice(punctuation)
        else:
            password += choice(ascii_letters)
    
    return password

if __name__ == "__main__":
    for i in range(5):
        print(generate_strong_password(15,True,True))


