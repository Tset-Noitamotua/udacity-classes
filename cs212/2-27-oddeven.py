def oddeven():
    for a in range(1, 10):
        for b in range(0, 10):
            odd = a * 100 + b * 10 + b
            even = 2 * odd
            if odd % 2 == 1 and even % 2 == 0 and even > 999:
                t0 = even / 1000 * 1000
                t1 = (even - t0) / 100 * 100
                t2 = (even - t0 - t1) / 10 * 10
                t3 = even - t0 - t1 - t2
                e0, e1, e2, e3 = t0 / 1000, t1 / 100, t2 / 10, t3
                if e0 == e2 and e0 != e1 and e1 != e3:
                    print '%d + %d = %d' % (odd, odd, even)

oddeven()