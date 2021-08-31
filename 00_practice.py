### team 7 rock-paper-scissors game ###

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer_selects = 0
winning_list = []
# game images list
game_images = [rock, paper, scissors]
# initiates arrays, user_selects, and computer_selects
# start a game
def start_game():
# Gets first input and adds user input to list
#    user_selects = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
    if user_selects == 0:
        print("Rock")
    elif user_selects == 1:
        print("Paper")
    elif user_selects == 2:
        print("Scissors")
    elif user_selects >= 3 or user_selects <0:
        print("Invalid number")
    if user_selects >= 3 or user_selects < 0:
        print("You typed an invalid number, you lose! GAME OVER")

# function win_or_lose determine winning throw, and appends winning_list
def win_or_lose (user_selects, computer_selects):
    # Rock user select arguments and outcomes
    if user_selects == 0 and computer_selects == 0:
        print("It's a draw")
        winning_list.append(1)
    elif user_selects == 0 and computer_selects == 1:
        print("You Lose")
        winning_list.append(2)
    elif user_selects == 0 and computer_selects == 2:
            print("You Win!")
            winning_list.append(1)
# Paper user select arguments and outcomes
    elif user_selects == 1 and computer_selects == 0:
        print("You Win!")
        winning_list.append(2)
    elif user_selects == 1 and computer_selects == 1:
        print("It's a draw")
        winning_list.append(2)
    elif user_selects == 1 and computer_selects == 2:
        print("You Lose")
        winning_list.append(0)
# Scissors user select arguments and outcomes
    elif user_selects == 2 and computer_selects == 0:
        print("You Lose")
        winning_list.append(1)
    elif user_selects == 2 and computer_selects == 1:
        print("You Win!")
        winning_list.append(0)
    elif user_selects == 2 and computer_selects == 2:
        print("It's a draw")
        winning_list.append(0)

# function computer_choice is the AI for computer throw
# computer selects the throw that would have beaten the winner
# of the previous game
def computer_choice(user_selects, computer_selects):
# Rock computer input change
    if user_selects == 0 and computer_selects == 0:
        return 1
    elif user_selects == 0 and computer_selects == 1:
        return 2
    elif user_selects == 0 and computer_selects == 2:
        return 1
# Paper computer input change
    elif user_selects == 1 and computer_selects == 0:
        return 2
    elif user_selects == 1 and computer_selects == 1:
        return 2
    elif user_selects == 1 and computer_selects == 2:
        return 0
# Scissors computer input change
    elif user_selects == 2 and computer_selects == 0:
        return 1
    elif user_selects == 2 and computer_selects == 1:
        return 0
    elif user_selects == 2 and computer_selects == 2:
        return 0

# display results of the game
def display_results():
    # prints out pictures for user and computer then calls function to run game
    print("User selects:")
    print(game_images[user_selects])
    print("Computer selects:")
    print(game_images[0])


# determine if user wants to play a second game
# problem here doesn't go past game over... may need to pass something into new_game()
   # def new_game():
   # input("Do you want to play again? \nType Y for YES or N for NO.\n").lower()
   #  if input() != "y" or input() != "yes":
   #         print("Game Over")
   #     start_game()
#user_selects = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

while True:
    # user input to begin game
    user_selects = int(input("Lets play Rock, Paper, Scissors. \nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    # play_again = True
    start_game()
    display_results()
    win_or_lose(user_selects, computer_selects)
    computer_selects = computer_choice(user_selects, computer_selects)

# while true continue to ask user to play another game
# problem here - continues to use the first throw by user
    play_again = input("Would you like to play another round? Yes or No: \n").lower()
    if play_again != "y" and play_again != "yes":
        break
print("Game over")
