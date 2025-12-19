f = open('input.txt', 'r')
input = f.readlines()
f.close()

# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: 
# find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

# For example:
# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

def Areacalculator(length, width, height):
    area1 =  length * width
    area2 =  width * height
    area3 =  height * length

    fullArea = 2 * (area1 + area2 + area3)
    smallestSide = min(area1, area2, area3)

    totalSquareFeet = fullArea + smallestSide
    # print(f"fullArea {fullArea}")
    # print(f"totalSquareFeet {totalSquareFeet}")
    return totalSquareFeet

total = 0
    
for line in input:
    length, width, height = map(int, line.strip().split("x")) #split x = '24' '25' '17' ---- map convert str to int ---- strip to remove whitespaces and goes into variables
    total += Areacalculator(length, width, height) #varibles into total in the areacalclator
    
print(total)
