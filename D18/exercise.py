from turtle import Screen, Turtle
import math

turtle = Turtle('classic')


def draw_shape(num_of_sides):
    angle = 360/num_of_sides
    for _ in range(num_of_sides):
        turtle.forward(80)
        turtle.right(angle)

colors = ['black', 'blue', 'red', 'yellow', 'orange', 'pink', 'purple', 'gray', 'aqua', 'black', 'blue', 'red', 'purple', 'gray', 'aqua', 'black', 'blue', 'red']
for shape in range(3, 51):
    # turtle.home()
    turtle.penup()
    turtle.goto(0, 150)
    turtle.pendown()
    draw_shape(shape)
    turtle.pencolor(colors[shape])


screen = Screen()
screen.exitonclick()

