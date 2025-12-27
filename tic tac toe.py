
board = [" " for _ in range(9)]
# Step 2: Function to display the board
def print_board():
    
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Step 3: Function to check if someone has won
def check_winner(player):
    # All possible winning positions
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Step 4: Function to check if the board is full (Draw)
def is_draw():
    return " " not in board

# Step 5: Main game loop
def play_game():
    current_player = "X"  # X always starts
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Step 6: Ask player for input
        try:
            move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input! Please enter a number between 1-9.")
            continue

        # Step 7: Validate the move
        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move! Try again.")
            continue

        # Step 8: Place the move
        board[move] = current_player
        print_board()

        # Step 9: Check for winner
        if check_winner(current_player):
            print(f"🎉 Player {current_player} wins!")
            break

        # Step 10: Check for draw
        if is_draw():
            print("It's a draw!")
            break

        # Step 11: Switch players
        current_player = "O" if current_player == "X" else "X"

# Step 12: Run the game
play_game()


