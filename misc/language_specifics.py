import sys
import time
a_list = [1, 2, 3, 4, 4, 5, 6, 7]
print a_list  # [1, 2, 3, 4, 4, 5, 6, 7]

# map: map a function to a list or set, for each element in the container
# map: returns a list
# lambda: anonymous functions, on the fly
b_list = map(lambda i: i + 3, a_list)
print b_list  # [4, 5, 6, 7, 7, 8, 9, 10]

# filter: apply rule to element
# filter: returns a list
c_list = filter(lambda x: x % 2 == 0, b_list)
print c_list  # [4, 6, 8, 10]

d_list = map(lambda x: x % 2 == 0, a_list)
print d_list  # [False, True, False, True, True, False, True, False]


# reduce: apply function to two arguments and
# reduce: returns a single value
summation = reduce(lambda a, b: a + b, a_list)  # equivalent to sum(a_list)
product = reduce(lambda a, b: a * b, a_list)
smallest = reduce(lambda a, b: a if a < b else b, a_list)
biggest = reduce(lambda a, b: a if a > b else b, a_list)

print 'Summation is: %d' % summation
print 'Product is %d' % product
print 'Smallest is %d' % smallest
print 'Biggest %d' % biggest


# generators
cap_stone = 100000

odds = (i for i in xrange(cap_stone) if i % 2 != 0)
print 'size of odds generator: %d ' % sys.getsizeof(odds)

odds_list = [i for i in xrange(cap_stone) if i % 2 != 0]
print 'size of odds list: %d ' % sys.getsizeof(odds_list)

# benchmark for summation of a list and a generator
start_time = time.time()
print 'summation of using no generators %d, is %d  ' % (cap_stone, reduce(lambda a, b: a + b, odds_list))
print("--- %s seconds for list ---" % (time.time() - start_time))

start_time = time.time()
print 'summation of using generators %d, is %d  ' % (cap_stone, reduce(lambda a, b: a + b, odds))
print("--- %s seconds for generator ---" % (time.time() - start_time))


# comprehensions
# the alphabet backwards
comp_list = [chr(122 - i) for i in xrange(26)]
comp_dict = {chr(i + 97): i + 97 for i in xrange(26)}

print comp_list
print comp_dict

print 7/2.0  # decimal value
print 19//2.0  # how many times the denominator goes in the numerator

# strings
# strings are immutable, cast to list to modify them
#
t_string = 'Hello World'
t_string += ' and people'
print t_string
