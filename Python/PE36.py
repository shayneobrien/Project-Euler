# PE Problem 36
# Find the sum of all numbers < 1e6 which are palindromic in base 10 and base 2.

def palindrome(a):
    a = str(a) # convert to string
    forward = a[:(len(a)/2)] # see first half, minus middle letter
    backward = [] # let backward be an empty list
    if len(a) % 2 != 0: # for odds
        for i in xrange(len(a)-1, len(a)/2, -1): # going backward until mid letter
            backward.append(a[i]) # append the letters
    else: # for evens
        for i in xrange(len(a)-1,len(a)/2 -1, -1):
            backward.append(a[i])
    backward = ''.join(backward) # concatenate list
    if (forward) == (backward): # check if it's a palindrome
        return True # yield it if it is
    else: # otherwise
        return False # return false
    
count = 0 # initialize count as 0
for i in xrange(1,1000000): # for 1 to 1 million
    if (palindrome(bin(i)[2:]) == True) & (palindrome(str(i)) == True): # if both bases are palindromes
        count += i #increment count by i
    
    
    