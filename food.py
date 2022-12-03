import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        pos_x = random.randint(-280, 280)
        pos_y = random.randint(-280, 280)
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.goto(pos_x, pos_y)

    def relocate(self):
        pos_x = random.randint(-280, 280)
        pos_y = random.randint(-280, 280)
        self.goto(pos_x, pos_y)
