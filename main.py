from turtle import Screen
from paddle import Paddle
from middle_line import MiddleLine
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

l_paddle = Paddle((-480, 0))
l_score = Score((-80, 250))
r_paddle = Paddle((472, 0))
r_score = Score((80, 250))

line = MiddleLine()
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

x_distance, y_distance = 1, 1
game_on = True
while game_on:
    if ball.ycor() > 280:
        y_distance *= -1
    elif ball.ycor() < -280:
        y_distance *= -1
    elif ball.xcor() > 465:
        if ball.distance(r_paddle) < 60:
            x_distance *= -1
        else:
            l_score.score_up()
            ball.goto(0, 0)
            x_distance = -1
            time.sleep(1)
    elif ball.xcor() < -475:
        if ball.distance(l_paddle) < 60:
            x_distance *= -1
        else:
            r_score.score_up()
            ball.goto(0, 0)
            x_distance = 1
            time.sleep(1)

    ball.move(x_distance, y_distance)
    screen.update()

screen.exitonclick()
