from cmu_graphics import *
from collections import deque
# deque info from: https://www.geeksforgeeks.org/queue-in-python/
# BFS search info from: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

def specificCost(maze, currPos, goalPos):
    costs, paths = BFS(maze, currPos)
    return costs[goalPos], paths[goalPos]

def BFS(maze, startingPos):
    directionsList = [(1,0),(0,-1),(-1,0),(0,1)] #down left up right
    visited = []
    visited.append(startingPos)
    costs = dict()
    paths = dict()
    queue = deque()
    currRow, currCol = startingPos
    pastRow = 0
    pastCol = 0
    for drow, dcol in directionsList:
        currRow += drow
        currCol += dcol
        queue.append((currRow, currCol))
        costs[(currRow, currCol)] = 1
        paths[(currRow, currCol)] = [(currRow, currCol)]
        currRow = 0
        currCol = 0
    print(paths)
    while queue != deque():
        currRow, currCol = queue.popleft()
        visited.append((currRow, currCol))
        for drow, dcol in directionsList:
            if isValid(maze, visited, currRow, currCol, drow, dcol):
                #if it hasnt been visited, within bounds, and doesnt break through a wall
                pastRow = currRow
                pastCol = currCol
                currRow += drow
                currCol += dcol
                if (currRow, currCol) in costs:
                    if costs[(currRow, currCol)] > (costs[(pastRow, pastCol)] + 1):
                        costs[(currRow, currCol)] = costs[(pastRow, pastCol)] + 1 #resetting cost to lower cost if it is
                        paths[(currRow, currCol)] = paths[(pastRow, pastCol)].append((currRow, currCol))
                else:
                    costs[(currRow, currCol)] = costs[(pastRow, pastCol)] + 1
                    paths[(currRow, currCol)] = paths[(pastRow, pastCol)].append((currRow, currCol))
                queue.append((currRow, currCol))
    return costs, paths

def isValid(maze, visited, row, col, drow, dcol):
    direction = 0
    row += drow
    col += dcol
    if (drow, dcol) == (1,0):
        direction = 0
    elif(drow, dcol) == (0,-1):
        direction = 1
    elif(drow, dcol) == (-1,0):
        direction = 2
    elif(drow, dcol) == (0,1):
        direction = 3
    if(0 <= row < len(maze) and
       0 <= col < len(maze[0])): #in maze bounds
        if((row, col) not in visited): #hasnt been seen
            if(maze[row][col][direction] == 0):
                return True
    return False

list = [[[1, 1, 1, 0], [1, 0, 1, 0], [0, 0, 1, 1], [1, 1, 1, 0], [0, 0, 1, 1]], 
        [[0, 1, 1, 1], [0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1]], 
        [[0, 1, 0, 1], [0, 1, 0, 1], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 1, 1]], 
        [[0, 1, 0, 1], [1, 1, 0, 0], [1, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 1]], 
        [[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 0, 0], [1, 0, 0, 1]]]
cost, path = specificCost(list, (0,0), (2,2))

print(cost)
print(path)