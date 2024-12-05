from random import randint

def guesser():
    print("Guess number between 1 and 100")
    random_number = randint(1, 100)
    attempts = 10
    print(f"Random number is {random_number}")
    is_game_over = False
    level = input("Choose a level: easy / hard \n")
    if level == "hard":
        attempts = 5
    print(f"You chose {level}, you have {attempts} attempts")
    while not is_game_over:
        guess = int(input("Enter a guess: "))
        if guess < random_number:
            print("Your guess is too low")
            attempts -= 1
        elif guess > random_number:
            print("Your guess is too high")
            attempts -= 1
        else:
            print("You got it!")
            is_game_over = True
            return
        print(f"You have {attempts} attempts")

guesser()