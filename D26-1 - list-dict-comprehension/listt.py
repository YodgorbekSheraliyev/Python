my_list = [1,2,3]
alphabet = ["Alpha", "Beta", "Charlie", "Diamond", "Elephant"]

new_list = [n*2 for n in range(1, 5)]
# new_list = [new_item for item in items]
# new_list = [item * 2 for item in items if test]
UPPER_LIST = [name.upper() for name in alphabet if name.__len__() < 5 ]

print(UPPER_LIST)