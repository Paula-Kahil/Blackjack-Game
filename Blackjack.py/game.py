#ok so bbalesh b eno traje3li random card mnl deck
import random

def deal_card():

  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)
#badi ekhod list mnl cards w raje3 lscore lma3melo calculation mnl cards
def calculate_score(cards):

  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
     cards.remove(11)
     cards.append(1)
  return sum(cards) 

def compare(user_score,computer_score):
   if user_score==computer_score:
     return "Draw a card"

   elif computer_score==0:
     return "Opponent has Blackjack,lose!"

   elif user_score==0:
     return "Win with a Blackjack!"

   elif user_score>21:
     return "You lose!"

   elif computer_score>21:
     return "You win!"

   elif user_score>computer_score:
     return "You win!"

   else:
     return "You lose!"

def play_game():
  print("Welcome to Blackjack!")

  user_cards=[]
  computer_cards=[]
  is_game_over=False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"You cards: {user_cards}, current score: {user_score}")
    print(f"Computer first card:{computer_cards[0]}")

  #lezem shuf iza fi winner fa ya bikoun 3andi 3 conditions bikoun game over True aw es2al l user iza badon yes7ab war2a ya bys7ab ya lis game over betkoun True

    if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
      user_answer=input("Type 'yes' to get another card or 'no' to pass")
      if user_answer=='yes':
        user_cards.append(deal_card())
      else:
        is_game_over=True

  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)

  print(f"Your final hand:{user_cards},final score: {user_score}")
  print(f"Computer final hand:{computer_cards},final score: {computer_score}")
  print(compare(user_score,computer_score))

while input("Do you want to play a blackjack game?yes or no?")=='yes':
  play_game()