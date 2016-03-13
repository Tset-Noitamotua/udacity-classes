#
# The code below uses a linear
# scan to find the unfinished node
# with the smallest distance from
# the source.
#
# Modify it to use a heap instead
# 

def up_heapify(L, i):
    if i <= 0: return
    p = parent(i)
    if L[p] > L[i]:
        L[i], L[p] = L[p], L[i]
        up_heapify(L, p)

def down_heapify(L, i):
    if is_leaf(L, i): return
    if one_child(L, i):
        if L[i] > L[left_child(i)]:
            (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        return
    if min(L[left_child(i)], L[right_child(i)]) >= L[i]: return
    if L[left_child(i)] < L[right_child(i)]:
        (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        down_heapify(L, left_child(i))
        return
    (L[i], L[right_child(i)]) = (L[right_child(i)], L[i])
    down_heapify(L, right_child(i))
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

def shortest_dist_node(dist_heap):
    hmin = dist_heap[0]
    dist_heap[0] = dist_heap[len(dist_heap)-1]
    dist_heap.pop(len(dist_heap)-1)
    down_heapify(dist_heap, 0)
    return hmin[1]

def dijkstra(G,v):
    final_dist = {}
    dist_heap = [(0, v)]
    dist_so_far = {}
    dist_so_far[v] = 0
    while len(final_dist) < len(G):
        w = shortest_dist_node(dist_heap)
        # lock it down!
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    dist_heap.append((dist_so_far[x], x))
                    up_heapify(dist_heap, len(dist_heap) - 1)
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    dist_heap.append((dist_so_far[x], x))
                    up_heapify(dist_heap, len(dist_heap) - 1)
    return final_dist

############
# 
# Test

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G


def test():
    # shortcuts
    (a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3), 
               (e,g,1),(e,f,5),(f,g,2),(b,f,1))
    G = {}
    for (i,j,k) in triples:
        make_link(G, i, j, k)

    dist = dijkstra(G, a)
    assert dist[g] == 8 #(a -> d -> e -> g)
    assert dist[b] == 11 #(a -> d -> e -> g -> f -> b)

test()