#
# write up_heapify, an algorithm that checks if
# node i and its parent satisfy the heap
# property, swapping and recursing if they don't
#
# L should be a heap when up_heapify is done
#

def up_heapify(L, i):
    if i <= 0: return
    p = parent(i)
    if L[p] > L[i]:
        L[i], L[p] = L[p], L[i]
        up_heapify(L, p)

def down_heapify(L, i):
    if leaf(L, i): return
    if one_child(L, i):
        if L[i] > L[left(i)]:
            (L[i], L[left(i)]) = (L[left(i)], L[i])
        return
    if min(L[left(i)], L[right(i)]) >= L[i]: return
    if L[left(i)] < L[right(i)]:
        (L[i], L[left(i)]) = (L[left(i)], L[i])
        down_heapify(L, left(i))
        return
    (L[i], L[right(i)]) = (L[right(i)], L[i])
    down_heapify(L, right(i))
    return

def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

def test():
    L = [2, 4, 3, 5, 9, 7, 7]
    L.append(1)
    up_heapify(L, 7)
    assert 1 == L[0]
    assert 2 == L[1]

test()