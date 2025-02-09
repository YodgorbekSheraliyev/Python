from turtle import Turtle
import random

CAR_COLORS = ["black", "yellow", "green", "red", "blue", "orange", "purple", "pink"]
MOVE_DISTANCE = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = 0.2

    def generate_car(self):
        create_chance = random.randint(1, 6)
        if create_chance == 1:
            position_y = random.randint(-250, 250)
            car = Turtle("square")
            car.color(random.choice(CAR_COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.hideturtle()
            car.penup()
            car.goto(280, position_y)
            car.setheading(180)
            car.showturtle()
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.forward(MOVE_DISTANCE)

    def speed_car(self):
        self.car_speed *= 0.75
