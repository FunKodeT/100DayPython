#################################################################
#================================================================
# BLACKJACK PROGRAM
#----------------------------------------------------------------

import random
from TextArt import logo
import os

def clean_terminal_window():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system('clear')
    
def deal_card():
    """ 
        Returns a random card from the assigned deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
        Take a list of cards and return the score calculated from the cards.

            Special Rule Functions:

                1) Check for a blackjack ( a hand with only 2 cards: ace + 10 ) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

                2) Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return 'Losers! Both the Computer and you went over 21!'
    elif user_score == computer_score:
        return 'Draw! Computer and you had the same score!'
    elif computer_score == 0:
        return 'Loser! Computer won with a Blackjack!'
    elif computer_score == 0:
        return 'Winner! You won with a Blackjack!'
    elif user_score > 21:
        return 'Loser! You went over 21!'
    elif computer_score > 21:
        return 'Winner! Computer went over 21!'
    elif user_score > computer_score:
        return 'Winner! You scored more than Computer!'
    else:
        return 'Loser! You scored less than Computer!'

def play_blackjack():
    print(logo)

    user_hand = []
    computer_hand = []
    is_game_over = False

    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not is_game_over:
        
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)

        print(f" Your cards: { user_hand }\n    Score: { user_score } ")
        print(f" Computer's First Played Card:\n    { computer_hand[0] }")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input( "Type 'y' to get another card, type 'n' to pass your turn: " )
            if user_deal == 'y':
                user_hand.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Your final hand was: {user_hand}\n    Your final score was: {user_score}")
    print(f"The Computer's final hand was: {computer_hand}\n    It's final score was: {computer_score}")
    print('Result:', compare(user_score, computer_score))

while input("Do you want to play some Blackjack? Type 'y' for yes, 'n' for no: ") == 'y':
    clean_terminal_window()
    play_blackjack()

#----------------------------------------------------------------
#================================================================
#################################################################
#================================================================
#----------------------------------------------------------------
PROGRAM0_V17 = {
#================================================================

# import random
# from TextArt import logo
# import os

# def clean_terminal_window():
#     if os.name =='nt':
#         os.system('cls')
#     else:
#         os.system('clear')
    
# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     """
#         Take a list of cards and return the score calculated from the cards.

#             Special Rule Functions:

#                 1) Check for a blackjack ( a hand with only 2 cards: ace + 10 ) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#                 2) Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
#     """
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# def compare(user_score, computer_score):
#     if user_score > 21 and computer_score > 21:
#         return 'Losers! Both the Computer and you went over 21!'
#     elif user_score == computer_score:
#         return 'Draw! Computer and you had the same score!'
#     elif computer_score == 0:
#         return 'Loser! Computer won with a Blackjack!'
#     elif computer_score == 0:
#         return 'Winner! You won with a Blackjack!'
#     elif user_score > 21:
#         return 'Loser! You went over 21!'
#     elif computer_score > 21:
#         return 'Winner! Computer went over 21!'
#     elif user_score > computer_score:
#         return 'Winner! You scored more than Computer!'
#     else:
#         return 'Loser! You scored less than Computer!'

# def play_blackjack():
#     print(logo)

#     user_hand = []
#     computer_hand = []
#     is_game_over = False

#     for _ in range(2):
#         user_hand.append(deal_card())
#         computer_hand.append(deal_card())

#     while not is_game_over:
        
#         user_score = calculate_score(user_hand)
#         computer_score = calculate_score(computer_hand)

#         print(f" Your cards: { user_hand }\n    Score: { user_score } ")
#         print(f" Computer's First Played Card:\n    { computer_hand[0] }")

#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_deal = input( "Type 'y' to get another card, type 'n' to pass your turn: " )
#             if user_deal == 'y':
#                 user_hand.append(deal_card())
#             else:
#                 is_game_over = True

#     while computer_score != 0 and computer_score < 17:
#         computer_hand.append(deal_card())
#         computer_score = calculate_score(computer_hand)

#     print(f"Your final hand was: {user_hand}\n    Your final score was: {user_score}")
#     print(f"The Computer's final hand was: {computer_hand}\n    It's final score was: {computer_score}")
#     print('Result:', compare(user_score, computer_score))

# while input("Do you want to play some Blackjack? Type 'y' for yes, 'n' for no: ") == 'y':
#     clean_terminal_window()
#     play_blackjack()

# # Do you want to play some Blackjack? Type 'y' for yes, 'n' for no: y; *ART*; Your cards: [<>, <>]; Score: <>; Computer's First Played Card:; <>; Type 'y' to get another card, type 'n' to pass your turn: n; Your final hand was: [<>, <>]; Your final score was: <>; The Computer's final hand was: [<>, <>]; It's final score was: <>; Result: <Conditional Result>; Do you want to play some Blackjack? Type 'y' for yes, 'n' for no: n;

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V16 = {
#================================================================

# import random
# from TextArt import logo

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     """
#         Take a list of cards and return the score calculated from the cards.

#             Special Rule Functions:

#                 1) Check for a blackjack ( a hand with only 2 cards: ace + 10 ) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#                 2) Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
#     """
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# def compare(user_score, computer_score):
#     if user_score == computer_score:
#         return 'Draw! Computer and you had the same score!'
#     elif computer_score == 0:
#         return 'Loser! Computer won with a Blackjack!'
#     elif computer_score == 0:
#         return 'Winner! You won with a Blackjack!'
#     elif user_score > 21:
#         return 'Loser! You went over 21!'
#     elif computer_score > 21:
#         return 'Winner! Computer went over 21!'
#     elif user_score > computer_score:
#         return 'Winner! You scored more than Computer!'
#     else:
#         'Loser! You scored less than Computer!'

# def play_blackjack():
#     print(logo)

#     user_hand = []
#     computer_hand = []
#     is_game_over = False

#     for _ in range(2):
#         user_hand.append(deal_card())
#         computer_hand.append(deal_card())

#     while not is_game_over:
        
#         user_score = calculate_score(user_hand)
#         computer_score = calculate_score(computer_hand)

#         print(f" Your cards: { user_hand }\n    Score: { user_score } ")
#         print(f" Computer's First Played Card:\n    { computer_hand[0] }")

#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_deal = input( "Type 'y' to get another card, type 'n' to pass your turn: " )
#             if user_deal == 'y':
#                 user_hand.append(deal_card())
#             else:
#                 is_game_over = True

#     while computer_score != 0 and computer_score < 17:
#         computer_hand.append(deal_card())
#         computer_score = calculate_score(computer_hand)

#     print('Result:', compare(user_score, computer_score))

# while input("Do you want to play some Blackjack? Type 'y' for yes, 'n' for no: ") == 'y':
#     play_blackjack()

# # ERROR: Your cards: [<>, <>]; Score: <>; Computer's First Played Card: <>; Type 'y' to get another card, type 'n' to pass your turn: n; Result: None;

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V15 = {
#================================================================

# import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     """
#         Take a list of cards and return the score calculated from the cards.

#             Special Rule Functions:

#                 1) Check for a blackjack ( a hand with only 2 cards: ace + 10 ) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#                 2) Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
#     """
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# def compare(user_score, computer_score):
#     if user_score == computer_score:
#         return 'Draw! Computer and you had the same score!'
#     elif computer_score == 0:
#         return 'Loser! Computer won with a Blackjack!'
#     elif computer_score == 0:
#         return 'Winner! You won with a Blackjack!'
#     elif user_score > 21:
#         return 'Loser! You went over 21!'
#     elif computer_score > 21:
#         return 'Winner! Computer went over 21!'
#     elif user_score > computer_score:
#         return 'Winner! You scored more than Computer!'
#     else:
#         'Loser! You scored less than Computer!'

# user_hand = []
# computer_hand = []
# is_game_over = False

# for _ in range(2):
#     user_hand.append(deal_card())
#     computer_hand.append(deal_card())

# while not is_game_over:
    
#     user_score = calculate_score(user_hand)
#     computer_score = calculate_score(computer_hand)

#     print(f" Your cards: { user_hand }\n    Score: {user_score} ")
#     print(f" Computer's First Played Card:\n    {computer_hand[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#         is_game_over = True
#     else:
#         user_deal = input(" Type 'y' to get another card, type 'n' to pass your turn: ")
#         if user_deal == 'y':
#             user_hand.append(deal_card())
#         else:
#             is_game_over = True

# while computer_score != 0 and computer_score < 17:
#     computer_hand.append(deal_card())
#     computer_score = calculate_score(computer_hand)

# print('Result:', compare(user_score, computer_score))

# # ERROR: Your cards: [<>, <>]; Score: <>; Computer's First Played Card: <>; Type 'y' to get another card, type 'n' to pass your turn: n; Result: None;

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V14 = {
#================================================================

# import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     """
#         Take a list of cards and return the score calculated from the cards.

#             Special Rule Functions:

#                 1) Check for a blackjack ( a hand with only 2 cards: ace + 10 ) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#                 2) Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
#     """
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# def compare(user_score, computer_score):
#     if user_score == computer_score:
#         return 'Draw! Computer and you had the same score!'
#     elif computer_score == 0:
#         return 'Loser! Computer won with a Blackjack!'
#     elif computer_score == 0:
#         return 'Winner! You won with a Blackjack!'
#     elif user_score > 21:
#         return 'Loser! You went over 21!'
#     elif computer_score > 21:
#         return 'Winner! Computer went over 21!'
#     elif user_score > computer_score:
#         return 'Winner! You scored more than Computer!'
#     else:
#         'Loser! You scored less than Computer!'

# user_hand = []
# computer_hand = []
# is_game_over = False

# for _ in range(2):
#     user_hand.append(deal_card())
#     computer_hand.append(deal_card())

# while not is_game_over:
    
#     user_score = calculate_score(user_hand)
#     computer_score = calculate_score(computer_hand)

#     print(f" Your cards: { user_hand }\n    Score: {user_score} ")
#     print(f" Computer's First Played Card:\n    {computer_hand[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#         is_game_over = True
#     else:
#         user_deal = input(" Type 'y' to get another card, type 'n' to pass your turn: ")
#         if user_deal == 'y' or 'Y':
#             user_hand.append(deal_card())
#         elif user_deal == 'n' or 'N':
#             is_game_over = True
#         else:
#             is_game_over = True

# while computer_score != 0 and computer_score < 17:
#     computer_hand.append(deal_card())
#     computer_score = calculate_score(computer_hand)

# print(compare(user_score, computer_score))

# # ERROR: 'n' input adds cards to user hand

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V13 = {
#================================================================

# import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     """
#         Take a list of cards and return the score calculated from the cards.

#             Special Rule Functions:

#                 1) Check for a blackjack ( a hand with only 2 cards: ace + 10 ) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#                 2) Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
#     """
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# def compare(user_score, computer_score):
#     if user_score == computer_score:
#         return 'Draw! Computer and you had the same score!'
#     elif computer_score == 0:
#         return 'Loser! Computer won with a Blackjack!'
#     elif user_score > 21:
#         return 'Loser! You went over 21!'
#     elif computer_score > 21:
#         return 'Winner! Computer went over 21!'
#     elif user_score > computer_score:
#         return 'Winner! You scored more than Computer!'
#     else:
#         'Loser! You scored less than Computer!'

# user_hand = []
# computer_hand = []
# is_game_over = False

# for _ in range(2):
#     user_hand.append(deal_card())
#     computer_hand.append(deal_card())

# while not is_game_over:
    
#     user_score = calculate_score(user_hand)
#     computer_score = calculate_score(computer_hand)

#     print(f" Your cards: { user_hand }\n    Score: {user_score} ")
#     print(f" Computer's First Played Card:\n    {computer_hand[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#         is_game_over = True
#     else:
#         user_deal = input(" Type 'y' to get another card, type 'n' to pass your turn:")
#         if user_deal == 'y' or 'Y':
#             user_hand.append(deal_card())
#         else:
#             is_game_over = True

# while computer_score != 0 and computer_score < 17:
#     computer_hand.append(deal_card())
#     computer_score = calculate_score(computer_hand)

# # Your cards: [<#>, <#>]; Score <Sum Total>; Computer's First Played Card: <#>; Type 'y' to get another card, type 'n' to pass your turn:y; Your Cards: [<#>, <#>, <#>]; Score: <Sum Total>; Computer's First Played Card:; <#>;

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V12 = {
#================================================================

# import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     """
#         Take a list of cards and return the score calculated from the cards.

#             Special Rule Functions:

#                 1) Check for a blackjack ( a hand with only 2 cards: ace + 10 ) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#                 2) Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
#     """
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# user_hand = []
# computer_hand = []
# is_game_over = False

# for _ in range(2):
#     user_hand.append(deal_card())
#     computer_hand.append(deal_card())

# while not is_game_over:
    
#     user_score = calculate_score(user_hand)
#     computer_score = calculate_score(computer_hand)

#     print(f" Your cards: { user_hand }\n    Score: {user_score} ")
#     print(f" Computer's First Played Card:\n    {computer_hand[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#         is_game_over = True
#     else:
#         user_deal = input(" Type 'y' to get another card, type 'n' to pass your turn:")
#         if user_deal == 'y':
#             user_hand.append(deal_card())
#         else:
#             is_game_over = True

# while computer_score != 0 and computer_score < 17:
#     computer_hand.append(deal_card())
#     computer_score = calculate_score(computer_hand)

# # Your cards: [<#>, <#>]; Score <Sum Total>; Computer's First Played Card: <#>; Type 'y' to get another card, type 'n' to pass your turn:y; Your Cards: [<#>, <#>, <#>]; Score: <Sum Total>; Computer's First Played Card:; <#>;

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V11 = {
#================================================================

# import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     """
#         Take a list of cards and return the score calculated from the cards.

#             Special Rule Functions:

#                 1) Check for a blackjack ( a hand with only 2 cards: ace + 10 ) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#                 2) Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
#     """
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# user_hand = []
# computer_hand = []
# is_game_over = False

# for _ in range(2):
#     user_hand.append(deal_card())
#     computer_hand.append(deal_card())

# while not is_game_over:
    
#     user_score = calculate_score(user_hand)
#     computer_score = calculate_score(computer_hand)

#     print(f" Your cards: { user_hand }\n    Score: {user_score} ")
#     print(f" Computer's First Played Card:\n    {computer_hand[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#         is_game_over = True
#     else:
#         input(" Type 'y' to get another card, type 'n' to pass your turn:")
#         if user_deal == 'y':
#             user_hand.append(deal_card())
#         else:
#             is_game_over = True

# # Your cards: [<#>, <#>]; Score <Sum Total>; Computer's First Played Card: <#>; Type 'y' to get another card, type 'n' to pass your turn:y; ERROR

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V10 = {
#================================================================

# import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     """
#         Take a list of cards and return the score calculated from the cards.

#             Special Rule Functions:

#                 1) Check for a blackjack ( a hand with only 2 cards: ace + 10 ) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#                 2) Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
#     """
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# user_hand = []
# computer_hand = []
# is_game_over = False

# for _ in range(2):
#     user_hand.append(deal_card())
#     computer_hand.append(deal_card())

# user_score = calculate_score(user_hand)
# computer_score = calculate_score(computer_hand)

# print(f" Your cards: { user_hand }\n    Score: {user_score} ")
# print(f" Computer's First Played Card:\n    {computer_hand[0]}")

# if user_score == 0 or computer_score == 0 or user_score > 21:
#     is_game_over = True
# else:
#     input(" Type 'y' to get another card, type 'n' to pass your turn:")
#     if user_deal == 'y':
#         user_hand.append(deal_card())
#     else:
#         is_game_over = True

# # 

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V9 = {
#================================================================

# import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     """
#         Take a list of cards and return the score calculated from the cards.

#             Special Rule Functions:

#                 1) Check for a blackjack ( a hand with only 2 cards: ace + 10 ) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#                 2) Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
#     """
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# user_hand = []
# computer_hand = []
# is_game_over = False

# for _ in range(2):
#     user_hand.append(deal_card())
#     computer_hand.append(deal_card())

# user_score = calculate_score(user_hand)
# computer_score = calculate_score(computer_hand)

# print(f" Your cards: { user_hand }, Score: {user_score} ")
# print(f" Computer's First Played Card: {computer_hand[0]}")

# if user_score == 0 or computer_score == 0 or user_score > 21:
#     is_game_over = True

# # Your cards: [<#>, <#>], Score: <Sum Total>; Computer's First Played Card: <First Card>;

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V8 = {
#================================================================

# import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     """
#         Take a list of cards and return the score calculated from the cards.

#             Special Rule Functions:

#                 1) Check for a blackjack ( a hand with only 2 cards: ace + 10 ) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#                 2) Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
#     """
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# user_hand = []
# computer_hand = []
# is_game_over = False

# for _ in range(2):
#     user_hand.append(deal_card())
#     computer_hand.append(deal_card())

# user_score: calculate_score(user_hand)
# computer_score: calculate_score(computer_hand)

# print(f" Your cards: { user_hand }, Score: {user_score} ")
# print(f" Computer's First Played Card: {computer_hand[0]}")

# if user_score == 0 or computer_score == 0 or user_score > 21:
#     is_game_over = True

# # ERROR

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V7 = {
#================================================================

# import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# user_hand = []
# computer_hand = []

# for _ in range(2):
#     user_hand.append(deal_card())
#     computer_hand.append(deal_card())

# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# # 

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V6 = {
#================================================================

# import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# user_hand = []
# computer_hand = []

# for _ in range(2):
#     user_hand.append(deal_card())
#     computer_hand.append(deal_card())

# def calculate_score(cards):
#     if 11 in cards and 10 in cards and len(cards) == 2:
#         return sum(cards)

# # 

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V5 = {
#================================================================

# import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# user_hand = []
# computer_hand = []

# for _ in range(2):
#     user_hand.append(deal_card())
#     computer_hand.append(deal_card())

# def calculate_score(cards):
#     cards = (1, 5, 3, 4)
#     return sum(cards)

# # 

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V4 = {
#================================================================

# import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# user_hand = []
# computer_hand = []

# for _ in range(2):
#     user_hand.append(deal_card())
#     computer_hand.append(deal_card())

# def calculate_score(cards):
#     return sum(cards)

# # 

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V3 = {
#================================================================

# import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# user_hand = []
# computer_hand = []

# for _ in range(2):
#     new_card = [deal_card()]
#     user_hand.extend(new_card)

# # 

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V1 = {
#================================================================

#     import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# user_hand = []
# computer_hand = []

# for _ in range(2):
#     new_card = deal_card()
#     user_hand += new_card

# # ERROR

#================================================================
}
#----------------------------------------------------------------
PROGRAM0_V0 = {
#================================================================

#     import random

# def deal_card():
#     """ 
#         Returns a random card from the assigned deck.
#     """
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# user_hand = []
# computer_hand = []

# for _ in range(2):
#     new_card = deal_card()
#     user_hand.append(new_card)

# # 

#================================================================
}
#----------------------------------------------------------------
#================================================================
#################################################################