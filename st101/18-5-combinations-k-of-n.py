import math

# binomial distribution

n = 12
k = 9
p = 0.8 # probability of outcome

fn  = math.factorial(n)
fnk = math.factorial(n - k)
fk  = math.factorial(k)

combinations = fn / (fnk * fk)
outcomes = 2 ** n

print 'combinations:', combinations

pOneCase = (p ** k) * ((1 - p) ** (n - k))
pAllCases = combinations * pOneCase

print 'probability:', pAllCases
