# class Animal:
#     def __init__(self):
#         self.eyes = 2
#     def breathe(self):
#         print("Inhale. Exhale")
#     def move(self):
#         print("Moving")


# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#     def swim():
#         print("Swimming")
#     def breathe():
#         super().breathe()

# fish = Animal()



# fish.breathe()
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.color('white')
tim.hideturtle()
tim.goto(0, 150)
tim.write("GAME", align='center')

screen.bgcolor('black')


screen.exitonclick()