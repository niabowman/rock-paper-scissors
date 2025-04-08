import sys
import random

print("")
playerChoice = input('Enter... \n1 for rock, \n2 for paper, or \n3 for scissors: \n\n')

player = int(playerChoice)


if player < 1 or player > 3: 
    sys.exit("You must enter 1, 2, or 3.")

compChoice = random.choice("123")

comp = int(compChoice)

print("")
print("You chose: " + playerChoice + ".")
print("Python chose: " + compChoice + ".")
print("")

if player == 1 and comp == 3:
    print("You win! \n")
elif player == 2 and comp == 1:
    print("You win! \n")
elif player == 3 and comp == 2:
    print("You win! \n")

elif player == 1 and comp == 2:
    print("You lost!\n")
elif player == 2 and comp == 3:
    print("You lost!\n")
elif player == 3 and comp == 1:
    print("You lost!\n")

elif player == 3 and comp == 3:
    print("It's a tie! \n")
elif player == 2 and comp == 2:
    print("It's a tie! \n")
elif player == 1 and comp == 1:
    print("It's a tie! \n")