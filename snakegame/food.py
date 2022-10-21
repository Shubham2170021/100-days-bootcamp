from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        #create inheritance class
        super().__init__()
        #create food part
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.refrash()
    def refrash(self):
        x_axis=random.randint(-280,280)
        y_axis=random.randint(-280,280)
        self.goto(x_axis,y_axis)


