# PE Problem 10
# Find the sum of all primes under two million



def sieve(n):
    # n is how many primes we want to find
    odds = range(3,n+1,2) # compute all odds, since evens aren't prime
    sieve = set(sum([range(x*x,n+1,2*x) for x in odds],[])) # let sieve be an object, where we 
    # find the sum of the list containing the arithmetic progression of integers such that
    # we start at x*x, where x is odd, and go by increments of 2*x until we hit n
    # basically what this does is enumerate all odds until n, and enumerate all multiples of those odds until n.
    return [2] + [x for x in odds if x not in sieve] # if it's in odds but not in sieve, it is prime

print sum(sieve(2000000))
# might be sped up a lot by breaking it into intervals.