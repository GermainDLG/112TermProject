from cmu_graphics import *
import math
import random


# INSPIRATION FROM: https://www.youtube.com/watch?v=jZQ31-4_8KM
class Maze:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.list = []
        self.surrounding = []
    
    def generateList(self):
        for i in range(self.height):
            self.list.append([])
        for emptylist in self.list:
            for j in range(self.width):
                emptylist.append([1,1,1,1]) # [bottom, left, top, right]
    
    def generateMaze(self, visited = [], currPos = (0,0)):
        directionList = [(1,0),(0,-1),(-1,0),(0,1)]
        directionsIndex = [1]
        if(len(set(visited)) == self.height * self.width):
            return 'done'
        else:
            while directionsIndex != []:
                directionsIndex = self.getPossibleDirections(currPos,visited)
                if directionsIndex == []:
                    return None
                i = random.randint(0,len(directionsIndex)-1)
                moveIndex = directionsIndex[i]
                visited.append(currPos)
                print(f'currPos: {currPos}')
                print(f'visited {visited}')
                print(f'directionsIndex: {directionsIndex}')
                directionsIndex.pop(i)
                move = directionList[moveIndex]
                drow, dcol = move
                currRow, currCol = currPos
                self.list[currRow][currCol][moveIndex] = 0
                print(f'knocked down {currRow, currCol, moveIndex}')
                currRow += drow
                currCol += dcol
                if moveIndex < 2:
                    newMove = moveIndex + 2
                else:
                    newMove = moveIndex - 2
                currPos = (currRow, currCol)
                self.list[currRow][currCol][newMove] = 0

                rest = self.generateMaze(visited, currPos)
                if rest != None:
                    return rest
                visited.append(currPos)
                #self.list[currRow][currCol][newMove] = 1
                currRow -= drow
                currCol -= dcol
                currPos = (currRow, currCol)
                print(f'backtrack to {currRow, currCol}')
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

    def __repr__(self):
        return f'{self.list}'
    
    def __eq__(self,other):
        return(isinstance(other, Maze) and self.list == other.list)



        # directionList = [(1,0),(0,-1),(-1,0),(0,1)]
        # if(len(visited) == self.height * self.width):
        #     return 'done'
        # else:
        #     directionsIndex = self.getPossibleDirections(currPos,visited)
        #     temp = set()
        #     while temp != set(directionsIndex):
        #         i = random.randint(0,len(directionsIndex)-1)
        #         moveIndex = directionsIndex[i]
        #         if moveIndex not in temp:
        #             temp.add(moveIndex)
        #             visited.add(currPos)
        #             print(f'currPos: {currPos}')
        #             print(f'visited {visited}')
        #             print(f'directionsIndex: {directionsIndex}')
        #             move = directionList[moveIndex]
        #             drow, dcol = move
        #             currRow, currCol = currPos
        #             self.list[currRow][currCol][moveIndex] = 0
        #             print(f'knocked down {currRow, currCol, moveIndex}')
        #             currRow += drow
        #             currCol += dcol
        #             if moveIndex < 2:
        #                 newMove = moveIndex + 2
        #             else:
        #                 newMove = moveIndex - 2
        #             currPos = (currRow, currCol)
        #             self.list[currRow][currCol][newMove] = 0

        #             rest = self.generateMaze(visited, currPos)
        #             if rest != None:
        #                 return rest
        #             visited.add(currPos)
        #             #self.list[currRow][currCol][newMove] = 1
        #             currRow -= drow
        #             currCol -= dcol
        #             currPos = (currRow, currCol)
        #             print(f'backtrack to {currRow, currCol}')
        #     return None