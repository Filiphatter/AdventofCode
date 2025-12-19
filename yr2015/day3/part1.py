f = open('input.txt', 'r')
text = f.read()
f.close()

# He begins by delivering a present to the house at his starting location, 
# and then an elf at the North Pole calls him via radio and tells him where to move next. 
# Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, 
# he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off,
# and Santa ends up visiting some houses more than once. How many houses receive at least one present?

x, y = 0, 0
visited = set()
visited.add((x, y)) #start position, set will add cords but not overwrite, basically a list of cords
directions = text

for move in directions:
    if move == "^":
        y += 1
    elif move == "v":
        y -= 1
    elif move == ">":
        x += 1
    elif move == "<":
        x -= 1

    visited.add((x, y))

    Houses = len(visited)
    print(Houses)