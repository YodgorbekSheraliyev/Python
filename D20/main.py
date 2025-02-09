from turtle import Turtle, Screen
import time
from snake import Snake


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake = Snake()

screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    time.sleep(0.2)
    screen.update()

    snake.move()


screen.exitonclick()
