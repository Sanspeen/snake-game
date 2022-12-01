from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
body_parts = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    square = Turtle()
    square.shape("square")
    square.color("white")
    square.goto(position)
    body_parts.append(square)







screen.exitonclick()