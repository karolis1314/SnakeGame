from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.updateScoreBoard()
        self.hideturtle()

    def updateScoreBoard(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.clear()
        self.score += 1
        self.updateScoreBoard()
