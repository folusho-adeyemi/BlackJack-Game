from random import randint

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
def print_card_name(card_rank):
  if card_rank == 1:
    card_name = 'Ace'
  elif card_rank == 11:
    card_name = 'Jack'
  elif card_rank == 12:
    card_name = 'Queen'
  elif card_rank == 13:
    card_name = 'King'
  else:
    card_name = card_rank

  if card_rank == 8 or card_rank == 1:
    print('Drew an ' + str(card_name))
  elif card_rank < 1 or card_rank > 13:
    print('BAD CARD')
  else:
    print('Drew a ' + str(card_name))

# Draws a new random card, prints its name, and returns its value.
# 
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
def draw_card():
  card_rank = randint(1, 13)
  print_card_name(card_rank)

  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    card_value = 10
  elif card_rank == 1:
    card_value = 11
  else:
    card_value = card_rank

  return card_value

# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
# 
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
def print_header(message):
  print('-----------')
  print(message)
  print('-----------')

# Prints turn header and draws a starting hand, which is two cards.
# 
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
  print_header(name.upper() + "'S TURN")
  return draw_card() + draw_card()

# Prints the hand total and status at the end of a player's turn.
# 
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none
def print_end_turn_status(hand_value):
  print('Final hand: ' + str(hand_value) + '.')
  if hand_value == 21:
    print('BLACKJACK!')
  elif hand_value > 21:
    print('BUST.')

# Prints the end game banner and the winner based on the final hands.
# 
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
def eachuser(sub_score):
  for i in range(len(sub_score)):
    if sub_score[i][1] != 0:
      #print(sub_score)
      player_value = draw_starting_hand(sub_score[i][0])
      should_hit = 'y'
      while player_value < 21:
        should_hit = input("You have {}. Hit (y/n)? ".format(player_value))
        if should_hit == 'n':
          break
        elif should_hit != 'y':
          print("Sorry I didn't get that.")
        else:
          player_value = player_value + draw_card()
      sub_score[i][2] = player_value 
      print_end_turn_status(player_value)
  return sub_score

#Funtion to craete the 2d-matrix that stores the numbers of users names, score and current plays
def players(num_of_players):
  sub_score = []
  for i in range(1,num_of_players+1):
    name = input("What is players "+str(i)+"'s name? ")
    sub_score.append([name, 3,0]) 
  return sub_score
#   none


# Calculate the current game status
def print_end_game_status(sub_score, dealer_hand):
  print_header('GAME RESULT')
  score = sub_score.copy()
  for i in range(len(sub_score)):
    if sub_score[i][1] > 0:
      if sub_score[i][2] <= 21 and (sub_score[i][2] > dealer_hand or dealer_hand > 21):
        sub_score[i][1] = sub_score[i][1] +1
        print(sub_score[i][0]+' wins! Score: '+ str(sub_score[i][1]))
      elif sub_score[i][2] > 21 or (dealer_hand <= 21 and dealer_hand > sub_score[i][2]):
        sub_score[i][1] = sub_score[i][1] -1
        print(sub_score[i][0]+' loses! Score: '+ str(sub_score[i][1]))
        if sub_score[i][1] == 0:
          print(sub_score[i][0] + " eliminated!")
          sub_score[i][1] = 0
      else:
        print(sub_score[i][0]+' pushes! Score: '+ str(sub_score[i][1]))


# Function for dealer plays
def dealer():
  dealer_hand = draw_starting_hand("DEALER")
  while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand = dealer_hand + draw_card()
  print_end_turn_status(dealer_hand)
  return dealer_hand