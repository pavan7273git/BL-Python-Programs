'''4. Cross Game or Tic-Tac-Toe Game
a. Desc -> Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1
is the Computer and the Player 2 is the user. Player 1 take Random Cell that is
the Column and Row.
b. I/P -> Take User Input for the Cell i.e. Col and Row to Mark the ‘X’
c. Logic -> The User or the Computer can only take the unoccupied cell. The Game
is played till either wins or till draw...
d. O/P -> Print the Col and the Cell after every step.
e. Hint -> The Hints is provided in the Logic. Use Functions for the Logic...'''

import random

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def computer_move(board):
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            print(f"Computer chose: Row {row}, Col {col}")
            break

def user_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column: 0 1 2): ").split())
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Cell already occupied! Choose another.")
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as two numbers between 0 and 2.")

def play_game():
    board = initialize_board()
    print_board(board)
    
    while True:
        user_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
        
        computer_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("Computer wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()