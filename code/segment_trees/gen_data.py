import sys
import random

n = int(sys.argv[1]) # num. leaves
m = int(sys.argv[2]) # num. queries

print n
for i in xrange(0, n):
    print random.randint(0, 1000)
print m
for i in xrange(0, m):
    lo = random.randint(0, n)
    hi = random.randint(0, n)
    min = lo
    max = hi
    if min > max:
        print max,
        print min
    else:
        print min,
        print max
