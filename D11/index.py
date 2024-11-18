import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
    
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)      

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "Win with a blackjack"
    elif computer_score == 0:
        return "Lose opponent has a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Computer lose. Opponent went over"
    elif user_score > computer_score:
        return "You win"
    elif user_score < computer_score:
        return "You lose"
    else: 
        return "You lose"

def play_game():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not is_game_over:    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, your score {user_score}")
        print(f"Computer's first card: {computer_cards[0]}, your score {computer_score}")

        if user_score ==0 or computer_score ==0 or user_score >21:
            is_game_over = True
        else:
            user_should_deal = input("Type y to get another card, or no to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else: 
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards) 

    print(compare(user_score, computer_score))

while input("Would you like to get card ? Type y for yes or n for pass: ") == "y":
    # print("\n"*20)
    play_game()

