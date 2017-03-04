# PE Problem 14
# It is thought Collatz sequences always go to 1
# 
# Which starting number, under one million, produces the longest chain?
import time  # for time
start = time.time()

y = 0 # initialize holder for starting number
maximum = 0 # initalize maximum
for i in xrange(1,1000001): # from 1 to one million
    counter = 0 # set a counter for steps
    z = i # let z be i
    while z != 1: # until we get to 1
        if z % 2 == 0: # if even, divide by 2
            z /= 2
        else: # otherwise it's odd, so multiply by 3 and add 1
            z = 3*z + 1
        counter += 1 # increment counter
        
    if counter > maximum: # if our counter is higher than the max
        y = i # save the starting number
        maximum = counter # re-write counter

print y

end = time.time() 
print end-start # print time