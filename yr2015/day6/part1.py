f = open('input.txt', 'r')
text = f.read()
f.close()

# Because your neighbors keep defeating you in the holiday house decorating contest year after year, 
# you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. 
# The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. 
# Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 
# therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?



directions = text.splitlines()

grid = [[False] * 1000 for _ in range(1000)]

for move in directions:
    parts = move.split()
    if 'on' in parts:
        x1, y1 = map(int, parts[2].split(','))
        x2, y2 = map(int, parts[4].split(','))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] = True

    elif 'off' in parts:
        x1, y1 = map(int, parts[2].split(','))
        x2, y2 = map(int, parts[4].split(','))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] = False

    elif 'toggle' in parts:
        x1, y1 = map(int, parts[1].split(','))
        x2, y2 = map(int, parts[3].split(','))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] = not grid[x][y]
                             
    amountOfTrue = 0
    for row in grid:
        amountOfTrue += sum(row)

print(amountOfTrue)