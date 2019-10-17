import math
'''欧几里得距离'''
def euclidean_distance(start, goal):
    return math.hypot(goal[0] - start[0], goal[1] - start[1])

'''曼哈顿距离'''
def manhattan_distance(start, goal):
    return abs(goal[0] - start[0]) + abs(goal[1] - start[1])

'''切比雪夫距离'''
def chebyshev_distance(start, goal):
    return max(abs(goal[0] - start[0]), abs(goal[1] - start[1]))
    
'''启发式函数'''
def distance(start, goal):
    return euclidean_distance(start, goal)

def shortest_path(M, start, goal):
    bestPath = []
    closed = set()
    opened = {start}
    path = {}
    g = {start:0}
    h = {start:distance(M.intersections[start], M.intersections[goal])}
    f = {start:h[start]}
    while len(opened) > 0:
        x = min(f, key=f.get)
        if x == goal:
            break
        opened.remove(x)
        closed.add(x)
        del f[x]
        for y in M.roads[x]:
            if y in closed:
                continue

            gy = g[x] + distance(M.intersections[x], M.intersections[y])
            better = 0
            if y not in opened:
                better = 1
            elif gy < g[y]:
                better = 1
            else:
                better = 0

            if better == 1:
                path[y] = x
                g[y] = gy
                h[y] = distance(M.intersections[y], M.intersections[goal])
                f[y] = g[y] + h[y]
                opened.add(y)
    node = goal
    while path.__contains__(node):
        bestPath.insert(0, node)
        node = path[node]
    bestPath.insert(0, node)
    return bestPath
