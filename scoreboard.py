from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.goto(0, 0)
        self.levels = 0
        self.penup()


    def lost(self):
        self.goto(0, 0)
        self.write(arg="You Lose", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.goto(-240, 250)
        self.levels += 1
        self.write(arg=f"LEVEL {self.levels}", align="center", font=FONT)

