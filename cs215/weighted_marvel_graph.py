from itertools import combinations
from heapq import heappush, heappop

import csv
import os

CHARACTERS  = ['SPIDER-MAN/PETER PAR','GREEN GOBLIN/NORMAN ','WOLVERINE/LOGAN ','PROFESSOR X/CHARLES ','CAPTAIN AMERICA']

def dijkstra(graph, start_node):
    heap = []
    
    distance_so_far = {}
    shortest_paths_set = {}
    final_distance = {} #Consolidated distances(nodes)

    distance_so_far[ start_node ] = 0
    heappush(heap, (0 , start_node))
    shortest_paths_set[start_node] = [[start_node]]

    while len(final_distance) < len(graph) and heap:
        # Pick the (not final) node having smaller distance 
        shortest_distance, closer_node = heappop(heap)
        #Make it final
        final_distance[ closer_node ] = shortest_distance

        for neighbor in graph[closer_node]:
            if neighbor not in final_distance:
                distance_through_closer_node = shortest_distance + 1.0 / graph[ closer_node ][neighbor]
                if neighbor not in distance_so_far:
                    distance_so_far[neighbor] = distance_through_closer_node #compute distance
                    heappush( heap, (distance_through_closer_node, neighbor) )#update the heap
                    paths = [ path +[ neighbor ] for path in shortest_paths_set[ closer_node ]] #create the path
                    shortest_paths_set[ neighbor ] = paths
                elif distance_through_closer_node < distance_so_far[neighbor] :
                    distance_so_far[neighbor] = distance_through_closer_node #update distance
                    heappush( heap, (distance_through_closer_node, neighbor) )#update the heap
                    paths = [ path +[ neighbor ] for path in shortest_paths_set[ closer_node ]]#create the path
                    shortest_paths_set[ neighbor ] = paths
                elif distance_through_closer_node == distance_so_far[neighbor]:
                    paths = [ path +[ neighbor ] for path in shortest_paths_set[ closer_node ]]
                    shortest_paths_set[ neighbor ].extend( paths )
                    heappush( heap, (distance_through_closer_node, neighbor) )
   
    return final_distance, shortest_paths_set

def make_link(graph,  node1, node2):
    if node1 not in graph:
        graph[node1] = {}
    graph[node1][node2] = 1
    
    if node2 not in graph:
        graph[node2] = {}
    graph[node2][node1] = 1
    
    return graph

def make_weighted_link(graph,  node1, node2):
    if node1 not in graph:
        graph[node1] = {}
    if node2 not in graph[node1]:
        graph[node1][node2] = 1.0
    else:
        graph[node1][node2] = graph[node1][node2] + 1.0
    
    if node2 not in graph:
        graph[node2] = {}
    if node1 not in graph[node2]:
        graph[node2][node1] = 1.0
    else:
        graph[node2][node1] = graph[node2][node1] + 1.0
    
    return graph

graph = {}
w_graph = {}
comics = {}
current_folder = os.curdir

print current_folder
marvel_world = csv.reader(open(current_folder + os.sep + 'marvel.txt','rb'), delimiter='\t')

characters = set()   

print 'Scanning data..'
for entry in marvel_world:
    character, comic= entry
    if comic not in comics:
            comics[comic] = []
    comics[comic].append(character)
    characters.add(character)
    
print 'Creating the graph...'
weighted_graph = {}
graph = {}

for cast in comics.values():
    for char1, char2 in combinations(cast, 2):
        graph = make_link( graph, char1, char2)
        weighted_graph = make_weighted_link( weighted_graph, char1, char2)

print 'Checking shortest path...'
count = 0

for character in CHARACTERS:
    distances, UNweighted_short_paths = dijkstra(graph, character)
    w_distances, weighted_short_paths = dijkstra(weighted_graph, character)

    p_count = 0 #counter: how many shortest path
    for other_character in weighted_short_paths:
        path_with_smallest_number_of_hops = min(weighted_short_paths[other_character], key= lambda x : len(x))
        if path_with_smallest_number_of_hops not in UNweighted_short_paths[other_character]:
            count   += 1
            p_count += 1
    print character, ':', p_count, ' differences'

print 'Total number of differences:', count 
