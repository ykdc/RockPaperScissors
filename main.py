# Simple game of Rock, Paper, scissors
from random import randint

choice = ["rock", "paper", "scissors"]

# computer chooses random choice 0,1,2
computer = choice[randint(0,2)]
play = "Y"

while play == "Y" or play == "y":
  player = input("Please select, rock, paper, or scissors:  ")
  print("Computer's choice is: ", computer)
  if player == computer:
    print("Tie!")
  elif player == "rock":
    if computer == "paper":
      print("You lose!" , computer, "covers ", player)
    else:
      print("You Win!", player, "crushes ", player)
  elif player == "paper":
    if computer == "scissors":
      print("You lose!" , computer, "cuts ", player)
    else:
      print("You Win!", player, "covers ", player)
  elif player == "scissors":
    if computer == "rock":
      print("You lose!" , computer, "crushes ", player)
    else:
      print("You Win!", player, "cuts ", player)
  else:
    print("You entered an invalid choice.")
  play = input("Would you like to play again? [Y/N]")
  print("\n")
  if play == "Y" or play == "y":
    computer = choice[randint(0,2)]
  else:
    print("Thank you for playing!")

 