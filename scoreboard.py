from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.display()

    def add_score(self):
        self.score += 1
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over Score: {self.score}", align=ALIGNMENT, font=FONT)
