from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1


    def display_score(self):
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def increase_level(self):
        self.level+=1
        self.clear()
        self.display_score()
        
    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
