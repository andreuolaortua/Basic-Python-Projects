import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import pandas
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")
car = CarManager()
score = Scoreboard()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    for car in car.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

screen.exitonclick()