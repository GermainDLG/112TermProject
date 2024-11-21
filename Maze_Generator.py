from cmu_graphics import *
import math
import random


# INSPIRATION FROM: https://www.youtube.com/watch?v=jZQ31-4_8KM
class Maze:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.list = []
    
    def generateList(self):
        for i in range(self.height):
            self.list.append([])
        for emptylist in self.list:
            for j in range(self.width):
                emptylist.append([1,1,1,1]) # [bottom, left, top, right]
    
    def generateMaze(self, visited = [], currPos = (0,0)):
        rows, cols = len(self.list), len(self.list[0])
        directionList = [(1,0),(0,-1),(-1,0),(0,1)]
        if(len(visited) == self.height * self.width):
            return 'done'
        else:
            directionsIndex = self.getPossibleDirections(currPos,visited)
            temp = set()
            while temp != set(directionsIndex):
                randomIndex = random.randint(0,len(directionsIndex)-1)
                move = directionsIndex[randomIndex]
                if move not in temp:
                    drow, dcol = directionList[move]
                    currRow, currCol = currPos
                    # vv make move vv
                    visited.append(currPos)
                    self.list[currRow][currCol][move] = 0
                    currRow += drow
                    currCol += dcol
                    currPos = (currRow, currCol)
                    if move > 1:
                        newMove = move - 2
                    elif move < 2:
                        newMove = move + 2
                    self.list[currRow][currCol][newMove] = 0
                    result = self.generateMaze(visited, currPos)
                    if result != None:
                        return result
                    self.list[currRow][currCol][newMove] = 1
                    currRow -= drow
                    currCol -= dcol
                    currPos = (currRow, currCol)
                    self.list[currRow][currCol][move] = 1
                    temp.add(move)
            return None
                


    
    def getPossibleDirections(self, currPos,visited):
        directionList = [(1,0),(0,-1),(-1,0),(0,1)]
        directionsIndex = []
        for i in range(4):
            currRow, currCol = currPos
            drow, dcol = directionList[i]
            currRow += drow
            currCol += dcol
            if(self.isValid(currRow,currCol,visited)):
                directionsIndex.append(i)
            return directionsIndex
        
    def isValid(self, row, col, visited):
        if((0 <= row < len(self.list)) and 
          (0 <= col < len(self.list[0]))):
          if((row,col) not in visited):
            return True
        return False

            # while seen != set([0,1,2,3]):
            #     direction = random.randint(0,3) # 0-3: bottom, left, top, right
            #     while direction in seen: #always gets a new direction
            #         direction = random.randint(0,3)
            #     seen.add(direction)
            #     drow, dcol = directionList[direction]
            #     if(self.isValid(currPos,drow,dcol,visited)): #validity check
            #         #make moves below
            #         currRow, currCol = currPos
            #         self.list[currRow][currCol][direction] = 0
            #         visited.append((currRow, currCol))
            #         currRow += drow
            #         currCol += dcol
            #         currPos = (currRow, currCol)
            #         if(direction > 1):
            #             newDirection = direction-2
            #         else:
            #             newDirection = direction + 2
            #         self.list[currRow][currCol][newDirection] = 0
            #         result = self.generateMaze(visited,currPos)
            #         if(result != None):
            #             return result
            #         visited.pop()
            #         self.list[currRow][currCol][newDirection] = 1
            #         currRow -= drow
            #         currCol -= dcol
            #         currPos = (currRow, currCol)
            # return None


            # possibleDirections, directionsIndex = self.getPossibleDirections(currPos, visited)
            #         #WARNING: RANDINT OF EMPTY LIST CRASHES
            #         #add something here to backtrack if possibleDirections is empty
            #         if(possibleDirections == []):
            #             return None
            #         move = random.randint(0, len(possibleDirections)-1) #0,1,2,3
            #         drow, dcol = possibleDirections[move]
            #         currRow, currCol = currPos
            #         print(f'currPos BEFORE {currPos}')
            #         visited.append((currRow,currCol))
            #         directionMoved = directionsIndex[move]
            #         self.list[currRow][currCol][directionMoved] = 0
            #         currRow += drow
            #         currCol += dcol
            #         currPos = (currRow, currCol)
            #         print(f'currPos AFTER {currPos}')
            #         if(directionMoved > 1):
            #             oppositeDirection = directionMoved - 2
            #         else:
            #             oppositeDirection = directionMoved + 2
            #         print(currRow, currCol)
            #         self.list[currRow][currCol][oppositeDirection] = 0
            #         nextMove = self.generateMaze(visited, currPos)
            #         if nextMove != None:
            #             return nextMove
            #         self.list[currRow][currCol][oppositeDirection] = 1
            #         currRow -= possibleDirections[move][0]
            #         currCol -= possibleDirections[move][1]
            #         self.list[currRow][currCol][directionMoved] = 1
            #         visited.pop()
        
    # good to go
    
    def __repr__(self):
        return f'{self.list}'

y = Maze(5,5)
y.generateList()
y.generateMaze()
print(y)
