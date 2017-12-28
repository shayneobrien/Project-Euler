
# coding: utf-8

# In[30]:


""" How many, not necessarily distinct, values of nCr, for 1 ≤ n ≤ 100, are greater than one-million? """

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
    
def nCr(n, r):
    if r > n:
        raise RuntimeError(': maximum recursion depth exceeded')
    else:
        return factorial(n)/(factorial(r)*factorial(n-r))

counter = 0
for n in xrange(1, 101):
    for r in xrange(1, n-1):
        if nCr(n, r) > int(1e6):
            counter += 1
            
print 'The number of, not necessarily distinct, values of nCr, for 1 ≤ n ≤ 100, are greater than one-million is {0}'.format(counter)


# In[29]:


counter

