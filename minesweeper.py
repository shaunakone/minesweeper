import numpy as np
import random

def create_board():
    board = np.full((11,11), " ")
    return board

def print_board(board):

    print("   1  2  3  4  5  6  7  8  9  10")
    print("  -------------------------------")

    for index, row in enumerate(board):
        print(index, "|", " ".join(row))  
    
    print()  

def check_location(board):
    
    col_choice = int(input("which col would you like to play in?")) 
    row_choice = int(input("which col would you like to play in?")) 


    board[row_choice][col_choice] = "X"

    return (row_choice, col_choice)

def bombs(bombs = 10):
    
    bomb_board = create_board()
    bomb_loc = random.sample(range(10 * 10), bombs)

    for pos in bomb_loc:
        row = pos//10
        col = pos%10
        bomb_board[row][col] = "*"

    for x in bomb_board:
        print(" ".join(x))  

    return bomb_board


def compare(player_move, bomb_board):
    
    player_row, player_col = player_move

    if bomb_board[player_row][player_col] == "*":
        return True
    else:
        return False
    

    #1,2,3,



def play_game():
    player_board = create_board()  
    bomb_board = bombs(10) 


    while True:
        print_board(player_board)  
        
        player_move = check_location(player_board)  

        if compare(player_move, bomb_board):
            print("Game Over")
            print_board(bomb_board)  
            break  


play_game()







#Create the grid and be able to select where everything is, then check if there is a bomb nearby

