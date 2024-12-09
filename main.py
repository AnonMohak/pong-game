from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "o")
screen.onkeypress(r_paddle.go_down, "l")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect the collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        # hits top or bottom wall.
        # needs to be bounced
        ball.bounce_y()

    # detect collision with paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when right paddle misses.
    if ball.xcor() > 380:
        ball.reset_pos()
        ball.bounce_x()
        score.l_point()

    # detect when left paddle misses.
    if ball.xcor() < -380:
        ball.reset_pos()
        ball.bounce_x()
        score.r_point()

screen.exitonclick()
