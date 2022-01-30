from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
BOUNDARY = 280
NEG_BOUNDARY = -280

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.06)

    snake.move()
    # if snakehead is close (15 pixels) collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()
    # detect collision with wall.
    if snake.head.xcor() > BOUNDARY or snake.head.ycor() > BOUNDARY or \
            snake.head.xcor() < NEG_BOUNDARY or snake.head.ycor() < NEG_BOUNDARY:
        score.game_over()
        game_is_on = False

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
