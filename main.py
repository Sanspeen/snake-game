from turtle import Screen, Turtle
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

SNAKE_SPEED = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.onkey(snake.look_up, "Up")
screen.onkey(snake.look_down, "Down")
screen.onkey(snake.look_left, "Left")
screen.onkey(snake.look_right, "Right")


screen.update()
game_is_on = True
while game_is_on:

    time.sleep(SNAKE_SPEED)
    snake.snake_move()

    if snake.head.distance(food) < 15:
        scoreboard.add_score()
        food.relocate()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.game_over()
        game_is_on = False

    screen.update()
screen.exitonclick()
