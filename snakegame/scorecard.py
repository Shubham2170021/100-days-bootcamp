from turtle import Turtle

class ScoreCard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score=0
        with open("data.txt") as f:
            self.highscore=int(f.read())
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score :{self.score} High Score :{self.highscore}",False,align="center",font=('Arial', 15, 'normal'))
    def increse_scores(self):
        self.score=self.score+1
        self.update_score()
    def resetscore(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt","w") as f:
                f.write(f"{self.highscore}")
        self.score=0
        self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game over! Your score is {self.score}",False,align="center",font=('Arial', 15, 'normal'))

