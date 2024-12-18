import random
questions = [
    {
        "description": "Ronaldo",
        "followers": 10000
    },
    {
        "description": "Tim",
        "followers": 10000
    },
    {
        "description": "Selena Gomez",
        "followers": 100000
    },
    {
        "description": "Tor",
        "followers": 100001
    },
    {
        "description": "Messi",
        "followers": 9000
    },
    {
        "description": "Neymar",
        "followers": 8000
    },
    {
        "description": "Hulk",
        "followers": 90000
    },
    {
        "description": "Spider Man",
        "followers": 85000
    },
    
]


def higher_or_lower():
    score = 0
    print("Welcome to the Higher or Lower game")
    random_1 = random.choice(questions)
    random_2 = random.choice(questions)
    while True:
        print(f"Compare A: {random_1["description"]}")
        print("VS")
        print(f"Against B: {random_2["description"]}")
        while True:
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            if guess not in ["a", "b"]:
                print("Please select correct option!!! ")
                continue
            break
        if guess == "a":
            if random_1["followers"] >= random_2["followers"]:
                score +=1
                print(f"You are right! Current score {score}")
                random_1 = random_2
                random_2 = random.choice(questions)
            else:
                print(f"You lose! Your score is {score}")
                break
        else:
            if random_1["followers"] <= random_2["followers"]:
                score +=1
                print(f"You are right! Current score {score}")
                random_1 = random_2
                random_2 = random.choice(questions)
            else:
                print(f"You lose! Your score is {score}")
                break

higher_or_lower()        

