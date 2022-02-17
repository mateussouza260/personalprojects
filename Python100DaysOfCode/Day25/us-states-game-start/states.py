from turtle import Turtle
FONT = ("Courier", 10, "normal")


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()

    def create_state(self, name, x, y):
        self.goto(x, y)
        self.write(name, align="center", font=FONT)
