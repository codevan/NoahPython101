#A simple maths game
#2nd Python Project

import random
import string

player_score = 0


def getRandomNumber(min, max):
    return random.randint(min, max)

Number1 = getRandomNumber(1,5)
print(Number1)
Number2 = getRandomNumber(1,5)
print(Number2)

print("Welcome to the maths game!")
print("What is Number1 + Number2?")
Answer = Number1 + Number2


if input() == "4":
#if input() == Answer:
    print("Correct, you brainiac, you!")
    player_score += 1
else:
    print("Wrong, go back to school!")

