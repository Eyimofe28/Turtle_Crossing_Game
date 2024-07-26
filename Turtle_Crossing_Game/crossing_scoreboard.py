from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.count = 1
        self.score()

    def score(self):
        self.goto(-280, 250)
        self.write(arg=f"Level {self.count}", move=False, align='left', font=("Courier", 20, 'italic'))

    def score_increase(self):
        self.count += 1
        self.clear()
        self.write(arg=f"Level {self.count}", move=False, align='left', font=("Courier", 20, 'italic'))

    def game_over(self):
        self.color('grey')
        self.speed(0)
        self.penup()
        self.goto(0, 0)
        self.write(arg="GAME OVER!", move=False, align='center', font=("Courier", 30, 'bold'))
