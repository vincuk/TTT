# Now, we modify the code from the 5th example using example 7.
# But in the beginning of while loop nested for loops still looks ugly.

board = [" "] * 9
horizontalLine = "-" * 11
separator = " | "

while True:
    for rowIndex in range(3):
        rowString = " "
        for columnIndex in range(3):
            rowString += board[columnIndex + 3*rowIndex]
            if columnIndex < 2:
                rowString += separator
        print( rowString )
        if rowIndex < 2:
            print( horizontalLine )

    index = raw_input( "Enter a cell index or 'q' to exit..." )

    if index == "q":
        break
    elif index not in map( str, range(9) ):
        print( "Wrong index!" )
        continue
    else:
        index = int(index)
        if board[index] != " ":
            print( "This cell is not free!" )
            continue
        else:
            board[index] = "x"