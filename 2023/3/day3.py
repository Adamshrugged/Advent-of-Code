# Gear Ratios

# Add up all the part numbers
# Any number adjacent to a symbol (even diagonally) is a part number

# Given the starting x, y of a number, check adjacent and see if it has a symbol nearby
def isNumberAdjacentToSymbol(matrix, x, y, length):
    # Iterate through matrix starting with 1 less than provided x and y
    i = x - 1
    j = y - length - 1
    while i < x + length:
        while j < y + 1:
            if( i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) ):
                pass
                #print("Out of bounds")
            # Check if position is neither a digit or a .
            elif( matrix[i][j] != "." ):
                #print("Checking i: " + str(i) + ". Max I: " + str(len(matrix)))
                #print("Checking j: " + str(j) + ". Max J: " + str(len(matrix[0])))
                if( not( matrix[i][j].isdigit() ) ):
                    return True
            j += 1
        i += 1
        j = y - length - 1
    # If no symbols are found, then false
    return False

# List of numbers
numbers = []

# Read in file
filename = "input.txt"
with open(filename, "r") as f:
    data = f.read()

    # read in each line of file
    lines = data.split("\n")

    # Create 2d matrix of input
    matrix = []
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        # Add a buffer at end of row to prevent edge cases
        row.append(".")
        matrix.append(row)

    # Iterate through the grid
    for i in range(len(matrix)):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j].isdigit():
                newNum = int(matrix[i][j])
                startX = i
                startY = j
                # Read in next number until the end is reached
                while( matrix[i][j+1].isdigit() ):
                    j += 1
                    newNum = newNum * 10 + int(matrix[i][j])
                j += 1
                # Check if number is adjacent to a symbol, if so add it
                if isNumberAdjacentToSymbol(matrix, i, j, len(str(newNum))):
                    numbers.append(newNum)
                    print("Adding " + str(newNum))
            j += 1

print("Final sum: " + str(sum(numbers)))

# Now close file
f.close()