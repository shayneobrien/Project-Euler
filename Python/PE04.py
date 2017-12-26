# PE Problem 4
# A palindromic number reads the same both ways. 
# Find the largest palindrome made from the product of two 3-digit numbers.

palprod = 0 # initialize counter as zero
for x in xrange(999,100,-1): # count backwards since we are looking for largest prod (reduces if checks)
    for y in xrange(x,100,-1): # loop for checking all numbers
        z = x * y # multiply numbers
        if z > palprod: # only care about larger products
            check = str(z) # convert to string
            if check == check[::-1]: #if all entries of the string check are the same forwards as backwards: 
                palprod = z # initialize new answer
                
print palprod # print answer
