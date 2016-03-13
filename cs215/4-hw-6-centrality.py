import csv

def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values()))/len(distance_from_start)

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    r = csv.reader(open('imdb-1.tsv', 'rb'), delimiter="\t")
    actors = {}
    G = {}
    for row in r:
        (a, m, y) = row
        k = m + ', ' + y
        make_link(G, k, a)
        actors[a] = -1
    
    print 'created graph'
    
    #print G

    for a in actors:
        actors[a] = centrality(G, a)
    
    print 'calculated centrality'
    
    s = sorted(actors, key=actors.get)
    print 'sorted centrality'
    
    for i in range(20):
        print (i + 1), ':', s[i], actors[s[i]]

test()