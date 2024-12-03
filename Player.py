from cmu_graphics import *
from Other_Maze import Maze
from CatAI import *

# Cat & Mouse Drawing: Ryker Germain (Brother)
#All below images from Pinterest account: Diana C.
#Game Screen Tom & Jerry Background from: https://in.pinterest.com/pin/5629568267946990/
#Start Screen Tom & Jerry Background from: https://in.pinterest.com/pin/tom-and-jerry-life-with-tom-animation-backgrounds--28710516357723207/
#Controls Screen Tom & Jerry Background from: https://in.pinterest.com/pin/739716307527846587/


#Checklist: Add and randomize cheese location, add win/loss screen, cube rotation

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
    app.screen = 'start' #start, game, controls, 2Player, loss, win
    app.stepsPerSecond = 2
    app.mouseRotation = 0

    # **NONE OF THE IMAGES ARE MINE, WORK CITED AT TOP**
    app.catPath = './Images/cat.png'
    app.mousePath = './Images/mouse.png'
    app.backgroundPath = './Images/background.png'
    app.startBackgroundPath = './Images/startBackground.png'
    app.controlsBackgroundPath = './Images/controlBackground.png'

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
                app.mouseRotation = 0
        elif (key == 'a'):
            if(app.maze.list[app.playerLocation[0]][app.playerLocation[1]][1] == 0):
                app.playerLocation[1] -= 1
                app.mouseRotation = 270
        elif (key == 's'):
            if(app.maze.list[app.playerLocation[0]][app.playerLocation[1]][0] == 0):
                app.playerLocation[0] += 1
                app.mouseRotation = 180
        elif (key == 'd'):
            if(app.maze.list[app.playerLocation[0]][app.playerLocation[1]][3] == 0):
                app.playerLocation[1] += 1
                app.mouseRotation = 90
    elif app.screen == '2Player':
        if key == 'w':
            if(app.maze.list[app.playerLocation[0]][app.playerLocation[1]][2] == 0):
                app.playerLocation[0] -= 1
                app.mouseRotation = 0
        elif (key == 'a'):
            if(app.maze.list[app.playerLocation[0]][app.playerLocation[1]][1] == 0):
                app.playerLocation[1] -= 1
                app.mouseRotation = 270
        elif (key == 's'):
            if(app.maze.list[app.playerLocation[0]][app.playerLocation[1]][0] == 0):
                app.playerLocation[0] += 1
                app.mouseRotation = 180
        elif (key == 'd'):
            if(app.maze.list[app.playerLocation[0]][app.playerLocation[1]][3] == 0):
                app.playerLocation[1] += 1
                app.mouseRotation = 90

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
            app.screen = 'loss'
            app.catLocation = [0, 0]
            app.playerLocation = [3, 2]

def onStep(app):
    if app.screen == 'game':
        if app.catLocation == tuple(app.playerLocation):
            app.screen = 'loss'
            app.catLocation = [0, 0]
            app.playerLocation = [3, 2]
        else:
            app.path = specificCost(app.maze.list, tuple(app.catLocation), tuple(app.playerLocation))
            app.paths = BFS(app.maze.list, tuple(app.catLocation))
            app.catLocation = app.path[0]
            if app.catLocation == tuple(app.playerLocation):
                app.screen = 'loss'
                app.catLocation = [0, 0]
                app.playerLocation = [3, 2]

def onMousePress(app, mouseX, mouseY):
    if app.screen == 'start':
        if (inStartBounds(app,mouseX,mouseY) == True):
            app.screen = 'game'
            app.catLocation = [0, 0]
            app.playerLocation = [3, 2]
        elif (in2PlayerBounds(app,mouseX,mouseY) == True):
            app.screen = '2Player'
            app.catLocation = [0, 0]
            app.playerLocation = [3, 2]
        elif(inControlBounds(app,mouseX,mouseY) == True):
            app.screen = 'controls'
    elif app.screen == 'controls':
        if (inBackBounds(app,mouseX,mouseY) == True):
            app.screen = 'start'
    elif app.screen == 'game' or app.screen == '2Player':
        if(0 <= mouseX <= 50) and (0 <= mouseY <= 50):
            app.screen = 'start'
            app.catLocation = [0, 0]
            app.playerLocation = [3, 2]

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
        drawImage(app.startBackgroundPath,0, 0, width = 600, height = 600)
        drawLabel('Cat and Mouse',300,100,size = 60)
        drawLabel('Around the World',300,155,size = 35)
        drawRect(150,250,300,75, fill = 'skyBlue', border = 'black')
        drawLabel('Start',300,287, size = 30)
        drawRect(175,350,250,75, fill = 'lightGreen', border = 'black')
        drawLabel('2 Player',300,387, size = 20)
        drawRect(200,450,200,75,fill= 'crimson', border = 'black')
        drawLabel('Controls',300,487,size=20)

    elif app.screen == 'game' or app.screen == '2Player':
        drawImage(app.backgroundPath, 0, 0, width = 600, height = 600)
        drawRect(50,50,500,500, fill='peru')
        drawMaze(app, app.maze)
        playerCoords = getCenter(app.playerLocation)
        for i in range(len(playerCoords)):
            playerCoords[i] -= 25
        drawImage(app.mousePath, *playerCoords, width = 50, height = 50, rotateAngle = app.mouseRotation)
        catCoords = getCenter(app.catLocation)
        for i in range(len(catCoords)):
            catCoords[i] -= 25
        drawImage(app.catPath, *catCoords, width = 50, height = 50)

    elif app.screen == 'controls':
        drawImage(app.controlsBackgroundPath,0,0, width = 600, height = 600)
        drawRect(200,500,200,50,fill='beige',border = 'black')
        drawLabel('Back',300,525,size=20)
        drawRect(25,50,275, 334, fill = 'beige', border = 'black')
        drawRect(310,50,275,334, fill = 'beige', border = 'black')
        drawLabel('W/Up',63,88, size = 30)
        drawLabel('A/Left', 63, 174, size = 30)
        drawLabel('S/Down', 63, 260, size = 30)
        drawLabel('D/Right', 63, 346, size = 30)
        drawLabel('Moves the mouse/cat up', 200, 88, size = 16)
        drawLabel('Moves the mouse/cat left',200,174, size = 16)
        drawLabel('Moves the mouse/cat down',200,260, size = 16)
        drawLabel('Moves the mouse/cat right', 200, 346, size = 16)
        drawLabel('Objective:',447.5, 75, size = 30)
        drawLabel('Welcome to the game of Cat & Mouse!',448,115,size = 15)
        drawLabel('Your objective is simple:', 448, 140, size = 15)
        drawLabel(' Collect 6 Cheese',448, 165, size=15, bold = True)
        drawLabel('Watch out though!',448, 190, size=15)
        drawLabel('If you get touched by the cat,',448,215,size=15)
        drawLabel('Its game over...',448,240,size = 15)
        drawLabel('Have fun!!',448, 265, size = 15)

    elif app.screen == 'loss':
        pass
def main():

    runApp()

main()