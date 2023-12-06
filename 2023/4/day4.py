# Scratchers

# Each line is a list of winnings numbers | numbers you have
# Points is doubled for each winning number match

def main():
    f = "input2.txt"
    fileContents = getFileContents(f)

    totalPoints = 0

    # Do this for each lines
    for line in fileContents:
        a = line.split(": ")
        b = a[1].split(" | ")
        winningNumbers = b[0].split(" ")
        myNumbers = b[1].split(" ")

        winningNumbers = removeBlanks(winningNumbers)
        myNumbers = removeBlanks(myNumbers)

        matches = getPoints(winningNumbers, myNumbers)
        totalPoints += getFinalPoints(matches)
        #print("Matches: " + str(matches))
        #print("Points: " + str(getFinalPoints(matches)))

    print("Total points: " + str(totalPoints))

def getFinalPoints(n):
    if( n <= 0):
        return 0
    return pow(2, n - 1)

def getPoints(winningNumbers, myNumbers):
    points = 0
    for myN in myNumbers:
        if( myN in winningNumbers):
            points += 1
    return points

def getDoublePoints(winningNumbers, myNumbers):
    points = 0
    for i in winningNumbers:
        if i in myNumbers:
            points += 2
    return points

def removeBlanks(s):
    while "" in s:
        s.remove("")
    return s

def getFileContents(fileName):
    with open(fileName, "r") as f:
        data = f.read()
    
    lines = data.split("\n")

    # Now close file
    f.close()

    return lines

if __name__ == "__main__":
    main()

