# Create board

board = ['#','1', '2', '3','4', '5', '6', '7', '8', '9']

# Keep track of the number of moves
moves = 0

def display(board):

    print('\n'*100)
    
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])
    
    
# Get player to choose marker

def player_input():

    marker = ''
    
    while marker not in ['X', 'x', 'O', 'o']:
        marker = input("Player 1 pick between 'X' or 'O': ")
    
    player1 = marker.upper()

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return player1, player2

# Update board with players marker

def place_marker(board, update_position, player_marker):
    board[update_position] = player_marker


# Winning conditions

win_conditions = [(1,2,3), (4,5,6), (7,8,9), (1,5,9), (3,5,7), (1,4,7), (2,5,8), (3,6,9)]

# Check for a winner
def check_winner(board, player1_marker, player2_marker):

    
    for conditions in win_conditions:
        if (board[conditions[0]] == player1_marker and 
            board[conditions[1]] == player1_marker and 
            board[conditions[2]] == player1_marker):
            return 'Congrats player 1 you won!'
        elif (board[conditions[0]] == player2_marker and 
              board[conditions[1]] == player2_marker and 
              board[conditions[2]] == player2_marker):
            return 'Congrats player 2 you won!'
                
    return None


import random

# Manage the player's turns

def player_turn(board, player1_marker, player2_marker):

    global moves
    turn = random.randint(0,1)
    
    while True:
        
        display(board)
        
        if turn == 0:
            print("Player 1's turn.")
            player_marker = player1_marker
        else:
            print("player 2's turn.")
            player_marker = player2_marker

        update_position = input('Please pick the number location that you would like to place your marker: ')
        
        if not update_position.isdigit():
            print('Invalid input. Please pick a number location.')
            continue
            
        update_position = int(update_position)
        
        if update_position in range(1,10) and board[update_position] not in ["X", "O"]: 
            place_marker(board, update_position, player_marker)
            moves += 1

            winner_message = check_winner(board, player1_marker, player2_marker)
            if winner_message:
                display(board)
                print(winner_message)
                break

            if moves == 9:
                print("It's a draw!")
                display(board)
                break


            turn = 1 - turn
            
        else:
            print('Please pick another space on the board.')
       
       

# Allowing players to play again
    
def play_again():

    choice = " "
    
    while choice not in ['Y', 'N']:
        choice = input("Do you want to play again: 'Y' or 'N': ").upper()

        if choice not in ['Y', 'N']:
            print('Sorry not valid.')

        if choice == "Y":
            return True
        else:
            return False
    

def reset_game():
    
    global moves, board
    board = ['#','1', '2', '3','4', '5', '6', '7', '8', '9']
    moves = 0
    
play_more = True


while play_more:
    reset_game()
    display(board)
    
    player1_marker, player2_marker = player_input()
    player_turn(board, player1_marker, player2_marker)
    
    play_more = play_again()
    