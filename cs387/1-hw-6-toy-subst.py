import math

keyspace = math.factorial(26)
n = 1
while 26 ** n < keyspace:
    n += 1
print 'N is', n