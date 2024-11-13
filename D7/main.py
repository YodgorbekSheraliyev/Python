import random

words_list = ["aardvark", "alphabet", "book", "price"]
chosen_word = random.choice(words_list)
placeholder = ""
words_length = len(chosen_word)

for position in range(words_length):
    placeholder += "_"

print(chosen_word)
print(placeholder)

lives = 6
stages= []
game_over = False
correct_letters = []

while not game_over:
    display = ""
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            display +=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if guess not in chosen_word:
        lives -=1
        print(f"You have chosen wrong letter {guess}!!!")
    print(f"You have {lives}/6 lives")

    if "_" not in display:
        game_over = True
        print("You win!")
    if lives == 0:
        game_over = True
        print("You lose!")
    print(display)

    print(stages[lives])


