#
# In lecture, we took the bipartite Marvel graph,
# where edges went between characters and the comics
# books they appeared in, and created a weighted graph
# with edges between characters where the weight was the
# number of comic books in which they both appeared.
#
# In this assignment, determine the weights between
# comic book characters by giving the probability
# that a randomly chosen comic book containing one of
# the characters will also contain the other
#

from marvel import marvel, characters
from collections import defaultdict

def create_weighted_graph(graph, characters):
    G = defaultdict(dict)
    
    for hero in characters:
        for comic in graph[hero]:
            for other in graph[comic]:
                if hero > other:
                    separate_movies = set(graph[hero].keys() + graph[other].keys())
                    together_movies = set(graph[hero].keys()) & set(graph[other].keys())
                    weight = 1.0 * len(together_movies) / len(separate_movies)
                    G[hero][other] = weight
                    G[other][hero] = weight
    return G

######
#
# Test

def test():
    bipartiteG = {'charA':{'comicB':1, 'comicC':1},
                  'charB':{'comicB':1, 'comicD':1},
                  'charC':{'comicD':1},
                  'comicB':{'charA':1, 'charB':1},
                  'comicC':{'charA':1},
                  'comicD': {'charC':1, 'charB':1}}
    G = create_weighted_graph(bipartiteG, ['charA', 'charB', 'charC'])
    # three comics contain charA or charB
    # charA and charB are together in one of them
    assert G['charA']['charB'] == 1.0 / 3
    assert G['charA'].get('charA') == None
    assert G['charA'].get('charC') == None

def test2():
    G = create_weighted_graph(marvel, characters)
    
test()
test2()