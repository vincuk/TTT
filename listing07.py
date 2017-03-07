# Is it possible to avoid creation of nine variables 
#   with different names in our model?
# Yes, of course! And in this example, we create one list variable
#   for our model.

board = [" "] * 9
#board = map( str, range(9) )

horizontalLine = "-" * 11
separator = " | "

for rowIndex in range(3):
    rowString = " "
    for columnIndex in range(3):
        rowString += board[columnIndex + 3*rowIndex]
        if columnIndex < 2:
            rowString += separator
    print( rowString )
    if rowIndex < 2:
        print( horizontalLine )