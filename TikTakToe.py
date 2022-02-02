
"""

Welcome to Tik Tak Toe!

Run all of the function cells to get things set up.

Then, call the tiktaktoe() function to play.

Enjoy!


"""


# Player name function

def playernamesetup():
    
    player1name = input("Enter Player 1 Name: ")
    player2name = input("Enter Player 2 Name: ")
    print("\n",f"Welcome to the game, {player1name} and {player2name}!","\n",f"{player1name} is X","\n", f"{player2name} is O",sep="")
    return player1name, player2name

    
# Board printer function - prints out the current state of the game board, stored in the global board_state list

def board_printer():
    print("\n",f"_{board_state[0]}_|",f"_{board_state[1]}_|",f"_{board_state[2]}_", sep="")
    print(f"_{board_state[3]}_|",f"_{board_state[4]}_|",f"_{board_state[5]}_", sep="")
    print(f" {board_state[6]} |",f" {board_state[7]} |",f" {board_state[8]} ", sep="")


# Board helper function - tutorial shows a numbered grid while explaining the controls for the game

def board_helper():
    
    board_help = ["1","2","3","4","5","6","7","8","9"]

    print("Enter one of the numbers below to take your turn in that square!")
    print("\n",f"_{board_help[0]}_|",f"_{board_help[1]}_|",f"_{board_help[2]}_", sep="")
    print(f"_{board_help[3]}_|",f"_{board_help[4]}_|",f"_{board_help[5]}_", sep="")
    print(f" {board_help[6]} |",f" {board_help[7]} |",f" {board_help[8]} ", sep="")
    
    if board_state == ["_","_","_","_","_","_"," "," "," "]:
        print("\n","X gets to go first. Your game board:", sep="")
    

# player turn function - figures out whose turn it is

def is_it_p1_turn():
    #whose turn is it?
    if board_state == ["_","_","_","_","_","_"," "," "," "]:
        player1turn = True
    elif board_state.count("X") == board_state.count("O"):
        player1turn = True
        print("\n",f"{player1name}, your turn!", sep="")
    else:
        player1turn = False
        print("\n",f"{player2name}, your turn!", sep ="")
    
    return player1turn


# user move function. Cased inside make_a_move below. Checks whose turn, accepts valid input, updates the board_state

def usermoves(p1turn,valid_list):
    global board_state
    
    if p1turn == True:
            x_position = "default"
            while x_position.isdigit() == False or int(x_position) not in valid_list:
                x_position = input("")
                if x_position.isdigit() == False or int(x_position) not in valid_list:
                    print("Sorry! Not a valid move.")
            else:
                board_state[int(x_position)-1] = "X"
                
    elif p1turn == False:
            o_position = "default"
            while o_position.isdigit() == False or int(o_position) not in valid_list:
                o_position = input("")
                if o_position.isdigit() == False or int(o_position) not in valid_list:
                    print("Sorry! Not a valid move.")
            else:
                board_state[int(o_position)-1] = "O"


# User move function (higher level). Pulls and passes in key info to usermoves(), then prints the updated board

def make_a_move():
    # whose turn
    is_p1 = is_it_p1_turn()
        
    # valid_list var - what are the available moves?
    valid_moves = valid_move_checker()
    print("\n","Available moves: ", valid_moves, sep="")
    
    # accept user input
    usermoves(is_p1,valid_moves)
    
    # print the board
    board_printer()
    
    
# Victory check function

def victory_check():
    
    """ 
    possible winning combos: 

    123 [012]
    456 [345]
    789 [678]

    147 [036]
    258 [147]
    369 [258]

    159 [048]
    357 [246]

    """
 
    if ((board_state[0] == "X" and board_state[1] == "X" and board_state[2] == "X") or
    (board_state[3] == "X" and board_state[4] == "X" and board_state[5] == "X") or
    (board_state[6] == "X" and board_state[7] == "X" and board_state[8] == "X") or
    (board_state[0] == "X" and board_state[3] == "X" and board_state[6] == "X") or
    (board_state[1] == "X" and board_state[4] == "X" and board_state[7] == "X") or
    (board_state[2] == "X" and board_state[5] == "X" and board_state[8] == "X") or
    (board_state[0] == "X" and board_state[4] == "X" and board_state[8] == "X") or
    (board_state[2] == "X" and board_state[4] == "X" and board_state[6] == "X")):
        return f"{player1name} wins!"
        
    elif ((board_state[0] == "O" and board_state[1] == "O" and board_state[2] == "O") or
    (board_state[3] == "O" and board_state[4] == "O" and board_state[5] == "O") or
    (board_state[6] == "O" and board_state[7] == "O" and board_state[8] == "O") or
    (board_state[0] == "O" and board_state[3] == "O" and board_state[6] == "O") or
    (board_state[1] == "O" and board_state[4] == "O" and board_state[7] == "O") or
    (board_state[2] == "O" and board_state[5] == "O" and board_state[8] == "O") or
    (board_state[0] == "O" and board_state[4] == "O" and board_state[8] == "O") or
    (board_state[2] == "O" and board_state[4] == "O" and board_state[6] == "O")):
        return f"{player2name} wins!"
    
    else:
          return "Play On"


# Checks the available valid moves

def valid_move_checker():
    valid_moves = []
    for idx,item in enumerate(board_state):
        if item == (" ") or item == ("_"):
            valid_moves.append(idx+1)
        else:
            pass
    return valid_moves


# One full game

def gameplay():

    global board_state
    global player1name
    global player2name
    board_state = ["_","_","_","_","_","_"," "," "," "]

    player1name, player2name = playernamesetup()

    board_helper()

    board_printer()
    
    while 1:
    
        victory_check_return = victory_check()
        if victory_check_return == "Play On":
            pass
        else:
            print("\n",victory_check_return,sep="")
            break

        valid_moves = valid_move_checker()
        if valid_moves == []:
            print("\n","It's a draw.",sep="")
            break
        else:
            pass

        make_a_move()
        

# Checks whether you want to replay

def replay_cycle():

    replay = "default"

    while replay != "Y" and replay != "N":
        replay = input("Would you like to play again? (Y/N) ")
        if replay != "Y" and replay != "N":
            print("Sorry! Not a valid response.")
        else:
            return replay


# Wraps it all up!

def tiktaktoe():
    
    while 1:
        gameplay()
        replaycheck = replay_cycle()
        if replaycheck == "Y":
            pass
        else:
            print("Thanks for playing Tik Tak Toe!")
            break
    

tiktaktoe()





                
    
    







