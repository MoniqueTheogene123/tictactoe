# app.py

def instructions_input():
    """Ask user if they want instructions and handle input validation"""
    while True:
        instructions = input("Would you like instructions on how to play the game? (yes/no) : ").lower()
        
        if instructions in ['yes', 'y']:
            print("Visit this page to learn: https://en.wikipedia.org/wiki/Tic-tac-toe.")
            return True
        elif instructions in ['no', 'n']:
            print("No instructions, OK! Let's go")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'")

def display_board(board):
    """Display the current game board"""
    print(f"\n {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("-----------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("-----------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

def main():
    print("Welcome to Tic Tac Toe!")
    
    # Initialize empty board
    board = [['1','2','3'], 
             ['4','5','6'], 
             ['7','8','9']]
    
    # Call the function - it will handle the loop and validation
    instructions_input()
    
    # Game continues here regardless of choice
    print("\nStarting the game now...")
    
    current_player = 'X'
    game_over = False
    
    while not game_over:
        display_board(board)
        print("\n")
        user_input = input(f"Player {current_player}, Enter a number between 1-9: ")
        
        # TO DO:  Validate input
        
        # If user wants to quit, let them at any time
        if user_input.lower()== 'quit':
            print("\n Quitting Game")
            return

        # Update board
        valid_move = False
        for row in range(3):
            for col in range(3):
                if board[row][col] == user_input:
                    board[row][col] = current_player
                    valid_move = True
                    break
            if valid_move:
                break
        
        if not valid_move:
            print("Invalid move! Please try again.")
            continue

        # Define check_winner params to win
        def check_winner(board, current_player):
            for row in range(3):
                if board[row][0] == current_player and board[row][1] == current_player and board[row][2] == current_player:
                    return True
                
            for row in range(3):
                if board[0][col] == current_player and board[1][col] == current_player and board[2][col] == current_player:
                    return True
                
            if board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player:
                return True
            
            return False        
        
        
        # Check for win across diagnal row
        if check_winner(board, current_player):
            display_board(board)
            print(f"\nPlayer {current_player} wins!")
            game_over = True
            
            
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
#run game
if __name__ == "__main__":
    main()
