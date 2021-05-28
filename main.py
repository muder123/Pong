from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, 's')
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    # Detect collison with paddle
    if ball.xcor()>320 and ball.distance(r_paddle)<50 or ball.xcor()<-320 and ball.distance(l_paddle)<50:
        ball.bounce_x()
        
    # reset if beyond boundary
    # left play scores
    if ball.xcor()>380:
        ball.reset_position()
        score.left_scores()

    # right play scores
    if ball.xcor()<-380:
        ball.reset_position()
        score.right_scores()

screen.exitonclick()