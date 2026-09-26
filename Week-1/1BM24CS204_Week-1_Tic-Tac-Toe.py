import random
board = [" " for _ in range(9)]

def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False

def board_full():
    return " " not in board

print("TIC-TAC-TOE")
print("You are X and Computer is O")

while True:
    while True:
        position = int(input("Enter position (1-9): "))
        if position < 1 or position > 9:
            print("Enter a number between 1 and 9.")
        elif board[position - 1] != " ":
            print("Position already occupied.")
        else:
            board[position - 1] = "X"
            break

    display_board()

    if check_winner("X"):
        print("You Win!")
        break

    if board_full():
        print("Draw!")
        break

    available = []

    for i in range(9):
        if board[i] == " ":
            available.append(i)

    computer_position = random.choice(available)
    board[computer_position] = "O"

    print("Computer's move:")
    display_board()

    if check_winner("O"):
        print("Computer Wins!")
        break

    if board_full():
        print("Draw!")
        break