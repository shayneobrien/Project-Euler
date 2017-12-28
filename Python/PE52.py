"""It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits."""

number = 10
product_range = range(2, 7)
while True:
    product_list = [int(number*product) for product in product_range]
    str_list = [sorted(str(entry)) for entry in product_list]
    if str_list.count(str_list[0]) == len(str_list):
        print 'The smallest positive integer x such that 2x, 3x, 4x, 5x, and 6x contain the same digits is: {0}'.format(number)
        break
    else:
        number += 1
