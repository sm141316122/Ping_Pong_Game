from turtle import Turtle
POSITION = [(0, 280), (0, 230), (0, 180), (0, 130),
            (0, 80), (0, 30), (0, -20), (0, -70),
            (0, -120), (0, -170), (0, -220), (0, -270)]


class MiddleLine:

    def __init__(self):
        self.line = []
        self.create_line(POSITION)

    def create_line(self, position):
        for pos in position:
            line = Turtle("square")
            line.color("white")
            line.shapesize(1.5, 0.5)
            line.penup()
            line.goto(pos)
            self.line.append(line)

