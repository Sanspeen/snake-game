from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        square = Turtle()
        square.penup()
        square.shape("square")
        square.color("green")
        square.goto(position)
        self.body_parts.append(square)

    def extend(self):
        self.add_segment(self.body_parts[-1].position())

    def snake_move(self):
        for body_part_num in range(len(self.body_parts) - 1, 0, -1):
            new_x = self.body_parts[body_part_num - 1].xcor()
            new_y = self.body_parts[body_part_num - 1].ycor()
            self.body_parts[body_part_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def look_up(self):
        if round(self.head.heading()) != DOWN:
            self.head.setheading(UP)

    def look_down(self):
        if round(self.head.heading()) != UP:
            self.head.setheading(DOWN)

    def look_left(self):
        if round(self.head.heading()) != RIGHT:
            self.head.setheading(LEFT)

    def look_right(self):
        if round(self.head.heading()) != LEFT:
            self.head.setheading(RIGHT)

    def hit_wall(self):
        self.head.bye()
