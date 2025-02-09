import colorgram
import random
import turtle

turtle.colormode(255)
colors = colorgram.extract("./1.jpg", 50)
color_list = [
    (228, 0, 87),
    (126, 87, 60),
    (48, 170, 224),
    (47, 172, 102),
    (197, 189, 17),
    (235, 220, 0),
    (254, 247, 252),
    (191, 229, 249),
    (210, 202, 145),
    (235, 110, 145),
    (102, 192, 187),
    (227, 25, 114),
    (233, 78, 28),
    (1, 72, 148),
    (218, 176, 69),
    (223, 45, 122),
    (14, 79, 146),
    (244, 159, 193),
    (49, 158, 199),
    (156, 212, 192),
    (143, 208, 230),
    (7, 59, 111),
    (56, 148, 98),
    (244, 173, 151),
    (92, 130, 169),
    (160, 194, 227),
    (81, 60, 47),
    (77, 58, 49),
    (251, 5, 78),
    (78, 62, 49),
]

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))

# print(color_list)


def draw_dots(size, count):
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.speed("fastest")
    t.setheading(225)
    t.fd(350)
    t.setheading(0)
    for _ in range(count):
        t.dot(size, random.choice(color_list))
        for _ in range(count):
            t.color(random.choice(color_list))
            t.fd(50)
            t.dot(size, random.choice(color_list))
        t.setheading(90)
        t.fd(50)
        t.setheading(180)
        t.fd(50 * count)
        t.setheading(0)


draw_dots(20, 10)


screen = turtle.Screen()
screen.exitonclick()
