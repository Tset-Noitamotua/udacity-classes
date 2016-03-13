# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------

def compute_value():
    value = [[99 for c in range(len(grid[0]))] for r in range(len(grid))]
    value[goal[0]][goal[1]] = 0

    open = [[0, goal[0], goal[1]]]
    while len(open) > 0:
        open.sort()
        open.reverse()
        c = open.pop()
        x = c[1]
        y = c[2]
        d = c[0]
        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if x2 >= 0 and y2 >= 0 and x2 < len(grid) and y2 < len(grid[0]) and grid[x2][y2] == 0:
                d2 = d + cost_step
                if value[x2][y2] > d2:
                    value[x2][y2] = d2
                    open.append([d2, x2, y2])

    return value #make sure your function returns a grid of values as demonstrated in the previous video.

v = compute_value()
for r in v:
    print r

