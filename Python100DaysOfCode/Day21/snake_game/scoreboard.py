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
        self.show_score()

    def add_point(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
