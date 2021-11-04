import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\nEnter a color:").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = ["turtle0", "turtle1", "turtle2", "turtle3", "turtle4", "turtle5"]

y = 75

for i in range(len(colors)):
    turtles[i] = Turtle(shape="turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=y)
    y -= 30


if user_input:
    is_race_on = True

while is_race_on:
    for i in range(len(turtles)):
        random_distance = random.randint(0, 10)
        turtles[i].forward(random_distance)
        if turtles[i].xcor() >= 200:
            if user_input == colors[i]:
                print(f"You won! The {colors[i]} turtle is the winner!")
            else:
                print(f"You lost! The {colors[i]} turtle is the winner!")
            is_race_on = False
            break


# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def turn_left():
#     tim.left(10)
#
#
# def turn_right():
#     tim.right(10)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)


screen.exitonclick()
