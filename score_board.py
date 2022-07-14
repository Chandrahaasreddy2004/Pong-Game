from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.right=0
        self.left=0
        self.UpdateScoreBoard()

    def UpdateScoreBoard(self):
        self.clear()
        self.goto(100, 200)
        self.write(f"{self.right}",align="center",font=("courier",80,"normal"))
        self.goto(-100, 200)
        self.write(f"{self.left}", align="center", font=("courier", 80, "normal"))

    def Right(self):
        self.right+=1
        self.UpdateScoreBoard()

    def Left(self):
        self.left+=1
        self.UpdateScoreBoard()