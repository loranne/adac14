print("Hello, world!")
print()

#######################################

# function for recording player moves
def make_move(board):
    """Asks player for a move and adds move to the board"""
    # asks user for player#
    player_num = input("Which player is making a move? 1 or 2 > ")
    print() 

    while True:
        
        # asks user for row, converts data to int
        player_row  = int(input("In which row would you like to place your mark? > ")) - 1
        print()

        # asks user for column, converts data to int
        player_column = int(input("In which column would you like to place your mark? > ")) - 1
        print()

        # if the space isn't a blank, the move is rejected
        if board[player_row][player_column] != "-":
            print("That space is already taken. Please try again.")
            print()

        # otherwise, if player 1, it gets an X
        elif player_num == "1":
            board[player_row][player_column] = "X"
            print("You placed an X at ({}, {}).".format(player_row + 1, player_column + 1))
            break
        
        # if player 2, it gets an O
        else:
            board[player_row][player_column] = "O"
            print("You placed an O at ({}, {}).".format(player_row + 1, player_column + 1))
            break
    
def print_board(board):
    """Prints board to show players"""

    print()
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("---+---+---")
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("---+---+---")
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])
    print()
 

def check_win(board):
    """Checks board for a winner and returns winner"""

    winner = False 

    # checks for rows win
    # if player 1 wins
    for row in board:
        if row[0] == row[1] == row[2] == "X":
            winner = 1
        
        # if player 2 wins
        elif row[0] == row[1] == row[2] == "O":
            winner = 2

    # checks for columns win
    for column in range(3):
        # if player 1 wins
        if board[0][column] == board[1][column] == board[2][column] == "X":
            winner = 1
        
        # if player 2 wins
        elif board[0][column] == board[1][column] == board[2][column] == "0":
            winner = 2

    # checks for diagonals win
    if (board[0][0] == board[1][1] == board[2][2] == "X") or (board[2][0] == board[1][1] == board[0][2] == "X"):
        winner = 1

    if (board[0][0] == board[1][1] == board[2][2] == "O") or (board[2][0] == board[1][1] == board[0][2] == "O"):
        winner = 2

    return winner


def check_tie(board):
    """Checks if board is full & there's a tie"""

    tie = True

    for row in board:
        for space in row:
            if space == "-":
                tie = False
                break
    
    return tie


def play(board):
    """Main function to play the game"""

    # welcome
    print("Let's play Tic Tac Toe!")
    print()
    # show empty board
    print(board)

    while True: 
        make_move(board)
        print_board(board)

        # variable assigned to check_win (true or false)
        winner = check_win(board)

        # same for check_tie
        tie = check_tie(board)

        # if there's a winner, state who it is, loop breaks
        if winner: 
            print("Player {} wins!".format(winner))
            break
        
        # if players tie, state tie, loop breaks    
        elif tie:
            print("There's a tie!")
            break

        # if no winner and no tie, nobody has won & game continues
        else: 
            print("No one has won yet.")
            print()

################################################

# define board and call main function to play 
tic_tac_toe_board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
play(tic_tac_toe_board)
