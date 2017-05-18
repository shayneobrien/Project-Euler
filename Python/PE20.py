# PE problem 20
# Sum of the digits in the number 100!

def fact(n):
    if n <= 0:
        return 1 # base case as well as stop point for recursion
    else:
        return n * fact(n-1) # recursion
        
sum = 0
for i in str(fact(100)):
    sum += int(i)

print sum