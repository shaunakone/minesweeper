import numpy as np
import random

def create_board():
    board = np.full((10,10), " ")
    return board

def check_location(board, col, row):
    
    col_choice = int(input("which col would you like to play in?")) 
    row_choice = int(input("which col would you like to play in?")) 


    board[row_choice][col_choice] = "X"

    return (row_choice, col_choice)



def bombs(board, bombs = 10):
    
    bomb_board = create_board()
    bomb_loc = random.sample(range(10 * 10), bombs)

    for pos in bomb_board:
        row = pos//10
        col = pos%10
        bomb_board[row][col] == "*"
    return bomb_board

def compare(player_move, bomb_board):
    
    player_row, player_col = player_move

    if bomb_board[player_row][player_col] == "*":
        print("GG")
        return True
    else:
        return False







board = print_board()
check_location(board, 0, 0)
print(board)



#def play_game():
    #player = "X"
    #user_input = int(input("Where do you want to place your bomb? (Row, Column)"))

    #while(True):
        #pr






#Create the grid and be able to select where everything is, then check if there is a bomb nearby

