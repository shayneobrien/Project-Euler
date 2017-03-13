# what is the sum of the digits of the number 2^1000?

w = sum([int(y) for y in str(2**1000)]) # convert 2^1000 to string, convert each character to int, sum ints
print w # print answer
