from cmu_graphics import *
from collections import deque
import copy
# deque info from: https://www.geeksforgeeks.org/queue-in-python/
# BFS learning from: https://www.youtube.com/watch?v=T_m27bhVQQQ

def specificCost(maze, currPos, goalPos):
    print(maze)
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
        if (drow, dcol) == (1,0):
            direction = 0
        elif (drow, dcol) == (0,-1):
            direction = 1
        elif (drow, dcol) == (-1,0):
            direction = 2
        elif (drow, dcol) == (0,1):
            direction = 3
        if isValid(maze, visited, currRow, currCol, drow, dcol, direction):
            currRow += drow
            currCol += dcol
            queue.append((currRow, currCol))
            costs[(currRow, currCol)] = 1
            paths[(currRow, currCol)] = [(currRow, currCol)]
            currRow = 0
            currCol = 0
    while queue != deque():
        currRow, currCol = queue.popleft()
        visited.append((currRow, currCol))
        for drow, dcol in directionsList:
            if (drow, dcol) == (1,0):
                direction = 0
            elif (drow, dcol) == (0,-1):
                direction = 1
            elif (drow, dcol) == (-1,0):
                direction = 2
            elif (drow, dcol) == (0,1):
                direction = 3
            if isValid(maze, visited, currRow, currCol, drow, dcol, direction) == True:
                #if it hasnt been visited, within bounds, and doesnt break through a wall
                pastRow = currRow
                pastCol = currCol
                currRow += drow
                currCol += dcol
                if (currRow, currCol) in costs:
                    if costs[(currRow, currCol)] > (costs[(pastRow, pastCol)] + 1):
                        costs[(currRow, currCol)] = costs[(pastRow, pastCol)] + 1 #resetting cost to lower cost if it is
                else:
                    costs[(currRow, currCol)] = costs[(pastRow, pastCol)] + 1
                    temp = copy.deepcopy(paths[(pastRow, pastCol)])
                    # print('-----')
                    # print(temp is paths[(pastRow, pastCol)])
                    temp.append((currRow, currCol))
                    # print(temp)
                    paths[(currRow, currCol)] = temp
                    # print('~~~~~')
                    # print(paths)

                queue.append((currRow, currCol))
    return costs, paths

def isValid(maze, visited, row, col, drow, dcol, direction):
    baseRow = row
    baseCol = col
    row += drow
    col += dcol
    # print('-----------')
    # print((baseRow, baseCol))
    # print(direction)
    if(0 <= row < len(maze.list) and
       0 <= col < len(maze.list[0])): #in maze bounds
        if((row, col) not in visited): #hasnt been seen
            if(maze[baseRow][baseCol][direction] == 0):
                # print('True')
                return True
    # print('False')
    return False