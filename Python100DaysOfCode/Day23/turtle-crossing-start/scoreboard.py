from turtle import Turtle
from car_manager import CarManager
ALIGNMENT = 'left'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto(-280, 250)
        self.color("black")
        self.add_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def add_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", align=ALIGNMENT, font=FONT)



