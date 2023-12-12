# Read in file
fileName = "input2.txt"
f = open(fileName, "r")

instructions, mapping = f.read().split("\n\n")