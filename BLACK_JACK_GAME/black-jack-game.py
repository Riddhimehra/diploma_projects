import random

def card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calc_handvalue(hand):
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def blackjack():
    player_hand = [card(), card()]
    comp_hand = [card(), card()]

    print("Your hand:", player_hand,
          "and present score:", calc_handvalue(player_hand))
    print("Computer's up card:", comp_hand[0])
    print()

    while True:
        choice = input("Do you want to 'hit' or 'stand'? ")

        if choice == 'hit':
            player_hand.append(card())

            print("Your hand:", player_hand,
                  "and total score:", calc_handvalue(player_hand))

            if calc_handvalue(player_hand) > 21:
                print("You busted, computer wins!")
                return

        elif choice == 'stand':
            break

        else:
            print("Please enter 'hit' or 'stand'.")

    while calc_handvalue(comp_hand) < 17:
        comp_hand.append(card())

    print()
    print("Your final hand:", player_hand,
          "and final score:", calc_handvalue(player_hand))
    print("Computer's final hand:", comp_hand,
          "and final score:", calc_handvalue(comp_hand))
    print()

    if calc_handvalue(comp_hand) > 21:
        print("Computer busted, you win!")
    elif calc_handvalue(player_hand) > 21:
        print("You busted, computer wins!")
    elif calc_handvalue(player_hand) > calc_handvalue(comp_hand):
        print("You win!")
    elif calc_handvalue(player_hand) < calc_handvalue(comp_hand):
        print("Computer wins!")
    else:
        print("It's a draw!")


blackjack()