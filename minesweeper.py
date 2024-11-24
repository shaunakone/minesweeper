import numpy as np
import random
import time

def create_board():
    board = np.full((11, 11), " ")
    return board

def counter():
    count = 5

    while count != 0:
        #print(count)
        time.sleep(1)
        count -= 1

    print("You have 5 seconds to think")

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
    questions  = {'What does a string and an int added together return?': "Error"}

    while True:
        col_input = int(input("Which column would you like to play in? "))
        row_input = int(input("Which row would you like to play in? "))

        if not (0 <= row_input < len(board) and 0 <= col_input < len(board[0])):
            print("Invalid")
            continue

        if bomb_board[row_input][col_input] == "*":
            #update this part
            for question in questions:
                print(question)
                counter()
                question_input = str(input("Answer this question for a redemption round"))
                

                if questions[question] == question_input:
                    break
                else:
                    print_board(bomb_board)
                    print("Game Over")
            #print("Game Over")
            #print_board(bomb_board)
                    return False

        #
        bombs_nearby = count_adjacent_bombs(row_input, col_input, bomb_board)
        board[row_input][col_input] = (bombs_nearby)
        return True


def create_bomb_board(bombs=10):
    bomb_board = create_board()
    bomb_loc = random.sample(range(10 * 10), bombs)

    for pos in bomb_loc:
        row = pos // 10
        col = pos % 10
        bomb_board[row][col] = "*"

    return bomb_board

def play_game():
    player_board = create_board()  
    bomb_board = create_bomb_board(10) 

    while True:
        print_board(player_board)  
        if not check_location(player_board, bomb_board):
            break

play_game()
