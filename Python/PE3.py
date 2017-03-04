# PE Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
def primefind(n):
    i = 2 # first prime
    while i * i < n: # until it is a square
        while n % i == 0: # while the modulus gives you a zero
            n = n/i # divide n by i
        i += 1 # increment i by 1
    print n
    
primefind(600851475143)
primefind(100)