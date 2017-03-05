# PE Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# Smallest positive number evenly divisible from 0 to 20?

################# ATTEMPT 1: SUCCESSFUL, BUT IN ~18 SECONDS################
# We have 0,1,2,3,4,5,6,7,8,9,10
#         11,12,13,14,15,16,17,18,19,20
# multiples of 20 are always multiples of 10,4,5,and 2 ---> check 20, get 2,4,5,10
# multiples of 18 are always multiples of 2,3,6,9      ---> check 18, get 3,6,9
# multiples of 16 are 2,8                              ---> check 16, get 8
# multiples of 14 are always multiples of 2,7          ---> check 14, get 7
# so far we have 2,3,4,5,6,7,8,9,10 by checking 20,18,16,14. Need 19,17,15,13,12,11

import time
start = time.time()
i = 2520 # start at 2520, since we know it's divisible by all 1 through 10
list = range(19,10,-1) # based on above logic, go backwards since it eliminates quicker
                       # we increment by 20, so don't need to check 20.
k = 0
while k != 1:
    if all(i % x == 0 for x in list):
        print i
        k += 1
        break
    else:
        i += 20 
end = time.time()
print end-start

# can also do with gcd, lcd... or finding prime factorization of each number 1-20 and multiplying?