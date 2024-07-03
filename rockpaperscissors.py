import random

wins = 0
loses = 0
draws = 0

while True :
    rock = 'Rock'
    paper = 'Paper'
    scissors = 'Scissors'

    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
      player_move = paper
    elif player_move == "s":
       player_move = scissors
    else:
      print("Invalid input. Try again...")
      break

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
       computer_move = paper
    else:
       computer_move = scissors

    print ("The computer chose ", computer_move, ".")

    if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or (player_move == scissors and computer_move == paper):
       print("You win!")
       wins = wins + 1
    elif player_move == computer_move:
       print("Draw!")
       draws = draws + 1
    else:
      print("You lose!")
      loses = loses + 1
    
    play = input ("Type [yes] to Play Again or [no] to quit: ")
    if play == "no":
       print ("Thanks for playing!")
       print ("Results : draws = ", draws, " wins = ", wins, " loses = ", loses, ".")
       break
    elif play == "yes":
        a = 1
    else:
        print("Invalid input. Try again...")
        break