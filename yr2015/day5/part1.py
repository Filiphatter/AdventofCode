f = open('input.txt', 'r')
text = f.readlines()
f.close()

# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:

# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
# How many strings are nice?

vowels = "aieou"
goodstring = 0

def findvowels(text):
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count >= 3

def oneletterappeartwice(text):
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            return True
    return False
    
def ifStringincludes(text):
    # illegalarg1 = "ab"
    # illegalarg2 = "cd"
    # illegalarg3 = "pq"
    # illegalarg4 = "xy"
    for bad in ("ab", "cd", "pq", "xy"):
        if bad in text:
            return False
    return True
            
def is_nice(text):
    if findvowels(text) and oneletterappeartwice(text) and ifStringincludes(text):
        return True
    return False

for lines in text:
    if is_nice(lines):
        goodstring +=1

print(goodstring)