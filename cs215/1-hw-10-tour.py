# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    path = find_path(graph, set(), [], graph[0])
    return [edge[0] for edge in path[:-1]] + list(path[-1]) if path else []

def find_path(all_edges, explored, path, current_edge):
    explored = explored | set([current_edge]) | set([tuple(reversed(current_edge))])

    if set(all_edges) <= set(explored):
        return path + [current_edge]

    _, node = current_edge
    successors = [edge for edge in all_edges if node in edge]

    for edge in successors:
        if edge in explored:
            continue
        edge = edge if node == edge[0] else tuple(reversed(edge))
        result = find_path(all_edges, explored, path + [current_edge], edge)
        if result:
            return result

    return []

def test():
  g0=[(1,2),(2,3),(3,4),(4,1),(2,5),(3,5),(4,5)]  # No eulerian path 
  assert find_eulerian_tour(g0)==[]
  
  g1=[(1,2),(2,3),(3,4),(4,1)]
  assert find_eulerian_tour(g1) in [[1,2,3,4,1],[2,3,4,1,2],[3,4,1,2,3],[4,1,2,3,4],[1,4,3,2,1],[2,1,4,3,2],[3,2,1,4,3],[4,3,2,1,4]]
  
  g2=[(1,2),(2,3),(3,4),(4,1),(1,3)]
  assert find_eulerian_tour(g2) in [[1,2,3,4,1,3],[1,2,3,1,4,3],[1,4,3,2,1,3],[1,4,3,1,2,3],[1,3,4,1,2,3],[1,3,2,1,4,3],[3,2,1,4,3,1],[3,2,1,3,4,1],[3,4,1,2,4,1],[3,4,1,3,2,1],[3,1,2,3,4,1],[3,1,4,3,2,1]]
  
  print('Test passed')

test()