from cmu_graphics import *
from Other_Maze import Maze

def onAppStart(app):
    app.playerLocation = [3,2]
    app.catLocation = [0,0]
    app.collected = 0
    app.gameOver = False
    app.width = 600
    app.height = 600
    app.rows = 5
    app.cols = 5
    app.maze = Maze(app.rows,app.cols)
    app.maze.generateList()
    app.maze.generateMaze(set(),(0,0))
    print(app.maze)

def drawMaze(app, maze):
    for row in range(app.rows):
        for col in range(app.cols):
            if(maze.list[row][col][2] == 1):
                drawLine(50 + (100*col),50 + (100*row),
                        150 + (100*col),50 + (100*row))
            if(maze.list[row][col][1] == 1):
                drawLine(50 + (100*col),50 + (100*row),
                        50 + (100*col),150 + (100*row))
            if(maze.list[row][col][0] == 1):
                drawLine(50 + (100*col), 150 + (100*row),
                         150 + (100*col), 150 + (100*row))
            if(maze.list[row][col][3] == 1):
                drawLine(150 + (100*col), 50 + (100*row),
                         150 + (100*col), 150 + (100*row))

def getCenter(app):
    row, col = app.playerLocation
    center = [100 + (100*col), 100 + (100*row)]
    return(center)

def onKeyPress(app, key):
    if (key == 'w'):
        if(app.maze.list[app.playerLocation[0]][app.playerLocation[1]][2] == 0):
            app.playerLocation[0] -= 1
    elif (key == 'a'):
        if(app.maze.list[app.playerLocation[0]][app.playerLocation[1]][1] == 0):
            app.playerLocation[1] -= 1
    elif (key == 's'):
        if(app.maze.list[app.playerLocation[0]][app.playerLocation[1]][0] == 0):
            app.playerLocation[0] += 1
    elif (key == 'd'):
        if(app.maze.list[app.playerLocation[0]][app.playerLocation[1]][3] == 0):
            app.playerLocation[1] += 1


def redrawAll(app):
    drawMaze(app, app.maze)
    playerCoords = getCenter(app)
    drawCircle(*playerCoords,15)
    #drawCircle()

def main():
    runApp()

main()