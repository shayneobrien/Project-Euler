# PE Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples3or5(): # define function
    for number in xrange(1000): # for all integers from 0 to 999:
        if not number % 3 or not number % 5: # if (number % 3,5) is true, then number is a multiple 
            yield number # therefore yield it to be summed (added to sequence)

print sum(multiples3or5()) # print the sum of the function
