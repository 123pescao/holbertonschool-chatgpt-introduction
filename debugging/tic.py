#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the tic-tac-toe board.

    Parameters:
        board (list of list): The current tic-tac-toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there's a winner in the current tic-tac-toe board.

    Parameters:
        board (list of list): The current tic-tac-toe board.

    Returns:
        str or None: "X" or "O" if there's a winner, otherwise None.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    """
    Check if the tic-tac-toe board is full.

    Parameters:
        board (list of list): The current tic-tac-toe board.

    Returns:
        bool: True if the board is full, otherwise False.
    """
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt, min_value, max_value):
    """
    Continuously prompt the user until a valid integer input is provided.

    Parameters:
        prompt (str): The prompt message to display to the user.
        min_value (int): The minimum allowed value.
        max_value (int): The maximum allowed value.

    Returns:
        int: A valid integer input from the user within the specified range.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Input must be between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def tic_tac_toe():
    """
    Simulate a two-player tic-tac-toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while not check_winner(board) and not is_board_full(board):
        print_board(board)
        row = get_valid_input(f"Enter row (0, 1, or 2) for player {player}: ", 0, 2)
        col = get_valid_input(f"Enter column (0, 1, or 2) for player {player}: ", 0, 2)
        if board[row][col] == " ":
            board[row][col] = player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")

tic_tac_toe()
