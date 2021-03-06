# In this example, we repeat large part of our script using while loop.
# To exit the loop we use break command.

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

while True:
    firstRow = " " + cell0 + separator + cell1 + separator + cell2 + "\n"
    secondRow = " " + cell3 + separator + cell4 + separator + cell5 + "\n"
    thirdRow = " " + cell6 + separator + cell7 + separator + cell8

    print( firstRow + horizontalLine + secondRow + horizontalLine + thirdRow )

    index = raw_input( "Enter a cell index or 'q' to exit..." )

    if index == "q":
        break
    elif index == "0":
        cell0 = "x"
    elif index == "1":
        cell1 = "x"
    elif index == "2":
        cell2 = "x"
    elif index == "3":
        cell3 = "x"
    elif index == "4":
        cell4 = "x"
    elif index == "5":
        cell5 = "x"
    elif index == "6":
        cell6 = "x"
    elif index == "7":
        cell7 = "x"
    elif index == "8":
        cell8 = "x"
    else:
        print( "Wrong index!\n" )