from turtle import Screen, Turtle
import time
from Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()

screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.snake_move()

screen.exitonclick()
