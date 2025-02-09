from turtle import Screen, Turtle
import random


tim = Turtle()
screen = Screen()
name_of_turtle = screen.textinput("Turtle race", "What turtle do you choose")

red = Turtle()
green = Turtle()
blue = Turtle()
grey = Turtle()
yellow = Turtle()
orange = Turtle()

turtle_list = [red, green, blue, grey, yellow, orange]
turtle_colors = ('red', 'green', 'blue', 'grey', 'yellow', 'orange')
interval = [20, 60, 15, 85, 10, 50]
y_position = -250
for t, c in zip(turtle_list, turtle_colors):
    t.penup()
    t.shape('turtle')
    t.goto((-350, y_position))
    t.color(c)
    y_position +=100

def start():
    print(screen.canvwidth)
    for _ in range(10):
        for turtle in turtle_list:
            turtle.fd(random.randint(20, 200))
            if turtle.xcor()>=screen.canvwidth:
                break

screen.title("Turtle")
screen.listen()
screen.onkey(key='space', fun=start)
screen.exitonclick()