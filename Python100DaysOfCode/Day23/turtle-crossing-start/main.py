import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()
cars_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player1.up, "Up")

i = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars_manager.move()
    i += 1

    if i <= 6:
        pass
    else:
        cars_manager.create_cars()
        i = 0

    if player1.ycor() >= 290:
        scoreboard.add_level()
        cars_manager.add_speed()
        player1.initial_position()


    for car in cars_manager.cars[1:]:
        if player1.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
