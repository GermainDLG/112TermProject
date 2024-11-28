from cmu_graphics import *
from collections import deque
# deque info from: https://www.geeksforgeeks.org/queue-in-python/
# BFS search info from: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

def BFS(list, startingPos):
    directionsList = [(1,0),(0,-1),(-1,0),(0,1)] #down left up right
    visited = []
    queue = deque()
    
