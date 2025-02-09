from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-230, 260)
        self.color('black')
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align='center', font=("Arial", 20, 'normal'))

    def update_score(self):
        self.score +=1
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align='center', font=("Arial", 40, 'normal'))
