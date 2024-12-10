import random

card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
card_suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

card_deck = []

for value in card_values: 
    for suit in card_suits: 
        card_deck.append(str(value) + " of " + str(suit))

def shuffle(deck): 
   random.shuffle(deck)
   return deck

def deal_cards(deck): 
    player_1_hand = [deck.pop(), deck.pop()]
    player_2_hand = [deck.pop(), deck.pop()]
    return player_1_hand, player_2_hand


def flop(deck):
    flop = [deck.pop(), deck.pop(), deck.pop()]
    return flop

def newflip(deck):
    newcard = deck.pop()
    return newcard

def has_flush(cards): 
    suit_counts = {'Spades': 0, 'Clubs': 0, 'Hearts': 0, 'Diamonds': 0 }
    for card in cards: 
        suit = card.split(" of ")[1]
        suit_counts[suit] += 1
    for suit in suit_counts: 
        if suit_counts[suit] >= 5:
            return True
    return False

def has_pair(cards): 
    card_counts = {}
    for card in cards: 
        value = card.split(" of ")[0]
        if value in card_counts: 
            card_counts[value] += 1
        else: 
            card_counts[value] = 1
    for card in card_counts: 
        if card_counts[card] == 2:
            return True
    return False
        
def has_two_pair(cards): 
    card_counts = {}
    for card in cards: 
        value = card.split(" of ")[0]
        if value in card_counts: 
            card_counts[value] += 1
        else: 
            card_counts[value] = 1
    pair_count = 0
    for card in card_counts: 
        if card_counts[card] == 2:
            pair_count += 1 
    if pair_count >= 2:
        return True
        
def three_of_a_kind(cards): 
    card_counts = {}
    for card in cards: 
        value = card.split(" of ")[0]
        if value in card_counts: 
            card_counts[value] += 1
        else: 
            card_counts[value] = 1
    for card in card_counts: 
        if card_counts[card] == 3:
            return True
    return False

def four_of_a_kind(cards):
    card_counts = {}
    for card in cards: 
        value = card.split(" of ")[0]
        if value in card_counts: 
            card_counts[value] += 1
        else: 
            card_counts[value] = 1
    for card in card_counts: 
        if card_counts[card] == 4:
            return True
    return False

def fullhouse(cards): 
    if three_of_a_kind(cards) and has_pair():
        return True 
    return False


def has_straight(cards): 
    card_values_hand = []
    for card in cards:
        value = card.split(" of ")[0]
        card_values_hand.append(card_values.get(value))
    card_values_hand.sort()

    for i in range (3):
        if card_values_hand[i + 1] == card_values_hand[i] + 1 and card_values_hand[i + 2] == card_values_hand[i+1] + 1 and card_values_hand[i + 3] == card_values_hand[i+2] + 1 and card_values_hand[i + 4] == card_values_hand[i+3] + 1:
            return True 
    if 14 in card_values_hand and 2 in card_values_hand and 3 in card_values_hand and 4 in card_values_hand and 5 in card_values_hand: 
        return True 
    return False
    

def straightflush(cards):
    if has_straight(cards) and has_flush(cards):
        return True
    return False

def Royal_flush(cards):
    card_values_hand = []
    for card in cards:
        value = card.split(" of ")[0]
        card_values_hand.append(card_values.get(value))
    card_values_hand.sort()
    if (10 in card_values_hand and 11 in card_values_hand and 12 in card_values_hand and 13 in card_values_hand and 14 in card_values_hand) and has_flush(cards):
        return True
    return False


def handEvaluation(cards):
    if Royal_flush(cards):
        return 10
    elif straightflush(cards):
        return 9
    elif four_of_a_kind(cards):
        return 8
    elif fullhouse(cards):
        return 7
    elif has_flush(cards):
        return 6
    elif has_straight(cards):
        return 5
    elif three_of_a_kind(cards):
        return 4
    elif has_two_pair(cards):
        return 3
    elif has_pair(cards):
        return 2
    else:
        return 1

def high_card(cards):
    valueofcards =[]
    for card in cards:
        value = card.split(" of ")[0]
        realval = card_values[value]
        valueofcards.append(realval)
    highest_val = valueofcards[0]
    for val in valueofcards:
        if val > highest_val:
            highest_val = val
    return highest_val
    
        


    







def player_action(player, chips, bet): 

    print(f"\n{player}'s turn. You have {chips} chips.")
    print(f"The Current bet is {bet} chips.")

    if bet > 0:
        print ("You can't check because there is an active bet.")
        while True: 
            action = input("Choose your action (call/raise/fold)")
            if action == "call":
                call_amount = bet
                chips -= call_amount
                print (f"{player} calls with {call_amount} chips.")
                if call_amount > chips:
                    print("You called more or exactly the amount you have! Going all in")
                    call_amount = chips
                    chips = 0 
                return bet, chips, "call"
            elif action == "raise": 
                raise_amount = int(input("Enter the amount you want to raise: "))
                if raise_amount <= bet:
                    print("Your raise must be greater than the current bet")
                elif raise_amount > chips:
                    print ("You dont have enough chips. Going all-in")
                    raise_amount = chips 
                    chips -= raise_amount
                    print (f"{player} raises bet to {raise_amount}")
                    return raise_amount, chips, "raise"
                else: 
                    chips -= raise_amount
                    print(f"{player} raises to {raise_amount}.")
                    return raise_amount, chips, "raise"
            elif action == "fold":
                print(f"{player} folds")
                return bet, chips, "fold"
            else:
                print ("Invalid action! Choose call, raise or fold!")

    else:
        print ("You can check because there is no active bet.\n")
        action = input("Choose (check/bet)").lower()

        if action == "bet": 
            bet_amount = int(input("\nHow many chips did you want to bet?"))
            if bet_amount > chips: 
                print ("You are betting more chips than you have. Going all in")
                bet_amount = chips
            chips -= bet_amount
            print(f"{player} bets {bet_amount} chips.")
            return bet_amount, chips, "bet"
        elif action == "check": 
            print (f"{player} checks")
            return bet, chips, "check"
        else:
            print("Invalid action! Checking.")
            return bet, chips, "check"

def oneturn(player_1_chips, player_2_chips):
    shuffled_deck = shuffle(card_deck)
    player_1_hand, player_2_hand = deal_cards(shuffled_deck)
    flop_cards = flop(shuffled_deck)
    fourth_card = newflip(shuffled_deck)
    community_cards4 = flop_cards + [fourth_card]
    fifth_card = newflip(shuffled_deck)
    community_cards5 = community_cards4 + [fifth_card]
    current_bet = 0
    pot = 0




    print("\n Poker Round Starts ")
    print(f"\n \n Player 1's Hand: {player_1_hand}")
    print(f"Flop Cards: {flop_cards}")
    current_bet, player_1_chips, action1 = player_action("Player 1", player_1_chips, current_bet)
    pot += current_bet
    print(pot)
    if action1 == "fold":
        print(f"Player 2 wins {pot} chips!")
        player_2_chips += pot
        return player_1_chips, player_2_chips
    print(f"\n \n \nPlayer 2's Hand: {player_2_hand}")
    print(f"Flop Cards: {flop_cards}")
    current_bet, player_2_chips, action2 = player_action("Player 2", player_2_chips, current_bet)
    pot += current_bet
    if action2 == "fold":
        print(f"Player 1 wins {pot} chips!")
        player_1_chips += pot
        return player_1_chips, player_2_chips
    if action2 == "bet" and current_bet > 0:
        print(f"Player 2 raised the bet to {current_bet}")
        current_bet, player_1_chips, action1 = player_action("Player 1", player_1_chips, current_bet)
        pot += current_bet
        print(pot)
        if action1 == "fold": 
            print(f"Player 2 wins{pot} chips!")
            player_2_chips+=pot
            return player_1_chips, player_2_chips
        


    

    
    print(f"\n\nFlipping the next card!: {fourth_card} \nThese are the community cards now: {community_cards4}")
    print(f"\n Player 1's Hand: {player_1_hand}")

    current_bet = 0
    current_bet, player_1_chips, action1 = player_action("Player 1", player_1_chips, current_bet)
    pot += current_bet
    if action1 == "fold":
        print(f"Player 2 wins{pot} chips!")
        player_2_chips += pot
        return player_1_chips, player_2_chips

    print(f"\nPlayer 2's Hand: {player_2_hand}")
    current_bet, player_2_chips, action2 = player_action("Player 2", player_2_chips, current_bet)
    pot += current_bet

    if action2 == "fold":
        print(f"Player 1 wins {pot} chips!")
        player_1_chips += pot
        return player_1_chips, player_2_chips

    if action2 == "bet" and current_bet > 0:
        print(f"Player 2 raised the bet to {current_bet}")
        current_bet, player_1_chips, action1 = player_action("Player 1", player_1_chips, current_bet)
        pot += current_bet
        if action1 == "fold": 
            print(f"Player 2 wins {pot} chips!")
            player_2_chips += pot
            return player_1_chips, player_2_chips

        





    
    print(f"Flipping the next card!: {fifth_card} \nThese are the community cards now: {community_cards5}")
    current_bet = 0
    current_bet, player_1_chips, action1 = player_action("Player 1", player_1_chips, current_bet)
    pot += current_bet
    if action1 == "fold":
        print(f"player 2 wins {pot} chips!")
        player_2_chips += pot
        return player_1_chips, player_2_chips

    current_bet, player_2_chips, action2 = player_action("Player 2", player_2_chips, current_bet)
    pot += current_bet

    if action2 == "fold":
        print(f"Player 1 wins {pot} chips")
        player_1_chips += pot
        return player_1_chips, player_2_chips
    if action2 == "bet" and current_bet > 0:
        print(f"Player 2 raised the bet to {current_bet}")
        current_bet, player_1_chips, action1 = player_action("Player 1", player_1_chips, current_bet)
        pot += current_bet
        if action1 == "fold": 
            print(f"Player 2 wins {pot} chips!")
            player_2_chips += pot
            return player_1_chips, player_2_chips

    community_cards = flop_cards + [fourth_card, fifth_card]
    player_1_whole_hand = player_1_hand + community_cards
    player_2_whole_hand = player_2_hand + community_cards
    p1_score = handEvaluation(player_1_whole_hand)
    p2_score = handEvaluation(player_2_whole_hand)
    if p1_score > p2_score:
        print ("Player 1 Wins")
        player_1_chips += pot
    elif p2_score > p1_score:
        print ("Player 2 wins")
        player_2_chips += pot
    elif p1_score == p2_score:
        high_card_1 = high_card(player_1_whole_hand)
        high_card_2 = high_card(player_2_whole_hand)
        if high_card_1 > high_card_2:
            print("Player 1 wins")
            player_1_chips += pot
        else: 
            print("Player 2 wins")
            player_2_chips += pot 
    else: 
        print("It's a tie! The pot is split.")
        player_1_chips += pot // 2
        player_2_chips += pot // 2
    return player_1_chips, player_2_chips

def play_game():
    buyin = int(input("What would you like the buy-in to be?\n"))
    player_1_chips = buyin
    player_2_chips = buyin

    while True:
        print("\nStarting a new round!")
        player_1_chips, player_2_chips = oneturn(player_1_chips, player_2_chips)
        
        if player_1_chips <= 0:
            print("Player 1 is out of chips! Player 2 wins the game!")
            break
        elif player_2_chips <= 0:
            print("Player 2 is out of chips! Player 1 wins the game!")
            break
        
        continue_game = input("\nDo you want to play another round? (yes/no): ").lower()
        if continue_game != "yes":
            print("Thanks for playing!")
            break

play_game()



    

    


    

            
                

    