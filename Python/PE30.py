# PE Problem 30
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits

# why is it double counting?
runtotal = 0 # for tracking sums
i = 10 # 10 since 2:9 cannot be written as sums the fifth powers of themself
while i < 250000: # run through numbers
    k = 0 # set k as 0
    b = str(i) # convert our i-th number to string
    for j in xrange(len(b)): # for all digits in the string
        w = int(b[j]) # convert digit to integer
        k += w**5 # add 5th power of digit to k
    if k == int(b): # if k is the same as our digit,
        runtotal += k # increment runtotal by k
    i += 1 # move to next number

print runtotal # print answer