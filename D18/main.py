from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape('turtle')
turtle.color("red")
turtle.speed(-1)
turtle.setx(-50)
turtle.sety(-50)
for _ in range(50):
    turtle.heading()
    turtle.forward()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()



screen = Screen()

screen.tracer()
screen.exitonclick()