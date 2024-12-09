def print_board(board):
    for index, row in enumerate(board[::-1]):
        print(len(board) - 1 - index, "┃", " ".join(row))
    print("  ━━━━━━━━━━━━━━━━━━━━━━━━")
    print("    " + " ".join(str(i) for i in range(len(board[0]))))