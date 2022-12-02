from turtle import Turtle
X_POS = 0
Y_POS = 280
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=X_POS, y=Y_POS)
        self.write_score()

    def add_score(self):
        """Keeps track of score"""
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        """Updates scoreboard"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
