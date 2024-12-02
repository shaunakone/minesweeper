import numpy as np
import random
import time

def create_board():
    board = np.full((11, 11), " ")
    return board

#def powerup(bomb_board):

    #count = 0

    #while count != 10:
        #count += 1
        #continue


    #print("Powerup activated!")
    #print(bomb_board)
    
def print_board(board):
    for index, row in enumerate(board[::-1]):
        print(len(board) - 1 - index, "┃", " ".join(row))
    print("  ━━━━━━━━━━━━━━━━━━━━━━━━")
    print("    " + " ".join(str(i) for i in range(len(board[0]))))

def count_adjacent_bombs(row, col, bomb_board):

    #end_loc = (row+(n*dir[0]), col+(n*dir[1]))

    count = 0
    checks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for r, c in checks:
        new_row = row + r
        new_col = col + c
        if 0 <= new_row < len(bomb_board) and 0 <= new_col < len(bomb_board[0]):
            if bomb_board[new_row][new_col] == "*":
                count += 1
    return count

def check_location(board, bomb_board): 
    #add more questions
    questions  = {'What does a string and an int added together return?': 'Error', 'Are arrays mutable? (True or False)': 'True', 'Are tuples mutable? (True or False)': 'False'}
    selected_question = random.choice(list(questions.keys()))
    while True:
        col_input = int(input("Which column would you like to play in? "))
        row_input = int(input("Which row would you like to play in? "))

        if not (0 <= row_input < len(board) and 0 <= col_input < len(board[0])):
            print("Invalid")
            continue


        if board[row_input][col_input] != " ":
            print("you have already picked this before")
            continue


        if bomb_board[row_input][col_input] == "*":
            #update this part

            print(selected_question)
            #counter()
            question_input = str(input("Answer this question for a redemption round "))
            

            if questions[selected_question] == question_input:
                board[row_input][col_input] = "*"
                print("You can keep on going!")
                return True
            else:
                print_board(bomb_board)
                print("Game Over")
                return False

        bombs_nearby = count_adjacent_bombs(row_input, col_input, bomb_board)

        if bombs_nearby > 0:
            board[row_input][col_input] = str(bombs_nearby) 
        else:
            board[row_input][col_input] = "0"
        return True

       


def create_bomb_board(bombs=10):
    bomb_board = create_board()
    bomb_loc = random.sample(range(11 * 11), bombs)

    for pos in bomb_loc:
        row = pos // 11
        col = pos % 11
        bomb_board[row][col] = "*"

    return bomb_board

def play_game():
    player_board = create_board()  
    bomb_board = create_bomb_board(10) 

    safe = 111
    count = 0

    while True:
        print_board(player_board)  
        if not check_location(player_board, bomb_board):
            break
        
        count = 0
        for row in player_board:
            for cell in row:
                if cell != " " and cell != "*":
                    count += 1

        if count == safe:
            print_board(bomb_board)
            print("You won the game!")
            break
        

play_game()
