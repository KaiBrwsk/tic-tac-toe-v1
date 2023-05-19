import random
from os import system, name
import time

game_token = []

USER_TOKEN = "X"
COMPUTER_TOKEN = "O"
rounds = 0
running = True


def place_computer_token():
    computer_row = random.randint(0, 2)
    computer_column = random.randint(0, 2)

    if check_free(computer_row, computer_column):
        game_token[computer_row][computer_column] = COMPUTER_TOKEN
    else:
        place_computer_token()


def check_winner(token):
    # Check rows
    for row in range(len(game_token)):
        if game_token[row][0] == game_token[row][1] == game_token[row][2] == token:
            return True

    # Check columns
    for column in range(len(game_token)):
        if game_token[0][column] == game_token[1][column] == game_token[2][column] == token:
            return True

    # Check diagonal top left to bottom right
    if game_token[0][0] == game_token[1][1] == game_token[2][2] == token:
        return True

    # Check diagonal bottom left to top right
    if game_token[0][2] == game_token[1][1] == game_token[2][0] == token:
        return True

    # No winner
    return False


def check_free(row, column):
    if row >= 0 and column >= 0:
        try:
            if game_token[row][column] == " ":
                return True
        except IndexError:
            return False
    else:
        return False


def game():
    global rounds

    # Place users token
    if rounds < 9:
        # Ask user for position of token
        user_row = int(input("In which row do you want to place your token? (1/2/3): ")) - 1
        user_column = int(input("In which column do you want to place your token? (1/2/3): ")) - 1

        # Check if position is free
        if check_free(user_row, user_column):
            game_token[user_row][user_column] = USER_TOKEN
            rounds += 1
        else:
            print("Sorry, this is not possible. Please choose another location.\n")
            game()

        # Show game board to user
        print("You have made your choice: ")
        show_game_board()
        print("Rounds = " + str(rounds))

        # Check if user is winner
        if check_winner(USER_TOKEN):
            print("You win.")
            return
    else:
        print("No winner.")
        return

    # Place computers token
    if rounds < 9:
        print("The computer is placing a token. Please wait a moment.")
        time.sleep(2)
        place_computer_token()
        rounds += 1

        # Show game board to user
        print("The computer has made a choice: ")
        show_game_board()
        print("Rounds = " + str(rounds))

        # Check if computer is winner
        if check_winner(COMPUTER_TOKEN):
            print("The computer wins.")
            return
        else:
            # Restart game loop
            game()
    else:
        print("No winner.")
        return


def clear():
    # For windows
    if name == 'nt':
        _ = system('cls')

    # For mac and linux
    else:
        _ = system('clear')


def show_game_board():
    clear()
    game_board = (f"{game_token[0][0]} | {game_token[0][1]} | {game_token[0][2]}\n"
                  "---------\n"
                  f"{game_token[1][0]} | {game_token[1][1]} | {game_token[1][2]}\n"
                  "---------\n"
                  f"{game_token[2][0]} | {game_token[2][1]} | {game_token[2][2]}\n")
    print(game_board)
    return


while running:
    user_play_again = input("Would you like to play? (yes/no): ").lower()
    if user_play_again == "yes":
        game_token = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        show_game_board()
        rounds = 0
        game()
    else:
        clear()
        print("See you next time.")
        running = False

