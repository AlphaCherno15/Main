import random as rd
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []
game = True
end = None
for _ in range(2):
    chosen_card = rd.choice(cards)
    player_cards.append(chosen_card)
    chosen_card = rd.choice(cards)
    dealer_cards.append(chosen_card)
def check_victory(player_score, computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == "Blackjack":
        return "lose, opponent has Blackjack"
    elif player_score == "Blackjack":
        return "Win with a Blackjack"
    elif player_score > 21:
        return "You went over, You lost"
    elif computer_score > 21:
        return "Computer went over, You won"
    elif player_score > computer_score:
        return "You won"
    else:
        return "You lost"

def check_ace(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return "Blackjack"
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
player_sum = check_ace(player_cards)
computer_sum = check_ace(dealer_cards)

while input('Do you want to play? ') == "y":
    while game is True:
        print(f'Your cards are: {player_cards}, total of {player_sum}')
        print(f'Computer first card is: {dealer_cards[0]}')
        if player_sum == "Blackjack" or computer_sum =="Blackjack":
            game = False
            end = check_victory(player_sum, computer_sum)
        elif player_sum < 21:
            extra_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if extra_card == "y":
                chosen_card = rd.choice(cards)
                player_cards.append(chosen_card)
                player_sum = check_ace(player_cards)
            else:
                while computer_sum < 17:
                    chosen_card = rd.choice(cards)
                    dealer_cards.append(chosen_card)
                    computer_sum = check_ace(dealer_cards)
                game = False
                end = check_victory(player_sum, computer_sum)
        else:
            game = False
            end = check_victory(player_sum, computer_sum)
    # end = check_victory(player_sum, computer_sum)
    print(end)
    print(f'Your cards are: {player_cards}, total of {player_sum}')
    print(f'Computer cards are: {dealer_cards}, total of {computer_sum}')
