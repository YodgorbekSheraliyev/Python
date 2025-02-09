alphabet = ["Alpha", "Beta", "Charlie", "Diamond", "Elephant"]
import random


# my_dict = {key_name: key_value for item in list}
my_dict = {item: random.randint(50, 100) for item in alphabet}
my_new_dict = {key: value for (key, value) in my_dict.items()}
print(my_new_dict)