import math
n = 2
b = 100 / math.log(1.1)
while n / math.log(n) < b:
    n += 1
print n