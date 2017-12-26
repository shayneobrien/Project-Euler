# PE Problem 6
# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.

a = sum(xrange(1,101)) # sum
print  a * a - sum(x*x for x in range(1,101)) # sum of squares minus square of the sum
