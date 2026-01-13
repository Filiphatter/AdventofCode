# Now find one that starts with six zeroes.

from hashlib import md5 #imports md5 hashing
key = 'ckczppom' #Key to hash

for i in range(5000000): #generates i up to 5m 
    encodedInput = md5((key + str(i)).encode()).hexdigest() #key + str(i) generates strings with n+1 each iteration. Encode, encodes the string to a byte, hexdigest converts it into a 32byte string
    if encodedInput.startswith('000000'): #if first 6 digits is 000000 it prints which iteration for the solution
        print(i)
        break

    # base is not mine as said in p1. But solved this one solo