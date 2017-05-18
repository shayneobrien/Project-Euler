# PE Problem 34
# Find the sum of all numbers which are equal to the sum of the factorial of their digits

def fact(n): # simple factorial function
    if n <= 0:
        return 1 # base case as well as stop point for recursion
    else:
        return n * fact(n-1) # recursion

count = 0 # running total
for i in xrange(3,99999): # for all numbers from 3 to 99,999
    w = str(i) # convert i to string, store in w
    add = 0 # add is our counter for digits factorial sum
    for j in w: # for all digits in i
        add += fact(int(j)) # add the factorial of each digit up
    if i == add: # if the digit is equal to the sum of the factorial of its digits
        count += i # increment count by i

print count # print answer