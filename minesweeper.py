import numpy as np


def create_board():
    board = np.full((10,10), " ")
    return board

def check_location(board, col, row):
    
    col_choice = int(input("which col would you like to play in?")) 
    row_choice = int(input("which col would you like to play in?")) 


    board[col_choice][row_choice] = "X"



def bombs(board, bombs):
    
    bomb_board = 



board = print_board()
check_location(board, 0, 0)
print(board)



#def play_game():
    #player = "X"
    #user_input = int(input("Where do you want to place your bomb? (Row, Column)"))

    #while(True):
        #pr






#Create the grid and be able to select where everything is, then check if there is a bomb nearby

