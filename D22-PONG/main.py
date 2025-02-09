from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(1200, 780, 0, 0)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Score()
ball = Ball()


screen.listen()
screen.onkeypress(l_paddle.go_up,'w')
screen.onkey(ball.stop,'space')
screen.onkeypress(l_paddle.go_down,'s')
screen.onkeypress(r_paddle.go_up,'Up')
screen.onkeypress(r_paddle.go_down,'Down')

game_is_on = True
while game_is_on: 
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) > 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()