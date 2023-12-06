# --- Day 5: If You Give A Seed A Fertilizer ---

# Each line is a list of winnings numbers | numbers you have
# Points is doubled for each winning number match

def main():
    f = "input.txt"
    fileContents = getFileContents(f)

    totalPoints = 0

    # Do this for each lines
    for line in fileContents:
        a = line.split(": ")

    print("Total points: " + str(totalPoints))

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

