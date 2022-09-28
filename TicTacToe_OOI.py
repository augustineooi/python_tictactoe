# This program implements a Tic Tac Toe games between 2 human players or 1 human player against the computer


def init_board():
    # Create an empty TicTacToe Board using a list of lists
    # Player 1 uses X and is represented as +1 in the TicTacToe Board
    # Player 2 uses O and is represented as -1 in the board
    # An empty area is represented as 0 
    
    # The list mirrors the TicTacToe Board in location
    # i.e.TTT[0][0] represents the top left corner of the board, [2][2] the bottom right, and [1][1] the middle
    # of the borads respectively.
    
    T = [
        [0,0,0], 
        [0,0,0], 
        [0,0,0]
        ]
        
    return T


def display_board(T):
    # function to display the TicTacToe Board based on TicTacToe Data Structure    
    # the TicTacToe Board is represented as +1, -1, 0
    # and we need to translate that to X, O and blanks respectively to be displayed
    T_Display_Map = {"1":"X", "-1":"O", "0":" "}
    
    # setup a list to map the displayed values (X, O, blanks)
    T_display = [["","",""],["","",""],["","",""]]
    
    # Map the TTT Board to display values using the dictionary
    for i in range(3):
        for j in range(3):
            display_val = str(T[i][j])
            T_display[i][j] = T_Display_Map[display_val]

    # display the board
    print("     |     |     ")
    print("  {}  |  {}  |  {}   ".format(T_display[0][0], T_display[0][1],T_display[0][2]))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  {}  |  {}  |  {}   ".format(T_display[1][0], T_display[1][1],T_display[1][2]))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  {}  |  {}  |  {}   ".format(T_display[2][0], T_display[2][1],T_display[2][2]))
    print("     |     |     ")
    

def user_instructions():
    # Displays instructions to the user
    # To be displayed during the start of the game
    # and can be called up by the user at any point of the game
    
    # We present the board layout, and indicate to the user how they can select a cell in the Tic Tac Toe board
    # The cells are labled from 1 to 9 to ease selection by the user
    
    
    print("\n********** INSTRUCTIONS **********\n") 
    print("Please select a cell for your next move, as indicated by the label of the cells below:")
    print("")
    
    # display the board label for the user
    print("     |     |     ")
    print("  {}  |  {}  |  {}   ".format(1, 2, 3))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  {}  |  {}  |  {}   ".format(4, 5, 6))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  {}  |  {}  |  {}   ".format(7, 8, 9))
    print("     |     |     ")
    

def check_input(T_Board, usr_input):
    # function checks the validity of user input
    
    # T_Board is the latest valid Tic Tac Toe Board
    # usr_input should be strings of integer from "1" - "9" as entered by the user
    
    # set up the mapping between user_input and coordinates in the Tic Tac Toe board
    usr_to_board = {"1":(0,0), "2":(0,1), "3":(0,2), \
                    "4":(1,0), "5":(1,1), "6":(1,2), \
                    "7":(2,0), "8":(2,1), "9":(2,2)}
    
    # convert usr_input to board coordinates
    usr_coord = usr_to_board[usr_input]
    
    # find value of board in coordinates entered by user
    board_value = T_Board[usr_coord[0]][usr_coord[1]]
    
    # returns True if board at selected cell is empty (value is 0)
    return board_value == 0


def update_board(T_board, player, plyr_input):
    # function updates the board T_board based on player input (from "1" - "9")
    # player can be player1 (assigned +1 to the board) or player2 (assigned -1)
    # returns the updated board
    
    # maps player to assigned value in the tic tac toe board
    player_map = {"player1":1, "player2":-1}
    
    # maps player input to coordinates in the tic tac toe board
    usr_to_board = {"1":(0,0), "2":(0,1), "3":(0,2), \
                    "4":(1,0), "5":(1,1), "6":(1,2), \
                    "7":(2,0), "8":(2,1), "9":(2,2)}
    
    player_val = player_map[player]
    player_coord = usr_to_board[plyr_input]
    
    # update the board location player_coord with player_val
    x_val = player_coord[0]
    y_val = player_coord[1]
    T_board[x_val][y_val] = player_val
    
    return T_board


def find_game_state(T):
    # function takes tic tac toe board as input
    # and returns the state of the board
    # There should be four states: Game_Cont, P1_Win, P2_Win, End_Draw
    
    winner_tracker = 0     # if there is a winner, track if it is Player 1 or 2
    
    # check to see if there is a win
    hor_sum = 0
    vert_sum = 0
    diag_l_r_sum = 0
    diag_r_l_sum = 0

    for j in range(3):
        # checking the horizontal lines
        hor_sum = sum(T[j])
        if hor_sum in (3, -3):
            print("\nWon at horizontal line {}".format(j+1))
            winner_tracker = hor_sum / 3
            break
        else:
            hor_sum = 0
    
        # checking the vertical lines
        for i in range(3):
            vert_sum += T[i][j] 
        if vert_sum in (3, -3):
            print("\nWon at vertical line {}".format(j+1))
            winner_tracker = vert_sum / 3
            break
        else:
            vert_sum = 0
    
        # checking diagonal lines
        diag_l_r_sum += T[j][j]      # checking the left-right diagonal line
        diag_r_l_sum += T[j][2-j]    # checking the right-left diagonal line
        if diag_l_r_sum in (3, -3):
            print("\nWon at diag left right")
            winner_tracker = diag_l_r_sum / 3
            break
        elif diag_r_l_sum in (3, -3):
            print("\nWon at diag right left")
            winner_tracker = diag_r_l_sum / 3
            break
    
    if winner_tracker == 1:
        return "P1_Win"
    elif winner_tracker == -1:
        return "P2_Win"
    elif sum(x == 0 for row in T for x in row) == 0:
        # the board is fully filled but nobody won
        return "End_Draw"
    else:
        return "Game_Cont"


# ------------------------------------------------
# The codes within this section is for implementation of a single-player game
# (against the computer)
#

def eval_score(T_board):
    # function is part of code for the single-player game (AI)
    # this function returns a score for the TicTacToe Board at the end of a game
    # if Computer (player2) wins, the score will be +10
    # if Human (player1) wins, the score will be -10
    
    # Computer plays according to the minimax search algorithm
    # Assign computer to be the maximizing player
    
    # Note that in the TicTacToe Board, a cell entry by player1 is assigned +1,
    # and player2 is assigned -1
        
    # check rows for winner
    for row in range(3):       
        if sum(T_board[row]) == 3:     # player1 has won
            return -10
        elif sum(T_board[row]) == -3:  # player2 has won
            return 10
    
    # check columns for winner
    for col in range(3):
        if (T_board[0][col] + T_board[1][col] + T_board[2][col]) == 3:     # player1 has won
            return -10
        elif (T_board[0][col] + T_board[1][col] + T_board[2][col]) == -3:   # player2 has won
            return 10
    
    # check diagonals for winner
    diag_l_r_sum = 0
    diag_r_l_sum = 0
    for i in range(3):
        diag_l_r_sum += T_board[i][i]      # checking the left-right diagonal line
        diag_r_l_sum += T_board[i][2-i]    # checking the right-left diagonal line
    
    if diag_l_r_sum == 3:     # player1 has won
        return -10
    elif diag_l_r_sum == -3:   # player2 has won
        return 10
    
    if diag_r_l_sum == 3:     # player1 has won
        return -10
    elif diag_r_l_sum == -3:   # player2 has won
        return 10
    
    return 0


def is_moves_left(T_board):  
    # function is part of code for the single-player game (AI)
    # this function checks if there are still moves available
    
    for i in range(3):
        for j in range(3):
            if (T_board[i][j] == 0):
                return True
    return False


def minimax(T_board, depth, is_max_player):
    # function is part of code for the single-player game (AI)
    # implements the minimax search algorithm. Considers all possible moves from the current board, and returns
    # the optimal value of the board
    
    # References:
    # (1) https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
    # (2) https://youtu.be/l-hh51ncgDI
    
    # computer's cell denoted as -1, and player's cell as +1
    # we set the computer to be the maximizing player
    computer, human = -1, +1
    
    # evaluate the score of the current board
    score = eval_score(T_board)
    
    # if the game has been won, return the evaluated score
    if score == 10:
        return score - depth     # score is adjusted to take number of moves into account (fewer moves are better)
    if score == -10:
        return score + depth
    
    # if this is a draw, the game has also ended and return evaluated score of 0
    if (is_moves_left(T_board) == False):
        return 0
    
    # otherwise, traverse down possible moves
    
    # if this is the maximizer's (computer's) move:
    if is_max_player:
        max_eval = -1000
        
        # traverse the cells
        for i in range(3):
            for j in range(3):
                
                # check if the board is empty
                if(T_board[i][j] == 0):
                    
                    # if it is, assign this to be the computer's move
                    T_board[i][j] = computer
                    
                    # call minimax recursively (it is now the minimizer's turn to evaluate)
                    eval_tmp = minimax(T_board, depth + 1, False)
                    
                    # find the highest score for this minimax search
                    max_eval = max(max_eval, eval_tmp)
                    
                    # reverse the computer's move
                    T_board[i][j] = 0
        
        return max_eval
    
    # if this is the minimzer's move:
    else:
        min_eval = +1000
        
        # traverse the cells
        for i in range(3):
            for j in range(3):
                
                # check if the board is empty
                if(T_board[i][j] == 0):
                    
                    # if it is, assign this to be the human's move
                    T_board[i][j] = human
                    
                    # call minimax recursively (it is now the maximizer's turn to evaluate)
                    eval_tmp = minimax(T_board, depth + 1, True)
                    
                    # find the lowest score for this minimax search
                    min_eval = min(min_eval, eval_tmp)
                    
                    # reverse the computer's move
                    T_board[i][j] = 0
        
        return min_eval


def computer_move(T_board):
    # function is part of code for the single-player game (AI)
    # function returns the best possible move for the computer
    # using the minimax algorithm
    
    # mapping of player input to coordinates in the tic tac toe board
    usr_to_board = {"1":(0,0), "2":(0,1), "3":(0,2), \
                    "4":(1,0), "5":(1,1), "6":(1,2), \
                    "7":(2,0), "8":(2,1), "9":(2,2)}
    
    # reversing the map above:
    board_to_usr = {}
    for key, value in usr_to_board.items():
        board_to_usr[value] = key
    
    
    # computer's cell denoted as -1, and player's cell as +1
    # we set the computer to be the maximizing player
    computer, human = -1, +1
    
    best_score = -1000
    best_move = (-1, -1)
    
    # traverse all cells and evaluate a minimax function for all empty cells
    # return the cell that gives the highest score
    
    for i in range(3):
        for j in range(3):
            
            # check if cell is empty
            if T_board[i][j] == 0:
                
                # computer makes the move in the empty cell
                T_board[i][j] = computer
                
                # evaluate the score from minimax on making this move
                eval_score = minimax(T_board, 0, False)     # next move is the minimizing player's
                
                # undo the move
                T_board[i][j] = 0
                
                # if the evaluated score from this move is better than the current best score
                # update the best score
                # and update the best move accordingly
                if (eval_score > best_score):
                    best_move = (i, j)
                    best_score = eval_score
    
    return board_to_usr[best_move]

# End of single-player code section
# ------------------------------------------------



# ************************************************
# implementing the Tic Tac Toe game:
    
def TicTacToe():
    # function implements a tic tac toe game
    # allows the players to choose either 1- or 2-player game
    
    import numpy as np
    
    # setup dictionaries to track basic player data
    # player1 plays "X", and player2 players "O"
    player_name = {"player1":"","player2":""}
    player_symbol = {"player1":"X","player2":"O"}
    
    # set up tracking counters
    games_ctr = 0          # the number of games played
    player1_score = 0      # cumulative wins for player 1
    player2_score = 0      # cumulative wins for player 2
    
    # game continues (up to multiple times) as long as it is not terminated by the players
    T_game_continue = True
        
    # start the series of games by asking players for names
    # and showing instructions on game-play
    
    print("\nWelcome to the game of Tic Tac Toe!")
    
    # get the number of players to play the game
    # if there are 2 players, they play against each other
    # if there is 1 player, player plays against the computer
    player_num = int(input("Please input the number of players (1 or 2): "))
    while player_num not in (1, 2):
        player_num = input("Please input the number of players (1 or 2): ")
    
    if player_num == 1:
        # if there is only one player, assigne the second player to be the computer
        player_name["player1"] = (input("Player 1, please enter your name: "))
        player_name["player2"] = "Computer"
    elif player_num == 2:
        player_name["player1"] = (input("Player 1, please enter your name: "))     
        player_name["player2"] = (input("Player 2, please enter your name: "))
    
    # display the player names, assigned symbols and instructions to play
    print('\n{} will play "{}"'.format(player_name["player1"], player_symbol["player1"]))
    print('{} will play "{}"'.format(player_name["player2"], player_symbol["player2"]))
    print('')
    user_instructions()   # function displays instructions on how to identify cells to play
    
    # the tic tac toe game commences and players continue playing (up to multiple games) 
    # unless they ask to stop
    while T_game_continue:
        # a new tic tac toe game commences
        # create a new tic tac toe board
        print("\n********** This is a new Tic Tac Toe game! **********\n")
        T_board = init_board()
        display_board(T_board)
        
        # track the state of the board
        game_state = "Game_Cont"
        
        # define valid user input (from "1" to "9")
        valid_range_int = list(range(1,10))
        valid_range = [str(x) for x in valid_range_int]
        
        # tracks cells that are valid for user input
        valid_cells = valid_range[:]

        # randomly select a player to start
        start_player = np.random.randint(1,3)
        
        # assign player to play current game, and player to play next
        current_player = "player" + str(start_player)
        next_player = "player" + str(3 - start_player)
        
        while game_state == "Game_Cont":
            # players play through the game until one person wins or ends in a draw
            print("\n\n\n----> It is {}'s turn (playing '{}').".format(player_name[current_player], player_symbol[current_player]))
            
            if (player_num == 1 and current_player == "player2"):
                player_input = computer_move(T_board)
                print("\nThe computer's move is {}".format(player_input))
            else:
                print("\nPlease select a cell to play by entering numbers between 1-9")
                player_input = input()
                # checking that player's input is valid:
                while player_input not in valid_range:
                    # loop until a valid cell number is entered
                    print("")
                    user_instructions()
                    print("\nPlease select a cell by entering numbers between 1 to 9, and enter 'b' to see the tic tac toe board")
                    player_input = input()
                
                    if player_input == "b":
                        display_board(T_board)
                        print("\nPlease select a cell by entering numbers between 1 to 9")
                        player_input = input()
            
                while not check_input(T_board, player_input):
                    print("\nWhat you have entered has been occupied. Please choose the cells {}".format(valid_cells))
                    player_input = input()
                        
            # we have a valid user input and thus we can update the board
            T_board = update_board(T_board, current_player, player_input)
            print("\nThis is the updated board: \n")
            display_board(T_board)
            
            # we remove what has been selected by the player from the list of selectable cells for the next player
            valid_cells.remove(player_input)
            
            # we check the effect of the player's input to the game
            game_state = find_game_state(T_board)
            
            # if the game has ended, we increase the number of games by 1
            if game_state != "Game_Cont":
                games_ctr += 1
            
            
            if game_state == "P1_Win":
                print("\n{} won this round.".format(player_name["player1"]))
                player1_score += 1
            elif game_state == "P2_Win":
                print("\n{} won this round.".format(player_name["player2"]))
                player2_score += 1
            elif game_state == "End_Draw":
                print("\nThis is a draw")
            
            # if the game continues, the turn goes to the next player
            current_player, next_player = next_player, current_player
            
        # one tic tac toe is finished
        # check to see if players want another game       
        # game stops when user enters "N" to the question
        next_game = ""
        while next_game not in ["y", "n"]:
            next_game = input("\nAnother game? (y/n): ")
        
        T_game_continue = (next_game == "y")
                 
                  
    # Game ends and summarize the results and initialize
    print("\nPlayers have played {} game(s)".format(games_ctr))
    print("{} has won {} games(s)".format(player_name["player1"], player1_score))
    print("{} has won {} games(s)".format(player_name["player2"], player2_score))


# Execute the TicT Tac Toe program:

TicTacToe()