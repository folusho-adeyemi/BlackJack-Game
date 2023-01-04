# Use randint to generate random cards. 
from blackjack_helper import *
num_of_players = int(input("Welcome to Blackjack! How many players? "))
score = players(num_of_players)
values = eachuser(score)
dealer_hand = dealer()

# GAME RESULT
print_end_game_status(score, dealer_hand)
summer = 0
for i in range(len(score)):
  summer+= score[i][1]
while summer != 0:
  play = input("Do you want to play another hand (y/n)? ")
  if play == "y":
    summer = 0
    values = eachuser(score)
    dealer_hand = dealer()
    print_end_game_status(score, dealer_hand)
    for i in range(len(score)):
      summer+= score[i][1]
    #print("I am summer 2 " + str(summer))
  else:
    break
if summer == 0:
  print("All players eliminated!")




