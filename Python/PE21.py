# PE Problem 21
# Sum of all amicable numbers under 10000

def divisors(n): # function to determine divisors of a number n
    return list(i for i in xrange(1, n/2 + 1) if n % i == 0)
    
count = 0 # initialize our running total as zero
for a in xrange(10000): # for 1 to 10000
    b = sum(divisors(a)) # d(a) = b
    k = sum(divisors(b)) # d(b) = k --> is k == a?
    if (k == a) & (b != a): # if so and b != a (as per prompt)
        count += a # increment count by a

print count # print ans