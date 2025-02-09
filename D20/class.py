class Animal:
    def __init__(self):
        self.eyes = 2
    def breathe(self):
        print("Inhale. Exhale")
    def move(self):
        print("Moving")


class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim():
        print("Swimming")
    def breathe():
        super().breathe()

fish = Animal()



fish.breathe()