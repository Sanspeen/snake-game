from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)


def look_left(turtle):
    turtle.left(90)


body_parts = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    square = Turtle()
    square.penup()
    square.shape("square")
    square.color("white")
    square.goto(position)
    body_parts.append(square)

screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    for body_part_num in range(len(body_parts) - 1, 0, -1):
        new_x = body_parts[body_part_num - 1].xcor()
        new_y = body_parts[body_part_num - 1].ycor()
        body_parts[body_part_num].goto(new_x, new_y)
    body_parts[0].forward(20)

screen.exitonclick()