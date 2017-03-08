# Now, a very important step, teach computer to play tic-tac-toe.
# We create a function for randomly choosing a blank cell.

from random import randrange

indexesList = list( map( str, range(9) ) )
board = [" "] * 9

def printBoard( board, caption ):
    horizontalLine = "-" * 11
    separator = " | "
    print ( caption )
    for rowIndex in range(3):
        rowString = " "
        for columnIndex in range(3):
            rowString += board[columnIndex + 3*rowIndex]
            if columnIndex < 2:
                rowString += separator
        print( rowString )
        if rowIndex < 2:
            print( horizontalLine )

def testRow(rowIdx):
    if board[0 + 3*rowIdx] == board[1 + 3*rowIdx] == board[2 + 3*rowIdx] != " ":
        return True
    else:
        return False
        
def testColumn(colIdx):
    if board[0 + colIdx] == board[3 + colIdx] == board[6 + colIdx] != " ":
        return True
    else:
        return False
        
def testDiagonals():
    if board[0] == board[4] == board[8] != " ":
        return True
    elif board[2] == board[4] == board[6] != " ":
        return True
    else:
        return False
        
def testBoard():
    if testDiagonals():
        return True
    for index in range(3):
        if testRow(index) or testColumn(index):
            return True
    return False

def computerMove():
    index = 4
    while board[index] != " ":
        index = randrange(9)
    return index
    
printBoard( indexesList, "Cell indexes:" )
while True:
    index = raw_input( "Enter a cell index... " )
    if index == "q":
        break
    elif index == "i":
        printBoard( indexesList, "\nCell indexes:" )
        continue
    elif index not in indexesList:
        print( "Wrong index!\nUse 'i' for hint or 'q' to exit..." )
        continue
    else:
        index = int(index)
        if board[index] != " ":
            print( "This cell is not free!" )
            continue
        else:
            board[index] = "x"
            if testBoard():
                printBoard( board, "\nYou won :)" )
                break
            elif " " in board:
                index = computerMove()
                board[index] = "o"
                if testBoard():
                    printBoard( board, "\nYou lost :(" )
                    break
            else:
                printBoard( board, "\nDrawn game!" )
                break
    printBoard( board, "\nGame board:" )