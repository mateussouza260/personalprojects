from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
HEADING = 180
X_RIGHT_POS = 300
X_LEFT_POS = -300
Y_TOP_POS = 250
Y_BOTTOM_POS = -250


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE

    def initial_position(self):
        x_pos = X_RIGHT_POS
        y_pos = randint(Y_BOTTOM_POS, Y_TOP_POS)
        self.goto(x_pos, y_pos)

    def create_cars(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.setheading(HEADING)
        x_pos = X_RIGHT_POS
        y_pos = randint(Y_BOTTOM_POS, Y_TOP_POS)
        new_car.goto(x_pos, y_pos)
        new_car.color(choice(COLORS))
        self.cars.append(new_car)

    def add_speed(self):
        self.speed += MOVE_INCREMENT
        print(self.speed)

    def move(self):
        for n in range(len(self.cars) - 1):
            self.cars[n].forward(self.speed)


