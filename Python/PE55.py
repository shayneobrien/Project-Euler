
# coding: utf-8

# In[114]:


""" How many Lychrel numbers are there below ten-thousand? """

def is_lychrel(number):
    number = str(number)
    for _ in xrange(0,50):
        number = str(int(number) + int(number[::-1]))
        if number == number[::-1]:
            return False
    return True

print 'The number of Lychrel numbers below 10,000 is {0}'.format(sum(1 for number in xrange(10000) if is_lychrel(number)))

