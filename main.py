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

game = Turtle()
game.color("white")
game.penup()
game.goto(-300, 300)
game.pendown()
game.setheading(0)
game.ht()
game.width(6)
for i in range(0, 4):
    game.forward(600)
    game.right(90)

scoreboard = Scoreboard()
snake = Snake()
food = Food()
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

    for segment in snake.body_parts:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    screen.update()
screen.exitonclick()
