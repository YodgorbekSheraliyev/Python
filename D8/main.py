# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice?")
    
    
# # greet()

# def greet_with_name(name, location):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print(f"Isn't the weather nice {location}?")

# greet_with_name(location="Andijon", name="Yodgorbek")


def calculate_love_score(name1, name2):
    word1 = "true"
    word2 = "love"
    
    word1_list = 0
    word2_list = 0
    for letter in name1.lower():
        if letter in word1:
            word1_list +=1
        if letter in word2:
            word2_list +=1
    for letter in name2.lower():
        if letter in word1:
            word1_list +=1
        if letter in word2:
            word2_list +=1
    print(f"{word1_list}{word2_list}")
            
calculate_love_score("Yodgorbek", "Sheraliyev")