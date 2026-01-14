f = open('input.txt', 'r')
text = f.readlines()
f.close()

#Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
# For example:

# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
# How many strings are nice under these new rules?
import re

goodstring = 0

def hasPairTwice(text):
    pairs = {}

    for i in range(len(text) - 1):
        pair = text[i:i+2] #finding pair
        if pair in pairs:
            if i - pairs[pair] >= 2:  # non-overlapping pairs
                return True
        else:
            pairs[pair] = i

    return False

def letterSpaceLetter(text):
    for i in range(len(text) - 2):
        if text[i] == text[i + 2]:
            return True
    return False
    
            
def is_nice(text):
    if hasPairTwice(text) and letterSpaceLetter(text):
        return True
    return False

for lines in text:
    if is_nice(lines):
        goodstring +=1

print(goodstring)