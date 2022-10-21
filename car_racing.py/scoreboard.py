from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.lavel=1
        self.lavel_1()
    def lavel_1 (self):
        self.penup()
        self.goto(-260,260)
        self.write(f"Level :{self.lavel}",False,align="left",font=FONT)
        self.hideturtle()
    def level_increse(self):
        self.lavel+=1
        self.clear()
        self.lavel_1()
    def game_over(self):
        self.clear()
        self.write(f"game over,your level is {self.lavel}",False,align="left",font=FONT)
