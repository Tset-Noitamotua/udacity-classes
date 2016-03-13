def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        print x, y, z
        z = z + y
        x = x - 1
    return z

naive(63, 12)