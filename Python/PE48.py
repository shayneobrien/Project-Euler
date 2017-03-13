# PE Problem 48
# Find the last ten digits of the series 1^1+2^2+3^3+...+1000^1000

count = sum(x**x for x in xrange(1,1001)) # compute sum
print str(count)[-10:] # print last 10 digits