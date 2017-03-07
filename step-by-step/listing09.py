# Let's create a separate function for representation of the game board.
# Now, the main part of the script looks more readable.

indexesList = map( str, range(9) )
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
    printBoard( board, "\nGame board:" )