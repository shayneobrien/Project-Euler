# PE Problem 29
# How many distinct terms are in the sequence generated by a^b for 2<=a<=100, 2<=b<=100?

z = [] # empty list for holding
for a in xrange(2,101): # for all a in [2,100]
    for b in xrange(2,101): # for all b in [2,100]
        y = a**b # let y = a^b
        if y not in z: # if y is not already in z,
            z.append(y) # append it

print len(z) # print length of z, which is our answer