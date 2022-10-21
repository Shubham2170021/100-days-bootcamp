import time
from turtle import Screen, ycor
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
# screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player=Player()
car=CarManager()
score=Scoreboard()
screen.onkey(player.move_forward,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.car_move()
    for cars in car.list:
        if cars.distance(player)<20:
            game_is_on=False
            score.game_over()
    if player.finish_line():
        player.go_to_start()
        car.level_up()
        score.level_increse()
screen.exitonclick()
