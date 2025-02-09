class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.seats = 5

    def enter_race_mode(self):
        self.seats = 2
        

user = User(1, "Yodgorbek")

print(user)