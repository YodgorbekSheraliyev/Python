import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager


player = Player()
score = Scoreboard()
car_manager = CarManager()

screen = Screen()
screen.setup(600,600)
screen.tracer(0)
screen.listen()



screen.onkey(player.move, 'w')

game_is_on = True

while game_is_on:
    time.sleep(car_manager.car_speed)
    car_manager.generate_car()
    car_manager.move_car()
    screen.update()

    for car in car_manager.cars:
        if car.distance(player) < 25:
            game_is_on = False
            score.game_over()

    if player.ycor() > 280:
        score.update_score()
        player.go_to_start()
        car_manager.speed_car()


screen.exitonclick()