from turtle import Screen
from paddle import Paddle
from ball import Ball
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

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # detect collision between ball and wall
    # first quadrant
    if ball.xcor() >= 0 and ball.ycor() >= 0:
        if ball.xcor() >= 370:
            if ball.heading() > 0:
                ball.setheading(ball.heading() + ANGLE)
            if ball.heading() < 0:
                ball.setheading(ball.heading() - ANGLE)
        if ball.ycor() >= 290:
            if ball.heading() > 90:
                ball.setheading(ball.heading() + ANGLE)
            if ball.heading() < 90:
                ball.setheading(ball.heading() - ANGLE)
    # second quadrant
    elif ball.xcor() <= 0 and ball.ycor() >= 0:
        if ball.xcor() <= -370:
            if ball.heading() > 180:
                ball.setheading(ball.heading() + ANGLE)
            if ball.heading() < 180:
                ball.setheading(ball.heading() - ANGLE)
        if ball.ycor() >= 290:
            if ball.heading() > 90:
                ball.setheading(ball.heading() + ANGLE)
            if ball.heading() < 90:
                ball.setheading(ball.heading() - ANGLE)
    # third quadrant
    elif ball.xcor() <= 0 and ball.ycor() <= 0:
        if ball.xcor() <= -370:
            if ball.heading() > 180:
                ball.setheading(ball.heading() + ANGLE)
            if ball.heading() < 180:
                ball.setheading(ball.heading() - ANGLE)
        if ball.ycor() <= -290:
            if ball.heading() > 270:
                ball.setheading(ball.heading() + ANGLE)
            if ball.heading() < 270:
                ball.setheading(ball.heading() - ANGLE)
    # fourth quadrant
    elif ball.xcor() >= 0 and ball.ycor() <= 0:
        if ball.xcor() >= 370:
            if ball.heading() > 0:
                ball.setheading(ball.heading() + ANGLE)
            if ball.heading() < 0:
                ball.setheading(ball.heading() - ANGLE)
        if ball.ycor() <= -290:
            if ball.heading() > 270:
                ball.setheading(ball.heading() + ANGLE)
            if ball.heading() < 270:
                ball.setheading(ball.heading() - ANGLE)
    else:
        pass

screen.exitonclick()
