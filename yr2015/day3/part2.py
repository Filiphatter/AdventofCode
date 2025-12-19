f = open('input.txt', 'r')
text = f.read()
f.close()

# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.
# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), 
# then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

sx, sy = 0, 0 #reg santa location
rx, ry = 0, 0 #robo santa location
visited = set() #list for locations, no dupes
visited.add((sx, sy)) #start position, set will add cords but not overwrite, basically a list of cords
directions = text #takes text input as directions

def moveSanta(x, y, move): #could prov be inline with enumerate function
        if move == "^":
            y += 1
            return x, y
        elif move == "v":
            y -= 1
            return x, y
        elif move == ">":
            x += 1
            return x, y
        elif move == "<":
            x -= 1
            return x, y
            
for i, move in enumerate(directions): #enumerate is basically for i = 0; i<10; i++, a way of keeping count of which santa should move.
    if i % 2 == 0:  # Santa
        sx, sy = moveSanta(sx, sy, move)
        visited.add((sx, sy))
    else:  # Robo-Santa
        rx, ry = moveSanta(rx, ry, move)
        visited.add((rx, ry))

print(len(visited))