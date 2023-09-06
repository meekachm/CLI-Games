# cli-games/bnc.py

# import library
from random import randint

# variable for roles
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role using an array
computer = roles[randint(0,2)]
player = False
score = 0

# display a starting message
def get_ready():
    print("Get ready to play Bear, Ninja, Cowboy!")

# function for instructions
def instruct(yes_no):
    if yes_no.lower() == "yes":
        print("Bear, Ninja, Cowboy is an exciting game of strategy and skill! Pit your wit against the computer! Choose a player: Bear, Ninja, or Cowboy. The computer chooses a player. Bear eats Ninja, Ninja defeats Cowboy and cowboy shoots bear.")
    else: 
        return

# function to check input validity
def valid_entry(user_entry):
    user_entry = user_entry.lower()

    if user_entry == "bear" or user_entry == "ninja" or user_entry == "cowboy":
        return True
    else:
        print(f"{user_entry} is not a valid entry. Please try again.")
        return False

# function for the action that the winner takes
def win_action(win):
    win = win.lower()
    
    if win == "bear":
        return("eats")
    elif win == "ninja":
        return("defeats")
    elif win == "cowboy":
        return("shoots")

# function to display win/lose message
def win_lose_script(user):
    global score
    if user == player:
        score += 1
        action = win_action(player)
        print(f"You win! {player} {action} {computer}. Your score is: {score}")
    else:
        score -= 1
        action = win_action(computer)
        print(f"You lose! {computer} {action} {player}. Your score is: {score}")

# function to for tie
def check_win(computer, player):
    global score, win
    computer = computer.lower()
    player = player.lower()
    
    # compare computer and player role
    if computer == player:
        print("DRAW!")
    elif computer == "cowboy":
        if player == "bear":
            win_lose_script(computer)
        else: # computer is cowboy, player is ninja
            win_lose_script(player)
    elif computer == "bear":
        if player == "cowboy":
            win_lose_script(player)
        else: # computer is bear, player is ninja
            win_lose_script(computer)
    elif computer == "ninja":
        if player == "cowboy":
            win_lose_script(computer)
        else: # computer is ninja, player is bear
            win_lose_script(player)

def bear_ninja_cowboy():
    global player, computer
    get_ready()
    instruct(input("Would you like instructions? (yes/no) > "))
    computer = roles[randint(0,2)]

    while player == False:
        # get player input
        player = input("Bear, Ninja, or Cowboy? > ")

        # check if entry valid
        if valid_entry(player) == False:
            player = False
            computer = roles[randint(0,2)]
        else:
            # check for winner
            check_win(computer, player)
            # prompt player to play again 
            play_again = input("Would you like to play again? (yes/no) > ")
            if play_again == 'yes':
                player = False
                computer = roles[randint(0,2)]
            else:
                print("Thank you for playing.")
                break

bear_ninja_cowboy()