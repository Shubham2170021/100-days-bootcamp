import time
from turtle import Screen
from food import Food
from snake import Snake
from scorecard import ScoreCard
screen=Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.tracer(0)
snake=Snake()
food=Food()
score=ScoreCard()
screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.head.distance(food)<15:
        food.refrash()
        score.increse_scores()
        snake.extend()
    if snake.head.xcor()>295 or snake.head.xcor()<-295 or snake.head.ycor()>295 or snake.head.ycor()<-295:
        # game_on=False
        score.resetscore()
        snake.repostionsnake()
    for seg in snake.snake:
        if seg==snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            # game_on=False
            score.resetscore()
            snake.repostionsnake()

            





screen.exitonclick()