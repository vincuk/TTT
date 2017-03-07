# Let's create a separate function for representation of the game board.
# Now, the main part of the script looks more readable.

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

printBoard( map( str, range(9) ), "Cell indexes:" )

board = [" "] * 9
index = "0"

while index != "q":
    index = raw_input( "Enter a cell index... " )
    if index == "q":
        break
    elif index == "i":
        printBoard( map( str, range(9) ), "\nCell indexes:" )
        continue
    elif index not in map( str, range(9) ):
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