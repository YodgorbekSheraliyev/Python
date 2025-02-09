import turtle

class State(turtle.Turtle):
    def __init__(self, position, state):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(f"{state.title()}", font=("Arial", 8, "normal"))

    