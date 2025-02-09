from random import choice, randint
import turtle

turtle.colormode(255)

angles = [90, 180, 270, 0]
colors = ['red', 'green', 'blue', 'black', 'gray', 'pink', 'purple', 'orange', 'aqua', 'yellow', 'violet']

turtle = turtle.Turtle()

def color_picker():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

turtle.speed(10)
turtle.pensize(10)




while True:
    turtle.color(color_picker())
    turtle.fd(20)
    turtle.setheading(choice(angles))
    # turtle.pencolor(choice(colors))


screen = turtle.Screen()
screen.exitonclick()