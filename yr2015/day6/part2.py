f = open('input.txt', 'r')
text = f.read()
f.close()

# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.
# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

# The phrase turn on actually means that you should increase the brightness of those lights by 1.

# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

# The phrase toggle actually means that you should increase the brightness of those lights by 2.

# What is the total brightness of all lights combined after following Santa's instructions?

# For example:
# turn on 0,0 through 0,0 would increase the total brightness by 1.
# toggle 0,0 through 999,999 would increase the total brightness by 2000000.

directions = text.splitlines()

grid = [[False] * 1000 for _ in range(1000)]

for move in directions:
    parts = move.split()
    if 'on' in parts:
        x1, y1 = map(int, parts[2].split(','))
        x2, y2 = map(int, parts[4].split(','))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] += 1

    elif 'off' in parts:
        x1, y1 = map(int, parts[2].split(','))
        x2, y2 = map(int, parts[4].split(','))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if grid[x][y] == 0:
                    grid[x][y]
                    
                elif grid[x][y] >= 1:
                    grid[x][y] -= 1

    elif 'toggle' in parts:
        x1, y1 = map(int, parts[1].split(','))
        x2, y2 = map(int, parts[3].split(','))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] += 2
                             
    lightness = 0
    for row in grid:
        lightness += sum(row)

print(lightness)