"""Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum? """

print max([sum(int(num) for num in str(a**b)) for a in xrange(100) for b in xrange(100)])
