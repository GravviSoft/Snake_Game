from turtle import Turtle

FONT = ("arial", 18, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-50, 260)
        self.hideturtle()
        self.write(f"Score is: {self.score}", move=True, font=FONT)

    def scoring(self):
        self.clear()
        self.goto(-50, 260)
        self.score += 1
        self.write(f"Score is: {self.score}", move=True, font=FONT)

    def game_over(self):
        self.goto(-40, 0)
        self.write(f"Game Over.", move=True, font=FONT)