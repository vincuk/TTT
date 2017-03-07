# Model of the game board

horizontalLine = "-----------\n"
separator = " | "

cell0 = "0"
cell1 = "1"
cell2 = "2"
cell3 = "3"
cell4 = "4"
cell5 = "5"
cell6 = "6"
cell7 = "7"
cell8 = "8"

firstRow = " " + cell0 + separator + cell1 + separator + cell2 + "\n"
secondRow = " " + cell3 + separator + cell4 + separator + cell5 + "\n"
thirdRow = " " + cell6 + separator + cell7 + separator + cell8

print( firstRow + horizontalLine + secondRow + horizontalLine + thirdRow )