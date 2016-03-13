# HW3-4 Version 1
# 
# Implement the Rabin Miller test for primality
#

#from hw3_4_util import mod_exp
from random import randrange

def rabin_miller(n, target=128):
    """returns True if prob(`n` is composite) <= 2**(-`target`)"""
    def calculate_t(n):
        # n = 2**t * s + 1
        n = n - 1
        t = 0
        while n % 2 == 0:
            n = n / 2
            t += 1
        return t
    if n % 2 == 0:
        return False
    t = calculate_t(n)
    s = (n - 1) / (2 ** t)
    
    n_tests = target / 2
    tried = set()
    if n_tests > n:
        raise Exception('n is too small')
    for i in range(n_tests):
        while(True):
            a = randrange(1, n)
            if a not in tried:
                break
            tried.add(a)
        if mod_exp(a, s, n) == 1:
            continue
        found = False
        for j in range(0, t):
            if mod_exp(a, 2**j*s, n) == (n - 1):
                found = True
                break
        if not found:
            return False
    return True

def mod_exp(a, b, q):
    """returns a**b % q"""
    def square(x): return x*x
    if b == 0: return 1
    if b % 2 == 0: return square(mod_exp(a, b / 2, q)) % q
    else: return square(mod_exp(a, b - 1, q)) % q

rabin_miller(1023)