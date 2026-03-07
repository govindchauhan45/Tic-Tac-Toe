import random
import time
import sys

# Typing animation for messages
def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Display the board
def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

# Check for win
def check_win(board, player):
    win_cond = [(0,1,2), (3,4,5), (6,7,8), # rows
                (0,3,6), (1,4,7), (2,5,8), # columns
                (0,4,8), (2,4,6)]          # diagonals
    return any(board[a]==board[b]==board[c]==player for a,b,c in win_cond)

# Get computer move (random)
def computer_move(board):
    available = [i for i, x in enumerate(board) if x == " "]
    return random.choice(available)

# Main game function
def tic_tac_toe():
    board = [" "] * 9
    slow_print("Welcome to Terminal Tic-Tac-Toe!")
    time.sleep(0.5)
    
    mode = input("Choose mode: 1) Player vs Player  2) Player vs Computer: ")
    player_turn = "X"
    
    while True:
        display_board(board)
        if mode == "2" and player_turn == "O":
            slow_print("Computer is thinking...")
            time.sleep(1)
            move = computer_move(board)
            board[move] = "O"
            slow_print(f"Computer chose position {move+1}")
        else:
            while True:
                try:
                    move = int(input(f"Player {player_turn}, enter your move (1-9): ")) - 1
                    if board[move] == " ":
                        board[move] = player_turn
                        break
                    else:
                        slow_print("Position taken! Choose another.")
                except (ValueError, IndexError):
                    slow_print("Invalid input! Enter a number from 1 to 9.")
        
        # Check win
        if check_win(board, player_turn):
            display_board(board)
            slow_print(f"Player {player_turn} wins! 🎉")
            break
        
        # Check tie
        if " " not in board:
            display_board(board)
            slow_print("It's a tie! 😐")
            break
        
        # Switch player
        player_turn = "O" if player_turn == "X" else "X"

    slow_print("Game Over. Thanks for playing!")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
