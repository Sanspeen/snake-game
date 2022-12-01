from turtle import Turtle


class Snake:
    def __init__(self):
        self.body_parts = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in self.starting_positions:
            square = Turtle()
            square.penup()
            square.shape("square")
            square.color("white")
            square.goto(position)
            self.body_parts.append(square)

    def snake_move(self):
        for body_part_num in range(len(self.body_parts) - 1, 0, -1):
            new_x = self.body_parts[body_part_num - 1].xcor()
            new_y = self.body_parts[body_part_num - 1].ycor()
            self.body_parts[body_part_num].goto(new_x, new_y)
        self.body_parts[0].forward(20)
