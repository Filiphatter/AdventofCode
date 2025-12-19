f = open('input.txt', 'r')
input = f.readlines()
f.close()

# #The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well;
#  the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

# For example:
# A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
# A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
# How many total feet of ribbon should they order?

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
    
def ribbonCalculator(length, width, height):
    sides = sorted([length, width, height]) #sort to get smallest sides
    perimeter = 2 * (sides[0] + sides[1]) # proceed math
    bow = length * width * height # add together for bow
    return perimeter + bow ##add bow + smallest sides

totalRibbon = 0

for line in input:
    length, width, height = map(int, line.strip().split("x"))
    totalRibbon += ribbonCalculator(length, width, height)

print(totalRibbon)
