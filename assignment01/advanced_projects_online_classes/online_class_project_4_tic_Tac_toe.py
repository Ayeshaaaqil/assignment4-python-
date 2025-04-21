# Tic-Tac-Toe Python Project
# In this Kylie Ying tutorial, you will learn how to build a tic-tac-toe game with 
# various players in the command line. You will learn how to work with Python's 
# time and math modules as well as get continual practice with nested if statements.

import time
import random

# Board initialize karna
board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---|---|---")
    print("\n")

def check_winner(player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8),  # Rows
                      (0,3,6), (1,4,7), (2,5,8),  # Columns
                      (0,4,8), (2,4,6)]           # Diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

def computer_move():
    available_moves = [i for i in range(9) if board[i] == " "]
    return random.choice(available_moves)

def play_game():
    user = "X"
    computer = "O"
    
    while True:
        print_board()

        # User Move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = user
            else:
                print("Invalid move! Try again.")
                continue
        except (IndexError, ValueError):
            print("Invalid input! Enter a number between 1 and 9.")
            continue

        # Check if user wins
        if check_winner(user):
            print_board()
            print("🎉 Congratulations! You win! 🎉")
            break

        # Check if game is draw
        if is_draw():
            print_board()
            print("It's a draw! 🤝")
            break

        # Computer Move
        time.sleep(1)
        move = computer_move()
        board[move] = computer
        print(f"Computer chose position {move + 1}")

        # Check if computer wins
        if check_winner(computer):
            print_board()
            print("💻 Computer wins! Better luck next time.")
            break

        # Check if game is draw
        if is_draw():
            print_board()
            print("It's a draw! 🤝")
            break

# Run game
play_game()

