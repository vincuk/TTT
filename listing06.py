# Print the game board (using for loop)

horizontalLine = "-----------"
separator = " | "

for rowIndex in range(3):
    rowString = " "
    for columnIndex in range(3):
        rowString += str( columnIndex + 3*rowIndex ) 
        if columnIndex < 2:
            rowString += separator
    print( rowString )
    if rowIndex < 2:
        print( horizontalLine )