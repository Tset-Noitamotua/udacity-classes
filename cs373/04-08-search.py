# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    visited = []
    for r in grid:
        row = []
        for c in r:
            row.append(False)
        visited.append(row)
        
    openlist = [[0, 0, 0]]
    
    while len(openlist) > 0:
        openlist.sort()
        current = openlist.pop(0)
        visited[current[1]][current[2]] = True
        if current[1] == goal[0] and current[2] == goal[1]:
            print current
            return
        else:
            for d in delta:
                r = current[1] + d[0]
                c = current[2] + d[1]
                if (r >= 0) and (c >= 0) and (r < len(grid)) and (c < len(grid[0])):
                    if visited[r][c] == False and grid[r][c] == 0:
                        openlist.append([current[0] + 1, r, c])
                        visited[r][c] = True
    print 'fail'

search()