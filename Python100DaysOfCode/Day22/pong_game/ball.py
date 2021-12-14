from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.8, 0.8)
        self.color("white")
        self.penup()
        self.speed(0.1)
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(9)
