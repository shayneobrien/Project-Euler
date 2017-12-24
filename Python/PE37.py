import numpy as np

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True

truncatable_primes = []
current_number = 739395
while len(truncatable_primes) < 11:
    if not is_prime_number(current_number):
        current_number += 1
    else:
        potential_truncatable = str(current_number)
        permutations_right = [potential_truncatable[i:] for i in xrange(len(potential_truncatable))]
        permutations_left  = [potential_truncatable[:i] for i in xrange(1, len(potential_truncatable)+1)]
        right_eval = [is_prime_number(int(number)) for number in permutations_right]
        left_eval  = [is_prime_number(int(number)) for number in permutations_left]
        if (np.all(right_eval) and np.all(left_eval)):
            truncatable_primes.append(int(potential_truncatable))
            print potential_truncatable
        current_number += 1

    if current_number % 10000 == 0:
        print 'Current number: {0} | No. truncatable primes so far: {1}'.format(current_number, len(truncatable_primes))

print 'The sum of the only eleven primes that are both truncatable from left to right and right to left is: {}'.format(sum(truncatable_primes))
