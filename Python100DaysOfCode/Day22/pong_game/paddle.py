from turtle import Turtle
PADDLEWIDTH = 1
PADDLEHEIGTH = 5


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.left(90)
        self.goto(x, y)
        self.shapesize(PADDLEWIDTH, PADDLEHEIGTH)
        self.color("white")
        self.penup()

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)


    # Create border and calculate distance from paddle to autorize use of function based on the position
