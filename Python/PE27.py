
# coding: utf-8

# In[ ]:


# Find the product of the coefficients, a and b, for the quadratic expression that produces the 
# maximum number of primes for consecutive values of n, starting with n=0.
def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True


f = lambda n: n*n + a*n + b
results_tuple = (0, 0, 0)

for a in xrange(-1000, 1001):
    for b in xrange(max(2,1-a), 1001):
        index, current_count = 0, 0
        while is_prime_number(f(index)):
            current_count += 1
            index += 1
        if results_tuple[2] < current_count:
            results_tuple = (a, b, current_count)
            
print 'The maximum number of primes for consecutive values of n, starting with n=0, is: {0}'.format(results_tuple[2])
print 'We get this when a = {0}, b = {1}. Their product is {2}'.format(results_tuple[0], results_tuple[1], results_tuple[0]*results_tuple[1])

