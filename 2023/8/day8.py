# Mapping class
class Mapping:
    def __init__(self, s):
        self.c, leftRight = s.split("=")
        self.c = self.c.strip()
        self.left  = leftRight.split(",")[0].strip()[1:]
        self.right = leftRight.split(",")[1].strip()[:-1]

# Dictionary mapping a string to a Mapping object
mappings = {}

# List of all mappings
allMappings = []

# Read in file
fileName = "input2.txt"
f = open(fileName, "r")

instructions, mapping = f.read().split("\n\n")

# Loop through mapping and add to mappings dictionary
for line in mapping.split("\n"):
    allMappings.append(Mapping(line))

# Loop through each item in allMappings and map to the mappings dictionary
for m in allMappings:
    mappings[m.c] = m

# Apply instructions
current = "AAA"
i = 0
while current != "ZZZ":
    step = i % len(instructions)
    if instructions[step] == "L":
        current = mappings[current].left
    elif instructions[step] == "R":
        current = mappings[current].right
    i += 1

print("Part 1 took: " + str(i) + " instructions")