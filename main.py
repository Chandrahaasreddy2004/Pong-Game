from turtle import Turtle,Screen
from create_paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard

score=ScoreBoard()
screen=Screen()
screen.tracer(0)
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("black")

r_paddle=Paddle((370,0))
l_paddle=Paddle((-370,0))



screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")

screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

ball=Ball()

is_on=True

while is_on:
    time.sleep(ball.time)
    screen.update()
    ball.move()
    if(ball.xcor()>380):
        ball.reset_position()
        score.Left()
    if (ball.xcor() < -380):
        ball.reset_position()
        score.Right()
    if(ball.ycor()>270) or (ball.ycor()<-270):
        ball.y_bounce()

    if(ball.xcor()>340 and ball.distance(r_paddle)<50) or (ball.ycor()>-340 and ball.distance(l_paddle)<50):
        ball.x_bounce()






















screen.exitonclick()