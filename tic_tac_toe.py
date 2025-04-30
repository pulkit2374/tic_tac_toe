import random

def print_board(board):
    print("\n")
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        print(row)
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner(board):
    combos = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in combos:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                return move
            else:
                print("That spot is taken.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number from 1 to 9.")

def get_ai_move(board):
    empty = [i for i, v in enumerate(board) if v == " "]
    return random.choice(empty)

def play_game(mode="human"):
    board = [" " for _ in range(9)]
    current = "X"
    print_board(board)

    while " " in board:
        print(f"{current}'s turn.")
        if mode == "ai" and current == "O":
            move = get_ai_move(board)
        else:
            move = get_player_move(board)

        board[move] = current
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            return winner
        current = "O" if current == "X" else "X"

    print("It's a draw!")
    return "Draw"

def main():
    print("Welcome to Tic Tac Toe!")
    mode = input("Choose mode - 'human' or 'ai': ").strip().lower()
    if mode not in ["human", "ai"]:
        print("Invalid mode. Defaulting to human vs human.")
        mode = "human"

    x_wins = o_wins = draws = 0
    while True:
        result = play_game(mode)
        if result == "X":
            x_wins += 1
        elif result == "O":
            o_wins += 1
        else:
            draws += 1

        print(f"\nStats - X Wins: {x_wins}, O Wins: {o_wins}, Draws: {draws}")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
