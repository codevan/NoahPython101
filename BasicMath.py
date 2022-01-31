#A simple maths game
#2nd Python Project

import random
import string
import time

player_score = 0


def getRandomNumber(min, max):
    return random.randint(min, max)



print("Welcome to the maths game!")
while True:
    Number1 = getRandomNumber(1,10)
#print(Number1)
    Number2 = getRandomNumber(1,10)
#print(Number2)
    print("What is " + str(Number1) + " + " + str(Number2) + "?")
    Answer = Number1 + Number2

    #print("Hint:  The answer is " + str(Answer))

    #if input() == "4":
    if input() == str(Answer):
        print("Correct, you brainiac, you!")
        player_score += 1
    else:
        print("Wrong, go back to school!")

    time.sleep(1)
    answer = input("Would you like to play again? y/n: ")
    if answer in("y", "Y"):
                print("Let's do this again!")
    else:
        print("Thanks for playing!")
        print("HIGH SCORE: " + str(player_score))
        break




