f = open('input.txt', 'r')
text = f.read()
f.close()

# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.
# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), 
# then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

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