import math  #My name jeff
# END OF IMPORT STATEMENTS

# FUNCTION filled (from previous submission)
def filled(board):
    x = 0
    for y in range(0,9):
        if board[y] == "X":
            x = x + 1
        
    if x == 9:
        return True
    else:
        return False
        
# FUNCTION fullRow (from previous submission)
def fullRow(board, letter, length_of_board):
    
    a = 1
    b = 0
    count = 0
    d = 1
    while d <= length_of_board:
        a = 1
        count = 0 
        while a <= length_of_board:
            if board[b] == letter:
                count = count + 1
            if count == length_of_board:
                return True
            b = b + 1
            a = a + 1
        d = d + 1
    return False
    
# FUNCTION fullCol (from previous submission)
def fullCol(board, letter, length_of_board):
    a = 1
    b = 0
    c = 0
    d = 1
    while a <= length_of_board:
        d = 1
        c = 0
        while d <= length_of_board:
            if board[int(b)] == letter:
                c = c + 1
            b = b + length_of_board
            if c == length_of_board:
                return True
            d = d + 1
        b = a
        a = a + 1
    return

# FUNCTION fullDiag (from previous submission)
def fullDiag(board, letter, length_of_board):
    a = 0
    count = 0
    for i in range(int(length_of_board)):
        if board[int(a)] == letter:
            count = count + 1
        a = a + int(length_of_board) + 1
    if count == length_of_board:
        return True
    
    b = int(length_of_board) - 1
    count1 = 0
    for i in range(int(length_of_board)):
        if board[b] == letter:
            count1 = count1 + 1
        b = b + int(length_of_board) - 1
    if count1 == length_of_board:
        return True
     
    return False
    
# FUNCTION printBoard:
#      If the slot is filled, display the character that fills it
#      If the slot is not filled, display the index of the slot
def printBoard(board):
    print("Here is the board:")
    a = math.sqrt(len(board))
    b = 1
    c = 1
    d = 1
    while c <= a:
        b = 1
        while b <= a:
            if board[d-1] != "X" and board[d-1] != "O":
                print(d,"| ",end='')
            else:
                print(board[d-1],"| ",end='')
            d = d + 1
            b = b + 1
        print("")
        c = c + 1
        
# FUNCTION updateBoard(board, who, where):
#      If the third parameter is passed, place "who" in position "where" 
#         in the board and return True UNLESS THAT SLOT IS ALREADY FILLED
#         If the slot is filled, print "That position is filled!" and return False
#      If the third parameter is not passed, look for the first empty slot and fill it with "who" and return True
#         If there are no empty slots in the board, print("No place to put the", who, "!") and return False
def updateBoard(board, who, where = None):
    if where != None:
        if (board[where-1] != "X") and (board[where-1] != "O"):
            board[where-1] = who
            return True
        if (board[where-1] != "_"):
            print("That position is filled!")
            return False
            
    a = 0
    while a <= 8:
        if board[a] != "X" and board[a] != "O":
            board[a] = who
            return True
        a = a + 1
            
    print("No place to put the", who, "!")
    return False

# FUNCTION getWinner: 
#     Return X if X has a full row, column or diagonal.
#     Return O if O has a full row, column or diagonal.
#     Otherwise, return "Draw"
def getWinner(board):
    if fullRow(board, "X", 3) or fullCol(board, "X", 3) or fullDiag(board, "X", 3)== True:
        return "X"
        
    elif fullRow(board, "O", 3) or fullCol(board, "O", 3) or fullDiag(board, "O", 3) == True:
        return "O"
    
    return "Draw"

#FUNCTION gameOver:
#     Return True if X or O has a full row, column or diagonal, or if the board is full 
#     Otherwise, return False

def gameOver(board):
    x = False
    if fullRow(board, "X", 3) or fullRow(board, "O", 3)or fullCol(board, "X", 3) == True:
        x = True
    if fullCol(board, "O", 3) or fullDiag(board, "X", 3) or fullDiag(board, "O", 3) == True:
        x = True
    
    elif(x == False):
        for a in range(len(board)):
        
            if(board[a]=='X')or(board[a]=='O'):
                x = True
            else:
                x = False
                break
    return x
    return False

# END OF FUNCTION DEFINITIONS

# MAIN PART OF THE PROGRAM -- DON'T CHANGE ANYTHING IN MAIN!
def main():
    board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    # YOUR CODE BEGINS HERE
    while not gameOver(board):
        printBoard(board)
        x = int(input("Enter move for x (1-9): "))
        print(x)
        if x < 1 or x > 9:
            print("Please enter a valid position number 1 through 9")
        else:
            if updateBoard(board, "X", x):
                updateBoard(board, "O")
            else:
                print("Please try again.")

    printBoard(board)
    winner = getWinner(board)
    if winner == "Draw":
        print("It's a draw!")
    else:
        print("The winner is", winner, "!")
  
# INCLUDE THE FOLLOWING 2 LINES, BUT NOTHING ELSE BETWEEN HERE
if __name__ == "__main__":
    main()
# AND HERE
