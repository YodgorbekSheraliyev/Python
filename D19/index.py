from turtle import Screen, Turtle
import random


tim = Turtle()
screen = Screen()
name_of_turtle = screen.textinput("Turtle race", "What turtle do you choose")
print(name_of_turtle)

def move_forward():
    tim.forward(50)

def move_backward():
    tim.backward(50)

def rotate_left():
    tim.setheading(tim.heading() + 25)

def rotate_right():
    tim.setheading(tim.heading() - 25)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()





screen.listen()
screen.onkeypress(move_forward, 'w')
screen.onkeypress(move_backward, 's')
screen.onkeypress(rotate_left, 'a')
screen.onkeypress(rotate_right, 'd')
screen.onkeypress(clear, 'c')


screen.title("Turtle")
screen.exitonclick()