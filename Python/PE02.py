# PE Problem 2
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

def fibbosum():
    a = 1 # initialize first term of fibonacci
    b = 1 # initialize second term of fibonacci
    c = 0 # initialize our c term
    sum = 0 # initialize sum counter
    while c < 4e6: # until we hit 4 million
        c = a + b # let c be the sum a+b
        a = b # set a as b 
        b = c #  set b as c (by doing this, we are moving along the sequence)
        if not c % 2: # if no remainder for c divided by 2
            sum += c # increase sum by c
    
    return sum # return sum to global variables
    
print sum

