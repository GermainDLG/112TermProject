from cmu_graphics import *
from Other_Maze import Maze
from CatAI import *

def onAppStart(app):
    app.playerLocation = [3, 2]
    app.catLocation = [0, 0]
    app.collected = 0
    app.gameOver = False
    app.width = 600
    app.height = 600
    app.rows = 5 #MAKE EACHS SQUARE SMALLER PLEEEEEEEEEEEEEEEEEEEEEEEEEEASE
    app.cols = 5
    app.maze = Maze(app.rows,app.cols)
    app.maze.generateList()
    app.maze.generateMaze()
    app.path = specificCost(app.maze.list, tuple(app.catLocation), tuple(app.playerLocation))
    app.paths = BFS(app.maze.list, tuple(app.catLocation))
    app.screen = 'start' #start, game, controls
    app.stepsPerSecond = 1

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

def getCenter(coordinates):
    row, col = coordinates[0], coordinates[1]
    center = [100 + (100*col), 100 + (100*row)]
    return(center)

def onKeyPress(app, key):
    if app.screen == 'game':
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
    elif app.screen == '2Player':
        if key == 'w':
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

        if key == 'up':
            if(app.maze.list[app.catLocation[0]][app.catLocation[1]][2] == 0):
                app.catLocation[0] -= 1
        elif key == 'down':
            if(app.maze.list[app.catLocation[0]][app.catLocation[1]][0] == 0):
                app.catLocation[0] += 1
        elif key == 'left':
            if(app.maze.list[app.catLocation[0]][app.catLocation[1]][1] == 0):
                app.catLocation[1] -= 1
        elif key == 'right':
            if(app.maze.list[app.catLocation[0]][app.catLocation[1]][3] == 0):
                app.catLocation[1] += 1
        if(app.playerLocation == app.catLocation):
            app.screen = 'start'

def onStep(app):
    if app.screen == 'game':
        if app.catLocation == tuple(app.playerLocation):
            app.screen = 'start'
            app.catLocation = [0, 0]
        else:
            app.path = specificCost(app.maze.list, tuple(app.catLocation), tuple(app.playerLocation))
            app.paths = BFS(app.maze.list, tuple(app.catLocation))
            app.catLocation = app.path[0]
            print(app.catLocation, app.playerLocation)

def onMousePress(app, mouseX, mouseY):
    if app.screen == 'start':
        if (inStartBounds(app,mouseX,mouseY) == True):
            app.screen = 'game'
        elif (in2PlayerBounds(app,mouseX,mouseY) == True):
            app.screen = '2Player'
        elif(inControlBounds(app,mouseX,mouseY) == True):
            app.screen = 'controls'
    elif app.screen == 'controls':
        if (inBackBounds(app,mouseX,mouseY) == True):
            app.screen = 'start'
    elif app.screen == 'game' or app.screen == '2Player':
        if(0 <= mouseX <= 50) and (0 <= mouseY <= 50):
            app.screen = 'start'
            app.catLocation = [0, 0]

def inBackBounds(app, mouseX, mouseY):
    return(200 <= mouseX <= 400) and (500 <= mouseY <= 550)

def inStartBounds(app, mouseX, mouseY):
    return(150 <= mouseX <= 450) and (250 <= mouseY <= 325)

def in2PlayerBounds(app, mouseX, mouseY):
    return (175 <= mouseX <= 425) and (350 <= mouseY <= 425)

def inControlBounds(app, mouseX, mouseY):
    return (200 <= mouseX <= 400) and (450 <= mouseY <= 525)

def redrawAll(app): 
    if app.screen == 'start':
        #drawRect(100,100,400,100)
        drawLabel('Cat and Mouse',300,100,size = 60)
        drawLabel('Around the World',300,155,size = 35)
        drawRect(150,250,300,75, fill = None, border = 'black')
        drawLabel('Start',300,287, size = 30)
        drawRect(175,350,250,75, fill = None, border = 'black')
        drawLabel('2 Player',300,387, size = 20)
        drawRect(200,450,200,75,fill= None, border = 'black')
        drawLabel('Controls',300,487,size=20)

    elif app.screen == 'game' or app.screen == '2Player':
        drawMaze(app, app.maze)
        playerCoords = getCenter(app.playerLocation)
        drawCircle(*playerCoords,15,fill='green')
        catCoords = getCenter(app.catLocation)
        drawCircle(*catCoords, 15, fill = 'red')

    
    elif app.screen == 'controls':
        drawRect(200,500,200,50,fill=None,border = 'black')
        drawLabel('Back',300,525,size=20)

def main():
    runApp()

main()