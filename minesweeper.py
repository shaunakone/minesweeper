import numpy as np
import random
#import time

def create_board():
    board = np.full((11, 11), " ")
    return board

def print_board(board):
    for index, row in enumerate(board[::-1]):
        print(len(board) - 1 - index, "┃", " ".join(row))
    print("  ━━━━━━━━━━━━━━━━━━━━━━━━")
    print("    " + " ".join(str(i) for i in range(len(board[0]))))

def create_bomb_board(bombs=10):
    bomb_board = create_board()
    bomb_loc = random.sample(range(11 * 11), bombs)

    for pos in bomb_loc:
        row = pos // 11
        col = pos % 11
        bomb_board[row][col] = "*"

    return bomb_board

def count_adjacent_bombs(row, col, bomb_board):
    count = 0
    rows = len(bomb_board)
    cols = len(bomb_board[0])

    for r in range(max(0, row - 1), min(row + 2, rows)):
        for c in range(max(0, col - 1), min(col + 2, cols)):
            if r == row and c == col:
                continue 
            if bomb_board[r][c] == '*':
                count += 1
    return count


def dig(row, col, board, bomb_board):
    if not (0 <= row < len(bomb_board) and 0 <= col < len(bomb_board[0])):
        return

    if board[row][col] != " ":
        return
        
    bombs_nearby = count_adjacent_bombs(row, col, bomb_board)
    if bombs_nearby > 0:
        board[row][col] = str(bombs_nearby) 
    else:
        board[row][col] = "0"
    if bombs_nearby > 0:
        return None

    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < len(bomb_board) and 0 <= c < len(bomb_board[0]):
                if board[r][c] == " " and bomb_board[r][c] != "*":
                    bombs_nearby = count_adjacent_bombs(r, c, bomb_board)
                    board[r][c] = str(bombs_nearby) if bombs_nearby > 0 else "0"



def check_location(board, bomb_board): 
    questions  = {'What does a string and an int added together return?': 'Error', 'Are arrays mutable? (True or False)': 'True', 'Are tuples mutable? (True or False)': 'False', 'What does the code 5/2 return?': '2.5', 'What does the code 7//2 return?': '3', 'What does the code 2.0**3 return?': '8.0', 'What symbol represents a comment in Python?': '#'}
    used_questions = set()
    while True:
        col_input = (input("Which column would you like to play in? "))
        row_input = (input("Which row would you like to play in? "))

        if col_input.isalpha() or row_input.isalpha():
            print("Invalid")
            continue
        else:
            col_input = int(col_input)
            row_input = int(row_input)

        

        if not (0 <= row_input < len(board) and 0 <= col_input < len(board[0]) and col_input != range(0,11)and row_input != range(0,11)):
            print("Invalid")
            continue

        if board[row_input][col_input] != " ":
            print("you have already picked this before")
            continue

        if bomb_board[row_input][col_input] == "*":
            selected_question = random.choice(list(questions.keys()))
            print(selected_question)

            question_input = str(input("Answer this question for a redemption round "))
            

            if questions[selected_question] == question_input:
                board[row_input][col_input] = "*"
                print("You can keep on going!")
                return True
            else:
                print_board(bomb_board)
                print("Game Over")
                return False

        dig(row_input, col_input, board, bomb_board)
        return True



def play_game():
    player_board = create_board()  
    bomb_board = create_bomb_board(10) 

    safe = 11*11-10
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
