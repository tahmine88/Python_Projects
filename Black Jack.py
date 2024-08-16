import random

def deal_card():
    """ Returns a random card from the deck. """
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Values in Blackjack
    return random.choice(cards)

def calculate_score(cards):
    """ Calculate the score of the current hand. """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Represents a blackjack in the game
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def blackjack_game():
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if user_score > 21:
        return "You went over. You lose 😤"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

print(blackjack_game())
