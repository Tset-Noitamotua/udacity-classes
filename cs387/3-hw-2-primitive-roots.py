# HW3-2 Version 1
#
# Define a procedure primitive_roots 
# that takes as input a small prime number
# and returns all the primitive roots of that number
#

#from hw3_2_util import mod_exp

def primitive_roots(n):
    """Returns all the primitive_roots of `n`"""
    roots = []
    def is_primitive_root(r):
        s = set()
        for i in range(1, n):
            t = mod_exp(r, i, n)
            if t in s:
                return False
            s.add(t)
        return True
    for i in range(2, n):
        if is_primitive_root(i):
            roots.append(i)
    return roots

def mod_exp(a, b, q):
    """returns a**b % q"""
    def square(x): return x*x
    if b == 0: return 1
    if b % 2 == 0: return square(mod_exp(a, b / 2, q)) % q
    else: return square(mod_exp(a, b - 1, q)) % q

def test():
    assert primitive_roots(3) == [2]
    assert primitive_roots(5) == [2, 3]
    print "tests pass"

test()