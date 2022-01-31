#SpaceWar

import os
import random

import turtle
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def _init_(self, spriteshape, color, startx, starty):
        turtle.Turtle._init_(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)

player = Sprite("triangle", "white", 0, 0)


while True:
    player.move()
    








delay = input("Press enter to finish. > ")