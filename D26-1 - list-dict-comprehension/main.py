alphabet = ["Alpha", "Beta", "Charlie", "Diamond", "Elephant"]

def name():
    name = input("Enter your name: \n").upper()
    word_list = []
    for letter in name:
        for word in alphabet:
            if word.startswith(letter):
                word_list.append(word)
        
    return word_list
print(name())
        
# print(name)rgerg
