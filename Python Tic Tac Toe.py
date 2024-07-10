from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('- - -')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('- - -')
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    
    board[position] = marker

def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark))

import random

def first_choice():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        
        position = int(input("Enter a position to place your marker (1-9): "))
    return position

def replay_game():
    
    return input("Would you like to play again? Y or N: ").upper().startswith('y')

print("Let's Play Tic Tac Toe!")

while True:
    
    fresh_board = [' '] * 10
    player1_marker , player2_marker = player_input()
    turn = first_choice()
    print(turn+ ' will go first!')
    
    start_game = input('Are you ready to play? Y or N: ')
    
    if start_game.upper() == 'Y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == 'Player 1':
            
            display_board(fresh_board)
            print("Player 1's turn!")
            position = player_choice(fresh_board)
            place_marker(fresh_board, player1_marker, position)
            
            if win_check(fresh_board, player1_marker):
                display_board(fresh_board)
                print('Player 1 is the winner!')
                game_on = False
            else:
                if full_board_check(fresh_board):
                    display_board(fresh_board)
                    print('The game is a draw!')
                    game_on = False
                else:
                    turn = 'Player 2'
                    
        else:
            
            display_board(fresh_board)
            print("Player 2's turn!")
            position = player_choice(fresh_board)
            place_marker(fresh_board, player2_marker, position)
            
            if win_check(fresh_board, player2_marker):
                display_board(fresh_board)
                print('Player 2 is the winner!')
                game_on = False
            else:
                if full_board_check(fresh_board):
                    display_board(fresh_board)
                    print('The game is a draw!')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay_game():
        break