# PE Problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find a*b*c

# we want a + b + c = 1000. then c = 1000 - a - b.

for a in xrange(1,501): # for all values a from 1 to 500 (since we don't want negative c)
    for b in xrange(1,501): # for all values b from 1 to 500 
        c = 1000 - a - b # let c = 1000 - a - b
        if c*c == (a*a + b*b): # if c^2 = a^2+b^2
            answer = a*b*c
            break

print answer