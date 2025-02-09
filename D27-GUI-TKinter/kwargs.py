def add(n, **kwargs):
    n+= kwargs['add']
    n *= kwargs['multiply']
    print(n)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs['model']

my_car = Car(model='Chevrolet')

print(my_car.model)