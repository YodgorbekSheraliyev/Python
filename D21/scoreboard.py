from turtle import Turtle
ALIGNMENT= 'left'
FONT= ("Arial", 8, "normal")

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.show_score() 

    def show_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score +=1
        self.clear()
        self.show_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER")