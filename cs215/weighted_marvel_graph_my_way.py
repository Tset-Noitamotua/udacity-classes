from itertools import combinations
from heapq import heappush, heappop
import csv
import os
CHARACTERS  = ['SPIDER-MAN/PETER PAR','GREEN GOBLIN/NORMAN ','WOLVERINE/LOGAN ','PROFESSOR X/CHARLES ','CAPTAIN AMERICA']
# This function returns 2 dictionaries:
# final_distance:       each key is a node reachable from start_node and
#                       final_distance[key] is the length of the shortest path
#                       from start_node to key
#
# shortest_paths_set:   each key is a node reachable from start_node and
#                       shortest_paths_set[key] is a list of all the possible shortest paths
#                       from start_node to key
#
def dijkstra(graph, start_node):
        heap = []
        #keep the current shortest distance for each node found 
        distance_so_far = {}
        shortest_paths_set = {}
        final_distance = {} #Consolidated distances(nodes)

        #Initialize everything using start_node
        distance_so_far[ start_node ] = 0
        heappush( heap, ( 0 , start_node ) )
        shortest_paths_set[ start_node ] = [[start_node]]
        
    
        while len(final_distance) < len(graph) and heap:
            #Pick the (not final) node having smaller distance 
            shortest_distance, closer_node = heappop(heap)
            #Make it final
            final_distance[ closer_node ] = shortest_distance

            #Consider all the neighbors
            for neighbor in graph[closer_node]:
                        #if it hasn't been consolidated yet
                        if neighbor not in final_distance:
                                distance_through_closer_node = shortest_distance + 1.0 / graph[ closer_node ][neighbor]
                                #If the current neighbor wasn't reachable...
                                if neighbor not in distance_so_far:
                                        distance_so_far[neighbor] = distance_through_closer_node #compute distance
                                        heappush( heap, (distance_through_closer_node, neighbor) )#update the heap
                                        paths = [ path +[ neighbor ] for path in shortest_paths_set[ closer_node ]] #create the path
                                        shortest_paths_set[ neighbor ] = paths
                                #If the current neighbor was reachable, but we've just found a shortcut...
                                elif distance_through_closer_node < distance_so_far[neighbor] :
                                        distance_so_far[neighbor] = distance_through_closer_node #update distance
                                        heappush( heap, (distance_through_closer_node, neighbor) )#update the heap
                                        paths = [ path +[ neighbor ] for path in shortest_paths_set[ closer_node ]]#create the path
                                        shortest_paths_set[ neighbor ] = paths
                                #If  we have found an equivalent path (alternative)...
                                elif distance_through_closer_node == distance_so_far[neighbor]:
                                        paths = [ path +[ neighbor ] for path in shortest_paths_set[ closer_node ]]
                                        #add this to the path we already know
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
		graph[node1][node2] = graph[node1][node2]  + 1.0
	
	if node2 not in graph:
		graph[node2] = {}
	if node1 not in graph[node2]:
		graph[node2][node1] = 1.0
	else:
		graph[node2][node1] = graph[node2][node1]  + 1.0
	
	return graph


comics = {}
current_folder = os.curdir

marvel_world = csv.reader(open(current_folder+os.sep+'marvel.tsv','rb'), delimiter='\t')
characters = set()   
#scan data
print 'Scanning data..'
for entry in marvel_world:
        character, comic= entry
        #if this is the first time I meet this comic...
        if comic not in comics:
                comics[comic] = []
        #for each comic we store all the characters appearing in that comic        
        comics[comic].append(character)

        # add the character to the set
        # I chose set as data-structure, because if we meet the same character more than once
        # we won't get duplicates
        characters.add(character)

    
    
#create the graph
print 'Creating the graph...'
weighted_graph = {}
graph = {}
#For each comic we have a list of characters appearing in that comic...
for cast in comics.values():
                 # for each possible pair of character appearing in the comic we add a link
                 # I used combinations to avoid to count the same pair of characters twice
                 # N.B. : from itertools import combinations
                 #        combinations(iterable, r) --> combinations object
                 #        Return successive r-length combinations of elements in the iterable.
                 #        combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)

		for char1, char2 in combinations(cast, 2):
				graph = make_link( graph, char1, char2)
				weighted_graph = make_weighted_link( weighted_graph, char1, char2)



print 'Checking shortest path...'
count = 0
i_count   = 0
for character in CHARACTERS:
        #Run Dijkstra for weighted and unweighted graph
        distances, UNweighted_short_paths   = dijkstra(graph, character)
        w_distances, weighted_short_paths = dijkstra(weighted_graph, character)

        p_count = 0 #counter: how many shortest path
        i_p_count = 0
        for other_character in weighted_short_paths:
               for unweighted_path in UNweighted_short_paths[other_character]:
                        #if any path is no longer optimal when we use a weighted graph
                        if unweighted_path not in weighted_short_paths[other_character]:
                                count   += 1
                                p_count += 1
                        else:
                                i_count   += 1
                                i_p_count += 1
        print character, ':', p_count, 'unweighted paths are no longer optimal using a weighted graph, whereas', i_p_count, 'are still shortest paths'

print 'Final results', count, ' unweighted paths are no longer optimal using a weighted graph, whereas', i_count, 'are still shortest paths'
