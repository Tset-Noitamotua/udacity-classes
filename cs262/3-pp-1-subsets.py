def permute(remaining, invited):
    if len(invited) > 0:
        print invited
    
    if len(remaining) == 0:
        return

    for i in range(len(remaining)):
        permute(remaining[0:i] + remaining[i+1:], invited + remaining[i:i+1])

def combine(remaining, invited):
    if len(remaining) == 0:
        return [invited]
    else:
        return combine(remaining[1:], invited + remaining[0:1]) + \
               combine(remaining[1:], invited)

print 'Combine:'
print combine(['a', 'b', 'c'], [])

print 'Permute:'
permute(['a', 'b', 'c'], [])

