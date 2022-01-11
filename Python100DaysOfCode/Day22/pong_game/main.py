from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREENWIDTH = 800
SCREENHEIGHT = 600
ANGLE = 90

screen = Screen()
screen.bgcolor("black")
screen.setup(SCREENWIDTH, SCREENHEIGHT)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    # detect collision between ball and wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision between ball and paddle
    if ball.xcor() > 320 or ball.xcor() < -320:
        if l_paddle.distance(ball) < 50 or r_paddle.distance(ball) < 50:
            ball.bounce_x()

    # detect if ball goes out of bounds
    if ball.xcor() > 380:
        scoreboard.l_add_point()
        ball.resetting()

    if ball.xcor() < -380:
        scoreboard.r_add_point()
        ball.resetting()


screen.exitonclick()
