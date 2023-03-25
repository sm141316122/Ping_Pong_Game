from turtle import Turtle


class Score(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(pos)
        self.refresh()

    def refresh(self):
        self.write(f"Score: {self.score}", align="center", font=('Arial', 18, 'normal'))

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 18, 'normal'))
