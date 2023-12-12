# --- Day 10: Pipe Maze ---

'''
The pipes are arranged in a two-dimensional grid of tiles:
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, 
        but your sketch doesn't show what shape the pipe has.
'''
# Read in file
fileName = "input.txt"
f = open(fileName, "r")

grid = f.read().split()
graph = {}
for x, line in enumerate(grid):
    for y, tile in enumerate(line):
        adjacent = []
        if tile in '-J7S':
            adjacent.append((x, y-1))
        if tile in '-FLS':
            adjacent.append((x, y+1))
        if tile in '|F7S':
            adjacent.append((x+1, y))      
        if tile in '|LJS':
            adjacent.append((x-1, y))
        if tile == 'S':
            visited = set([(x, y)])
            q = set([(x, y)])
        graph[(x, y)] = adjacent

steps = -1
while q:
    nxt = set()
    for x1, y1 in q:
        for x2, y2 in graph[(x1, y1)]:
            if (x2, y2) not in visited and (x1, y1) in graph.get((x2, y2), []): 
                nxt.add((x2, y2))
                visited.add((x2, y2))
    q = nxt
    steps += 1

print(steps)