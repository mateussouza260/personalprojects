import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 19:
        scoreboard.add_point()
        food.refresh()
        snake.create_segment()

    # Detect collision with wall
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290:
        scoreboard.reset_scoreboard()
        snake.reset_snake()
    elif snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        scoreboard.reset_scoreboard()
        snake.reset_snake()
    else:
        pass

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
