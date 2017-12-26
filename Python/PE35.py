from tqdm import tqdm

def rotate_prime(prime):
    """ Take integer prime as input, turn into string, put first digit at the end and return string """
    prime = str(prime)
    rotated_prime = prime + prime[0]
    return rotated_prime[1:]

def rwh_primes2(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

primes_under_1e6 = rwh_primes2(int(1e6))
counter = 0
for prime in tqdm(primes_under_1e6):
    original = str(prime)
    rotated_prime = rotate_prime(prime)
    add_one = True
    while rotated_prime != original:
        if int(rotated_prime) not in primes_under_1e6:
            add_one = False
            break
        else:
            rotated_prime = rotate_prime(rotated_prime)

    if add_one:
        counter += 1
        
print 'The number of circular primes under one million is {0}'.format(counter)
