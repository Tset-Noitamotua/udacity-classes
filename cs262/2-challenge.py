# Bonus Practice: Find Max

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Given a list l and a function f, return the element of l that maximizes f.

# Assume:
#    l is not empty
#    f returns a number

# Example:

l = ['Barbara', 'kingsolver', 'wrote', 'The', 'Poisonwood','Bible']
f = len

def findmaxl(l):
    s = sorted(l, key=lambda(word): word.find('l'))
    return s[-1]

def findmax(f, l):
    s = sorted(l, key=f)
    return s[-1]

print findmax(f, l)
print findmaxl(l)

