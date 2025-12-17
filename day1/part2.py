f = open('input.txt', 'r')
input = f.read()
f.close()

# Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). 
# The first character in the instructions has position 1, the second character has position 2, and so on.

# For example:
# ) causes him to enter the basement at character position 1.
# ()()) causes him to enter the basement at character position 5.
# What is the position of the character that causes Santa to first enter the basement?

i = 0  #position
steps = 0 #total positions
plus = "(" #if bracket ( +1 in i
minus = ")" #if bracket ) -1 in i 
for k in input:
   if i == -1 : break
   
   elif k == plus: i = i + 1; steps = steps + 1

   else: i = i - 1; steps = steps + 1

print(i)
print(steps)