import random
from math import sqrt

def mean(data):
    return sum(data)/len(data)

def variance(data):
    mu=mean(data)
    return sum([(x-mu)**2 for x in data])/len(data)

def stddev(data):
    return sqrt(variance(data))

def confidence(data):
    m = mean(data)
    v = variance(data)
    c = 1.96 * sqrt(v / len(data))
    print 'mean: %f, variance: %f, confidence: +/- %f' % (m, v, c)

def calc(heads, tails):
    data = [1.0] * heads + [0.0] * tails
    confidence(data)

calc(600, 400)