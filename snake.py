from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            xy_cor = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(xy_cor)
        self.segments[0].fd(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def add_segment(self, position):
        body = Turtle("square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.segments.append(body)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for body in self.segments:
            body.goto(1000, 1000)
        self.segments.clear()
        self.__init__()
