import random


def random_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def score_calculation(cards):
    """Takes a list of the cards and returns the score calculated"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare_scores(u_score, c_score):
    """Compare the users score against the computers score"""
    if u_score == c_score:
        return "Draw :("
    elif c_score == 0:
        return "Lose! Computer has Blackjack :("
    elif u_score == 0:
        return "You win with Blackjack 😎"
    elif u_score > 21:
        return "You busted. You lose :("
    elif c_score > 21:
        return "Computer busted. You won!!"
    elif u_score > c_score:
        return "You won!"
    else:
        return "You lose :("
    
def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_games_over = False
    
    for _ in range(2):
        user_cards.append(random_cards())
        computer_cards.append(random_cards())

    
    while not is_games_over:
        user_score = score_calculation(user_cards)
        computer_score = score_calculation(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computers first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_games_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == "y":
                user_cards.append(random_cards())
            else:
                is_games_over = True
    
    while computer_cards != 0 and computer_score < 17:
        computer_cards.append(random_cards())
        computer_score = score_calculation(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' yes or 'n' for no: ") == "y":
    print("\n" * 20)
    play_game()