from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(6, 1)
        self.penup()
        self.goto(pos)
        self.line = []

    def up(self):
        x = self.xcor()
        y = self.ycor() + 15
        self.goto(x, y)

    def down(self):
        x = self.xcor()
        y = self.ycor() - 15
        self.goto(x, y)
