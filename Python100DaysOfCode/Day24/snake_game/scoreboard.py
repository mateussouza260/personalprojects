from turtle import Turtle
ALIGNMENT = 'left'
FONT = ('Arial', 14, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(-40, 270)
        self.hideturtle()
        self.clear()
        self.color("white")
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.show_score()

    def add_point(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.show_score()
