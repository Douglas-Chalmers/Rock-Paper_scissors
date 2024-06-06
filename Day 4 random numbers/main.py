import random

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

choice = [rock, paper, scissors]
num_choice = ""
player_win = 0
cpu_win = 0


# Asks player how many rounds to play - 3, 5 or 7
def rounds_to_play():
    global num_choice
    good_to_go = False
    num_of_rounds = (input("How many rounds would you like to play? (Best of 3, 5 or 7): "))
    while not good_to_go:
        check_user_input(num_of_rounds)
        good_to_go = True
        rounds = int(num_choice)
        while good_to_go:
            if rounds < 3:
                num_of_rounds = (input("Please pick (Best of 3, 5 or 7): "))
                good_to_go = False
            elif 3 < rounds < 5:
                num_of_rounds = (input("Please pick (Best of 3, 5 or 7): "))
                good_to_go = False
            elif 5 < rounds < 7:
                num_of_rounds = (input("Please pick (Best of 3, 5 or 7): "))
                good_to_go = False
            elif rounds > 7:
                num_of_rounds = (input("Please pick (Best of 3, 5 or 7): "))
                good_to_go = False
            else:
                return rounds


# checks user input against float, str or null
def check_user_input(something):
    int_check = False
    global num_choice
    while not int_check:
        try:
            val = int(something)
            int_check = True
            num_choice = str(val)
            return int_check
        except ValueError:
            try:
                val = float(something)
                print(f"Input = {val}, is float")
                something = input("Please enter a whole number: ")
                num_choice = something
            except ValueError:
                print("Input is string")
                something = input("Please enter a number value: ")
                num_choice = something


# Asks player to choose rock, paper or scissors
def player_choice():
    global num_choice
    player_selection = (input("What do you choose? (Type 1 for Rock, 2 for Paper, 3 for Scissors) \n"))
    num_choice = player_selection
    while check_user_input(num_choice):
        player_input = int(num_choice) - 1
        while player_input > 2 or player_input < 0:
            player_selection = input("Please pick an option (1 for Rock, 2 for Paper, 3 for Scissors): \n")
            if check_user_input(player_selection):
                player_input = int(num_choice) - 1
        else:
            print(choice[player_input])
            return player_input


# generates a random computer choice
def computer_choice():
    random_num = random.randint(0, 2)
    cpu_selection = random_num
    print(f"Computer chose: {cpu_selection}")
    print(choice[cpu_selection])
    return cpu_selection


# check if player or cpu won the game
def win_lose():
    if player_win > cpu_win:
        print(f"Player wins: {player_win}")
        print(f"Computer wins: {cpu_win}")
        print("You won the game of Rock-Paper-Scissors!")
    elif player_win == cpu_win:
        print(f"Player wins: {player_win}")
        print(f"Computer wins: {cpu_win}")
        print("Looks like it's a draw.")
    else:
        print(f"Player wins: {player_win}")
        print(f"Computer wins: {cpu_win}")
        print("You did not win the game of Rock-Paper-Scissor")


# Asks player if they would like to play again.
def keep_playing():
    global player_win
    global cpu_win
    play_again = input("Would you like to play again? (yes/no) ")
    while play_again.lower() == "yes" or play_again.lower() == "y":
        player_win = 0
        cpu_win = 0
        main_game()
        play_again = "n"
    else:
        print("Thank you for playing!")
        exit()


# Main part of the game, checks if player wins round or cpu
def main_game():
    global player_win
    global cpu_win
    print("Welcome to Doug's Rock-Paper-Scissors game")
    rounds = int(rounds_to_play())
    rounds_played = 0
    while rounds_played < rounds:
        player = player_choice()
        computer = computer_choice()
        if player == 0:
            if computer == 0:
                print("It's a draw\n")
            elif computer == 1:
                print("You lose.\n")
                cpu_win += 1
            else:
                print("You win!\n")
                player_win += 1
        elif player == 1:
            if computer == 0:
                print("You win!\n")
                player_win += 1
            elif computer == 1:
                print("It's a draw\n")
            else:
                print("You lose.\n")
                cpu_win += 1
        else:
            if computer == 0:
                print("You lose.\n")
                cpu_win += 1
            elif computer == 1:
                print("You win!\n")
                player_win += 1
            else:
                print("It's a draw.\n")
        rounds_played += 1
    else:
        win_lose()
        keep_playing()


main_game()
