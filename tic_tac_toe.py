# Create and display board

def display(board):

    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])

test_board = ['#','1', '2', '3','4', '5', '6', '7', '8', '9']
display(test_board)

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

player1_marker, player2_marker = player_input()

print(f'Player 1 is {player1_marker} and player 2 is {player2_marker}.')

# Update board with players marker

def place_marker(test_board, update_position, player_marker):
    test_board[update_position] = player_marker
    
# Keep track of the number of moves

moves = 1

# Manage the player's turns

def player_turn(test_board, player_marker, player2_marker):

    global moves

    while True:
        
        print('\n'*100)
        display(test_board)
      
        
        if moves %2 == 1:
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
        
        if update_position in range(1,10) and test_board[update_position] not in ["X", "O"]: 
            place_marker(test_board, update_position, player_marker)
            display(test_board)

            moves += 1

            if check_winner(test_board, player1_marker, player2_marker):
                print('\n'*100)
                display(test_board)
                break

            if moves == 10:
                print("It's a draw!")
                print('\n'*100)
                break
            
        else:
            print('Please pick another space on the board.')
    
    
# Winning conditions

win_conditions = [(1,2,3), (4,5,6), (7,8,9), (1,5,9), (3,5,7), (1,4,7), (2,4,6), (3,6,9)]

# Check for a winner
def check_winner(test_board, player1_marker, player2_marker):

    
    for conditions in win_conditions:
        if (test_board[conditions[0]] == player1_marker and
            test_board[conditions[1]] == player1_marker and
            test_board[conditions[2]] == player1_marker):
            print('Congrats player 1 you won!')
            return True
        elif (test_board[conditions[0]] == player2_marker and
            test_board[conditions[1]] == player2_marker and
            test_board[conditions[2]] == player2_marker):
            print('Congrats player 2 you won!')
            return True 
    
    return False

# ask to play again
def play_again():

    choice = "wrong"
    
    while choice not in 'Y' or 'N':
        choice = input("Do you want to play again: 'Y' or 'N': ").upper()

        if choice == "Y":
            return True
        else:
            break


play_more = True
        

player_turn(test_board, player1_marker, player2_marker)
display(test_board)
play_more = play_again()

  
