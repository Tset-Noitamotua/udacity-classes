#
# Another way of thinking of a path in the Kevin Bacon game 
# is not about finding short paths, but by finding paths 
# that don't use obscure movies. We will give you a 
# list of movies along with their obscureness score.  
#
# For this assignment, we'll approximate obscurity 
# based on the multiplicative inverse of the amount of 
# money the movie made.  Though, its not really important where
# the obscurity score came from.
#
# Use the the imdb-1.tsv and imdb-weights.tsv files to find
# the obscurity of the 'least obscure' 
# path from a given actor to another.  
# The obscurity of a path is the maximum obscurity of 
# any of the movies used along the path.
#
# You will have to do the processing in your local environment
# and then copy in your answer.
#
# Hint: A variation of Dijkstra can be used to solve this problem.
#

# Change the None values in this dictionary to be the obscurity score
# of the least obscure path between the two actors

import csv

from heapq import heappush, heappop

movies = {}
r = csv.reader(open('imdb-weights.tsv', 'rb'), delimiter="\t")
for m, y, w in r:
    k = m + ', ' + y
    movies[k] = float(w)

print 'read all movie obscurities'

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def obscurity(path):
    o = [movies[m] for m in movies.keys() if m in path]
    if len(o) > 0: return max(o)
    return 0.0

def dijkstra(graph, start_node):
    heap = []
    
    distance_so_far = {}
    shortest_path = {}
    final_distance = {}

    distance_so_far[start_node] = 0
    heappush(heap, (0, start_node))
    shortest_path[start_node] = [start_node]

    while len(final_distance) < len(graph) and heap:
        shortest_distance, closer_node = heappop(heap)
        final_distance[closer_node] = shortest_distance

        #print shortest_distance, closer_node

        for neighbor in graph[closer_node]:
            if neighbor not in final_distance:
                distance_through_closer_node = max(shortest_distance, obscurity([neighbor]))
                if neighbor not in distance_so_far:
                    distance_so_far[neighbor] = distance_through_closer_node # compute distance
                    heappush(heap, (distance_through_closer_node, neighbor)) # update the heap
                    shortest_path[neighbor] = shortest_path[closer_node] + [neighbor] # create the path
                elif distance_through_closer_node < distance_so_far[neighbor] :
                    distance_so_far[neighbor] = distance_through_closer_node # update distance
                    heappush(heap, (distance_through_closer_node, neighbor)) # update the heap
                    shortest_path[neighbor] = shortest_path[closer_node] + [neighbor] # create the path
   
    return final_distance, shortest_path

# Change the `None` values in this dictionary to be the obscurity score
# of the least obscure path between the two actors
answer = {('Boone Junior, Mark', 'Del Toro, Benicio'): None,
          ('Braine, Richard', 'Coogan, Will'): None,
          ('Byrne, Michael (I)', 'Quinn, Al (I)'): None,
          ('Cartwright, Veronica', 'Edelstein, Lisa'): None,
          ('Curry, Jon (II)', 'Wise, Ray (I)'): None,
          ('Di Benedetto, John', 'Hallgrey, Johnathan'): None,
          ('Hochendoner, Jeff', 'Cross, Kendall'): None,
          ('Izquierdo, Ty', 'Kimball, Donna'): None,
          ('Jace, Michael', 'Snell, Don'): None,
          ('James, Charity', 'Tuerpe, Paul'): None,
          ('Kay, Dominic Scott', 'Cathey, Reg E.'): None,
          ('McCabe, Richard', 'Washington, Denzel'): None,
          ('Reid, Kevin (I)', 'Affleck, Rab'): None,
          ('Reid, R.D.', 'Boston, David (IV)'): None,
          ('Restivo, Steve', 'Preston, Carrie (I)'): None,
          ('Rodriguez, Ramon (II)', 'Mulrooney, Kelsey'): None,
          ('Rooker, Michael (I)', 'Grady, Kevin (I)'): None,
          ('Ruscoe, Alan', 'Thornton, Cooper'): None,
          ('Sloan, Tina', 'Dever, James D.'): None,
          ('Wasserman, Jerry', 'Sizemore, Tom'): None}

# Here are some test cases.
# For example, the obscurity score of the least obscure path
# between 'Ali, Tony' and 'Allen, Woody' is 0.5657
test = {('Ali, Tony', 'Allen, Woody'): 0.5657,
        ('Auberjonois, Rene', 'MacInnes, Angus'): 0.0814,
        ('Avery, Shondrella', 'Dorsey, Kimberly (I)'): 0.7837,
        ('Bollo, Lou', 'Jeremy, Ron'): 0.4763,
        ('Byrne, P.J.', 'Clarke, Larry'): 0.109,
        ('Couturier, Sandra-Jessica', 'Jean-Louis, Jimmy'): 0.3649,
        ('Crawford, Eve (I)', 'Cutler, Tom'): 0.2052,
        ('Flemyng, Jason', 'Newman, Laraine'): 0.139,
        ('French, Dawn', 'Smallwood, Tucker'): 0.2979,
        ('Gunton, Bob', 'Nagra, Joti'): 0.2136,
        ('Hoffman, Jake (I)', 'Shook, Carol'): 0.6073,
        ('Kamiki, Ry\xfbnosuke', 'Thor, Cameron'): 0.3644,
        ('Roache, Linus', 'Dreyfuss, Richard'): 0.6731,
        ('Sanchez, Phillip (I)', 'Wiest, Dianne'): 0.5083,
        ('Sheppard, William Morgan', 'Crook, Mackenzie'): 0.0849,
        ('Stan, Sebastian', 'Malahide, Patrick'): 0.2857,
        ('Tessiero, Michael A.', 'Molen, Gerald R.'): 0.2056,
        ('Thomas, Ken (I)', 'Bell, Jamie (I)'): 0.3941,
        ('Thompson, Sophie (I)', 'Foley, Dave (I)'): 0.1095,
        ('Tzur, Mira', 'Heston, Charlton'): 0.3642}

r = csv.reader(open('imdb-1.tsv', 'rb'), delimiter="\t")

G = {}
for a, m, y in r:
    k = m + ', ' + y
    make_link(G, k, a)

print 'created graph'

#for k in test.iterkeys():
#    n1, n2 = k
#    final_distance, shortest_path = dijkstra(G, n1)
#    print n1, '--', n2, ':', final_distance[n2], '==', test[k], ':', (final_distance[n2] == test[k])

print 'answer = {'
for k in answer.iterkeys():
    n1, n2 = k
    final_distance, shortest_path = dijkstra(G, n1)
    print "        ('%s', '%s'): %.4f," % (n1, n2, final_distance[n2])
print '}'
