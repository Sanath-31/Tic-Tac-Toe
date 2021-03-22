#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+ ' ''|' + ' ' + board[8]+ ' ''|' + ' ' + board[9])
    print('----------')
    print(board[4]+ ' ''|' + ' ' + board[5]+ ' ''|' + ' ' + board[6])
    print('----------')
    print(board[1]+ ' ''|' + ' ' + board[2]+ ' ''|' + ' ' + board[3])


# In[2]:


test_board = [' ']*10
display_board(test_board)


# In[3]:


def player_input():
    
    '''
    OUTPUT = (PLAYER 1 MARKER, PLAYER 2 MARKER)
    '''
    marker = ''
    
    # Keep asking Player 1 to choose X or O
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Choose X or O: ').upper()
    
    # Assign Player 2, the opposite marker
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')


# In[4]:


player_input()


# In[5]:


def place_marker(board, marker, position):
    board[position] = marker


# In[6]:


place_marker(test_board,'$',5)
display_board(test_board)


# In[7]:


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[8]:


win_check(test_board,' ')


# In[9]:


import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'


# In[10]:


def space_check(board,position):
    
    return board[position] == ' '


# In[11]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    
    # Board is full if it return TRUE
    return True


# In[12]:


def player_choice(board):
    
    position = 0
    
    while position not in range(1,10) or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
        
    return position


# In[13]:


player_choice(test_board)


# In[16]:


def replay():
    
    choice = input("Do you want to play again? Enter Yes or No: ")
    
    return choice == 'yes'


# In[ ]:


print('Welcome to Tic Tac Toe')


while True:
    
    # SET EVERYTHING UP (BOARD, CHOOSE MARKERS, WHO GOES FIRST)
    the_board = [' ']*10
    
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first!')
    
    play_game = input('Ready to play? y or n? ')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    ## GAME PLAY
    
    while game_on:
        
        if turn == 'Player 1':
            
            # Show the board
            display_board(the_board)
            
            # Choose a position
            position = player_choice(the_board)
            
            # Place the marker on the position
            place_marker(the_board,player1_marker,position)
            
            # Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("IT'S A TIE!!")
                    game_on = False
                else:
                    turn = 'Player 2'
        
        else:
            # Show the board
            display_board(the_board)
            
            # Choose a position
            position = player_choice(the_board)
            
            # Place the marker on the position
            place_marker(the_board,player2_marker,position)
            
            # Check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("IT'S A TIE!!")
                    game_on = False
                else:
                    turn = 'Player 1'    
    
    
    if not replay():
        break
    # BREAK OUT OF THE WHILE LOOP on replay()


# In[ ]:




