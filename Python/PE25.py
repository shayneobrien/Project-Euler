# PE Problem 25
# What is the index of the first time in the Fibonacci sequence to contain over 1000 digits?


a = 1 # initialize first term of fibonacci
b = 1 # initialize second term of fibonacci
c = 0 # initialize our c term
length = 0 # initialize sum counter
counter = 2
while length < 1000: # until we hit 4 million
    c = a + b # let c be the sum a+b
    a = b # set a as b 
    b = c #  set b as c (by doing this, we are moving along the sequence)
    counter += 1 # increment counter by 1
    length = len(str(c)) # check how many digits our current term has

print counter    