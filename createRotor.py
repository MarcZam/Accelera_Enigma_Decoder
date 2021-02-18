import random

letters="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def createRotor():

    result = []
    otherLetters = letters

    for letter in letters:
        n = random.randrange(len(otherLetters))
        result.append((letter, otherLetters[n]))
        otherLetters = otherLetters[0:n] + otherLetters[(n+1):]
    return result
    
r1 = createRotor()

print(r1)