import turtle
import colorgram
import random

colors = colorgram.extract('1.jpg', 10)
color_list = []
def color_picker():
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_list.append((r, g, b))

color_picker()
print(color_list)


def draw_shape(tilt, radius):
    tim = turtle.Turtle()
    turtle.colormode(255)
    tim.color(random.choice(color_list))
    tim.speed('fastest')
    iteration_count = int(360/tilt)
    for _ in range(iteration_count):
        tim.circle(radius)
        tim.setheading(tim.heading() + tilt)

draw_shape(10, 100)
draw_shape(10, 200)
draw_shape(10, 140)
draw_shape(10, 170)



screen = turtle.Screen()
screen.exitonclick()