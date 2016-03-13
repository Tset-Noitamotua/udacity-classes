import math

#f = math.factorial(5)
#print f

t = [str(i) + ',' + str(j) for i in range(5) for j in range(3)]
print t

for x in (str(i) + ',' + str(j) for i in range(5) for j in range(3)):
    print x

