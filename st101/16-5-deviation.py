#Complete the stddev function to make it return the standard deviation 
#of a list of numbers
from math import sqrt

data3=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]


def mean(data):
    return sum(data)/len(data)

def variance(data):
    mu=mean(data)
    return mean([(x-mu)**2 for x in data])

def stddev(data):
    return sqrt(variance(data))

print stddev(data3)