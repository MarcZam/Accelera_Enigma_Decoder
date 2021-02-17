import random

letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def CreateRotor():
    result = []
    otherLetters = letters

    for letter in letters:
        n = random.randrange(len(otherLetters))
        result.append((letter, otherLetters[n]))
        otherLetters = otherLetters[0:n] + otherLetters[(n+1):]
    return result


r1 = CreateRotor()

print(r1)