COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle

class CarManager():
    def __init__(self):
        self.list=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    def create_car(self):
        if random.randint(1,6)==1:
            car=Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1,stretch_len=3)
            car.color(random.choice(COLORS))
            Random_y=random.randint(-250,250)
            self.list.append(car)
            car.goto(290,Random_y)
    def car_move(self):
        for cars in self.list:
            cars.backward(self.car_speed)
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT


