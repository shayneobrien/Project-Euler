# PE Problem 40
# An irrational decimal fraction is created by concatenating the positive integers
# What if dn is the nth digit of the fractional part, what is
# d1*d10*d100*d1000*d10000*d100000*d1000000?
import time as time
start = time.time()
w = []
for j in xrange(1,1000001):
    j = str(j)
    for k in xrange(len(j)):
        w.append(j[k])

print int(w[1-1])*int(w[10-1])*int(w[100-1])*int(w[1000-1])*int(w[10000-1])*int(w[100000-1])*int(w[1000000-1])
end = time.time()
print end-start

            