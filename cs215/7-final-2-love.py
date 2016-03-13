#
# Take a weighted graph representing a social network where the weight
# between two nodes is the "love" between them.  In this "feel the
# love of a path" problem, we want to find the best path from node `i`
# and node `j` where the score for a path is the maximum love of an
# edge on this path. If there is no path from `i` to `j` return
# `None`.  The returned path doesn't need to be simple, ie it can
# contain cycles or repeated vertices.
#
# Devise and implement an algorithm for this problem.
#

def bfs(G, node):
    
    visited = []
    queue = [node]
    path = { node : [node] }

    while len(queue) > 0:
        node = queue.pop()
        
        for t in G[node]:
            if t not in visited:
                path[t] = path[node] + [t]
                queue.append(t)
        
        if node not in visited:
            visited.append(node)
    
    return visited, path

def longest_edge(G, nodes):
    e = None
    for n1 in nodes:
        for n2 in G[n1]:
            if n2 in nodes:
                if e == None or G[n1][n2] > G[e[0]][e[1]]:
                    e = (n1, n2)
    return e

def feel_the_love(G, i, j):
    # return a path (a list of nodes) between `i` and `j`,
    # with `i` as the first node and `j` as the last node,
    # or None if no path exists
    nodes, paths = bfs(G, i)
    if j in nodes:
        e = longest_edge(G, nodes)
        tailnodes, tailpaths = bfs(G, e[1])
        path = paths[e[0]] + tailpaths[j]
        return path
    return None

#########
#
# Test

def score_of_path(G, path):
    max_love = -float('inf')
    for n1, n2 in zip(path[:-1], path[1:]):
        love = G[n1][n2]
        if love > max_love:
            max_love = love
    return max_love

def test():
    G = {'a':{'c':1},
         'b':{'c':1},
         'c':{'a':1, 'b':1, 'e':1, 'd':1},
         'e':{'c':1, 'd':2},
         'd':{'e':2, 'c':1},
         'f':{}}
    path = feel_the_love(G, 'a', 'b')
    assert score_of_path(G, path) == 2

    path = feel_the_love(G, 'a', 'f')
    assert path == None

test()