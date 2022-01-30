from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
FILE_LOCATION = "data.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open(FILE_LOCATION, mode="r") as file:
            score = file.read()
            if score == "":
                self.high_score = 0
            else:
                self.high_score = int(score)
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
        self.write(f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_to_file()
        self.score = 0
        self.display()

    def write_to_file(self):
        with open(FILE_LOCATION, mode="w") as file:
            file.write(str(self.high_score))

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"Game Over Score: {self.score}", align=ALIGNMENT, font=FONT)
