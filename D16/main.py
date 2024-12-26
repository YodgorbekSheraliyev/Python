# import module
# import math
# from turtle import Turtle, Screen
# print(module.variable)

# timmy = Turtle(shape='turtle', undobuffersize=2000, visible=True)
# timmy.color('burlywood')
# timmy.right(90)
# timmy.forward(100)
# timmy.circle(math.pi)
# timmy.forward(100)
# screen = Screen()
# screen.setup(600, 400)
# screen.exitonclick()
# print(timmy)

from prettytable import PrettyTable
table = PrettyTable()

table.add_column('Name', ['Name1', 'Name2', 'Name3'])
table.add_column('Surname', ['Name1', 'Name2', 'Name3'], 'r')
print(table)