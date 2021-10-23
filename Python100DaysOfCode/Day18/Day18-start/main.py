import turtle
from turtle import Turtle, Screen
from random import choice, randint

turtle.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    timmy.color((r, g, b))

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkOliveGreen")

# # CHALLENGE 3
# colors = ["DarkOliveGreen", "MediumBlue", "OrangeRed", "Indigo", "Peru", "LightSkyBlue", "Gold"]
# sides = 2
# for n in range(7):
#     sides += 1
#     angle = 360 / sides
#     timmy.pencolor(colors[n])
#     for i in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)

# # CHALLENGE 4
# direction = [0, 90, 180, 270]
#
# timmy.pensize(15)
# timmy.speed(10)
# for n in range(200):
#     random_color()
#     timmy.forward(30)
#     timmy.setheading(direction[randint(0, 3)])
#
# timmy.hideturtle()

# CHALLENGE 5
direction = 5
timmy.speed(0)
timmy.pensize(1)
for i in range(72):
    random_color()
    timmy.circle(100)
    timmy.left(direction)



screen = Screen()
screen.exitonclick()
