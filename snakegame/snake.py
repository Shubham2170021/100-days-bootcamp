from turtle import Turtle
POSTION=[(0,0),(-20,0),(-40,0)]
MOVE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.snake=[]
        self.create_snake()
        self.head=self.snake[0]
    def create_snake(self):
        for item in range(3):
           self.upadate_snake(POSTION[item])
    def upadate_snake(self,POSTION):
        tim=Turtle(shape="square")
        tim.speed("fastest")
        tim.penup()
        tim.color("white")
        tim.goto(POSTION)
        self.snake.append(tim)
    def extend(self):
        self.upadate_snake(self.snake[-1].position())
    def move(self):
        for seg_num in range(len(self.snake)-1,0,-1):
            #for changing postion of turtle
            x_cor=self.snake[seg_num-1].xcor()
            y_cor=self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(x_cor,y_cor)
        self.head.forward(MOVE)
        # self.snake[0].left(90)
    def move_right(self):
        if self.head.heading()!=LEFT:
            # self.head.heading() change head of snake
            self.snake[0].setheading(RIGHT)
    def move_left(self):
        if self.head.heading()!=RIGHT:
            self.snake[0].setheading(LEFT)
    def move_up(self):
        if self.head.heading()!=DOWN:
            self.snake[0].setheading(UP)
    def move_down(self):
        if self.head.heading()!=UP:
            self.snake[0].setheading(DOWN)
    def repostionsnake(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head=self.snake[0]
        
