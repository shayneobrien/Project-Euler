
# coding: utf-8

# In[14]:


# Find the next triangle number that is also pentagonal and hexagonal.

triangle_numbers = [(x*(x+1))/2 for x in range(100000)]
pentagonal_numbers = [(x*(3*x-1))/2 for x in range(100000)]
hexagonal_numbers = [x*(2*x-1) for x in range(100000)]

set(triangle_numbers).intersection(pentagonal_numbers, hexagonal_numbers)

