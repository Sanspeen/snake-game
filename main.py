from turtle import Screen, Turtle
import time
from snake import Snake
SNAKE_SPEED = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
screen.listen()

snake = Snake()
screen.onkey(snake.look_up, "Up")
screen.onkey(snake.look_down, "Down")
screen.onkey(snake.look_left, "Left")
screen.onkey(snake.look_right, "Right")


screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SNAKE_SPEED)
    snake.snake_move()

screen.exitonclick()
