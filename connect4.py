board = [["_","_","_","_","_","_","_"] , ["_","_","_","_","_","_","_"] , ["_","_","_","_","_","_","_"] , ["_","_","_","_","_","_","_"] , ["_","_","_","_","_","_","_"] , ["_","_","_","_","_","_","_"]]


p1Name = input("Enter P1 name: ")
p2Name = input("Enter P2 name: ")

#P1 starts the game
current_turn = "P1"

#Runs the game by printing the board and calling turn checks win as well
def game():
    while check_win(current_turn) == False:
        for row in board:
            print(row)
        turn()
    if current_turn == "P1":
        print(p2Name + " wins!")
    else:
        print(p1Name + " wins!")
    print("Final board:")
    for row in board:
        print(row)
    return

#Prompts current player to make their move, calls move and check_win after input is recieved
def turn():
    column = int(input(current_turn + " Enter the column you want to play in: ")) - 1
    if check_valid_move(column):
        move(column)
        change_turn()
        return
    else:
        print("Invalid move")
        return

#Updates game board based on player move
def move(column):
    for row in reversed(board):
        if row[column] == "_" and current_turn == "P1":
            row[column] = "X"
            return
        elif row[column] == "_" and current_turn == "P2":
            row[column] = "O"
            return
    return

#After a turn checks if anyone has won, we reduce the number of columns or rows we iterate through to prevent us from going out of the index
def check_win(current_turn):
    #Determines who last moved so we know what to check for. It's opposite since the turn changes before check_win is called
    drop = "O" if current_turn == "P1" else "X"
    
    #No one can have won if the board is empty
    if not any("X" in row for row in board) or not any("O" in row for row in board):
        return False
    
    #Horizontal 
    for row in range(6):
        for column in range(4):
            if board[row][column] == drop and board[row][column+1] == drop and board[row][column+2] == drop and board[row][column+3] == drop:
                return True
                
    #Vertical
    for row in range(3):
        for column in range(7):
            if board[row][column] == drop and board[row+1][column] == drop and board[row+2][column] == drop and board[row+3][column] == drop:
                return True
            
    #Diagonal upwards
    for row in range(3):
        for column in range(4):
            if board[row][column] == drop and board[row+1][column+1] == drop and board[row+2][column+2] == drop and board[row+3][column+3] == drop:
                return True
            
    #Diagonal downwards
    for row in range(3, 6):
        for column in range(4):
            if board[row][column] == drop and board[row-1][column+1] == drop and board[row-2][column+2] == drop and board[row-3][column+3] == drop:
                return True
    return False

#checks to make sure the column is not full
def check_valid_move(column):
    if column > 7:
        return False
    if board[0][column] == 'X' or board[0][column] == 'O':
        return False
    return True

#Changes the current_turn contianed in this function since it uses global
def change_turn():
    global current_turn
    if current_turn == "P1":
        current_turn = "P2"
    else:
        current_turn = "P1"
    return


game()
