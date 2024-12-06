from cmu_graphics import *
from Other_Maze import *
from CatAI import *
import random

# Cat & Mouse Drawing: Ryker Germain (Brother)
#All below images from Pinterest account: Diana C.
#Game Screen Tom & Jerry Background from: https://in.pinterest.com/pin/5629568267946990/
#Start Screen Tom & Jerry Background from: https://in.pinterest.com/pin/tom-and-jerry-life-with-tom-animation-backgrounds--28710516357723207/
#Controls Screen Tom & Jerry Background from: https://in.pinterest.com/pin/739716307527846587/
#Win Screen Tom & Jerry Background from: https://in.pinterest.com/pin/749990144227580505/
#Loss Screen Tom & Jerry Background from: https://in.pinterest.com/pin/tom-jerry-casanova-cat-animation-backgrounds--492370171755936393/

def onAppStart(app):
    app.playerLocation = [3, 2]
    app.catLocation = [0, 0]
    app.width = 600
    app.height = 600
    app.rows = 5 
    app.cols = 5
    app.maze1 = Maze(app.rows,app.cols)
    app.maze2 = Maze(app.rows,app.cols)
    app.maze3 = Maze(app.rows,app.cols)
    app.maze4 = Maze(app.rows,app.cols)
    app.maze5 = Maze(app.rows,app.cols)
    app.maze6 = Maze(app.rows,app.cols)
    mazeSetup(app.maze1)
    mazeSetup(app.maze2)
    mazeSetup(app.maze3)
    mazeSetup(app.maze4)
    mazeSetup(app.maze5)
    mazeSetup(app.maze6)
    app.maze1.surrounding = [app.maze3, app.maze2, app.maze6, app.maze4]
    app.maze2.surrounding = [app.maze5, app.maze6, app.maze1, app.maze3]
    app.maze3.surrounding = [app.maze5, app.maze2, app.maze1, app.maze4]
    app.maze4.surrounding = [app.maze5, app.maze3, app.maze1, app.maze6]
    app.maze5.surrounding = [app.maze6, app.maze2, app.maze3, app.maze4]
    app.maze6.surrounding = [app.maze1, app.maze2, app.maze5, app.maze4]
    app.possible6Surrounding = [[app.maze1, app.maze2, app.maze5, app.maze4],
                                [app.maze5, app.maze4, app.maze1, app.maze2]]
    app.mazeList = [app.maze1, app.maze2, app.maze3, app.maze4, app.maze5, app.maze6]
    app.currMaze = app.maze3
    app.newSurrounding = []
    app.path = specificCost(app.currMaze.list, tuple(app.catLocation), tuple(app.playerLocation))
    app.paths = BFS(app.currMaze.list, tuple(app.catLocation))
    app.screen = 'start' #start, game, controls, 2Player, loss, win
    app.stepsPerSecond = 0.75
    app.mouseRotation = 0
    app.numCheese = 30
    app.cheeseList = dict()
    app.trueCheese = dict()
    app.collected = 0
    cheeseCoords(app)

    # Only the cheese was drawn by me, all other images cited at the top
    app.catPath = './Images/cat.png'
    app.mousePath = './Images/mouse.png'
    app.backgroundPath = './Images/background.png'
    app.startBackgroundPath = './Images/startBackground.png'
    app.controlsBackgroundPath = './Images/controlBackground.png'
    app.winBackgroundPath =  './Images/winBackground.png'
    app.lossBackgroundPath = './Images/lossBackground.png'
    app.cheesePath = './Images/cheese.png'

def reset(app):
    app.playerLocation = [3, 2]
    app.catLocation = [0, 0]
    app.width = 600
    app.height = 600
    app.rows = 5 
    app.cols = 5
    app.maze1 = Maze(app.rows,app.cols)
    app.maze2 = Maze(app.rows,app.cols)
    app.maze3 = Maze(app.rows,app.cols)
    app.maze4 = Maze(app.rows,app.cols)
    app.maze5 = Maze(app.rows,app.cols)
    app.maze6 = Maze(app.rows,app.cols)
    mazeSetup(app.maze1)
    mazeSetup(app.maze2)
    mazeSetup(app.maze3)
    mazeSetup(app.maze4)
    mazeSetup(app.maze5)
    mazeSetup(app.maze6)
    app.maze1.surrounding = [app.maze3, app.maze2, app.maze6, app.maze4]
    app.maze2.surrounding = [app.maze5, app.maze6, app.maze1, app.maze3]
    app.maze3.surrounding = [app.maze5, app.maze2, app.maze1, app.maze4]
    app.maze4.surrounding = [app.maze5, app.maze3, app.maze1, app.maze6]
    app.maze5.surrounding = [app.maze6, app.maze2, app.maze3, app.maze4]
    app.maze6.surrounding = [app.maze1, app.maze2, app.maze5, app.maze4]
    app.possible6Surrounding = [[app.maze1, app.maze2, app.maze5, app.maze4],
                                [app.maze5, app.maze4, app.maze1, app.maze2]]
    app.mazeList = [app.maze1, app.maze2, app.maze3, app.maze4, app.maze5, app.maze6]
    app.currMaze = app.maze3
    app.newSurrounding = []
    app.path = specificCost(app.currMaze.list, tuple(app.catLocation), tuple(app.playerLocation))
    app.paths = BFS(app.currMaze.list, tuple(app.catLocation))
    app.screen = 'start' #start, game, controls, 2Player, loss, win
    app.stepsPerSecond = 0.75
    app.mouseRotation = 0
    app.numCheese = 30
    app.cheeseList = dict()
    app.trueCheese = dict()
    app.collected = 0
    cheeseCoords(app)

def mazeSetup(maze):
    maze.generateList()
    maze.generateMaze([],(0,0))

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

def getNum(bigList, startingRow, startingCol, endingRow, endingCol):
    tempRow = None
    tempList = []
    result = []
    for row in range(startingRow, endingRow+1):
        for col in range(startingCol, endingCol+1):
            if tempRow == None:
                tempRow = row
            if tempRow == row:
                tempList.append(bigList[row][col])
            elif tempRow != row:
                result.append(tempList)
                tempRow = row
                tempList = []
                tempList.append(bigList[row][col])
    result.append(tempList)
    return(result)

def getCenter(coordinates):
    row, col = coordinates[0], coordinates[1]
    center = [100 + (100*col), 100 + (100*row)]
    return(center)

def cheeseCoords(app):
    for ___ in range(app.numCheese):
        random, mazeNum = generateRandom(app)
        centerX, centerY = getCenter(random)
        leftX = centerX - 25
        topY = centerY - 25
        if mazeNum not in app.cheeseList:
            app.cheeseList[mazeNum] = [(centerX, centerY)]
            app.trueCheese[mazeNum] = [(leftX, topY)]
        else:
            app.cheeseList[mazeNum].append((centerX, centerY))
            app.trueCheese[mazeNum].append((leftX, topY))

def generateRandom(app):
    randomX = random.randint(0,app.rows-1)
    randomY = random.randint(0,app.cols-1)
    randomNum = random.randint(1,6)
    return ((randomX, randomY), randomNum)

def numAssigner(app, num):
    result = None
    if num == app.maze1:
        result = 1
    elif num == app.maze2:
        result = 2
    elif num == app.maze3:
        result = 3
    elif num == app.maze4:
        result = 4
    elif num == app.maze5:
        result = 5
    elif num == app.maze6:
        result = 6
    return result

def onKeyPress(app, key):
    temp = app.currMaze
    tempNum = numAssigner(app, temp)
    if key == 'r':
        reset(app)
    if app.screen == 'game':
        if (key == 'w'):
            if (app.playerLocation[0]-1) < 0:
                leftMaze = app.currMaze.surrounding[1]
                rightMaze = app.currMaze.surrounding[3]
                if leftMaze == app.maze6:
                    leftMaze = app.possible6Surrounding[1]
                    leftMaze.insert(0,leftMaze.pop())
                else: leftMaze.surrounding.insert(0,leftMaze.surrounding.pop())
                if rightMaze == app.maze6:
                    rightMaze = app.possible6Surrounding[1]
                    rightMaze.append(rightMaze.pop(0))
                else: rightMaze.surrounding.append(rightMaze.surrounding.pop(0))
                app.currMaze = temp.surrounding[2]
                app.playerLocation[0] = 4
                catX, catY = app.catLocation
                app.catLocation = (4, catY)
                if app.catLocation == tuple(app.playerLocation):
                    app.playerLocation[0] = 3
                app.maze6.surrounding = app.possible6Surrounding[0]
            elif(app.currMaze.list[app.playerLocation[0]][app.playerLocation[1]][2] == 0):
                app.playerLocation[0] -= 1
                app.mouseRotation = 0
        elif (key == 'a'):
            if (app.playerLocation[1]-1) < 0:
                topMaze = app.currMaze.surrounding[2]
                bottomMaze = app.currMaze.surrounding[0]
                if topMaze == app.maze6:
                    topMaze = app.possible6Surrounding[0]
                    topMaze.append(topMaze.pop(0))
                else: topMaze.surrounding.append(topMaze.surrounding.pop(0))
                if bottomMaze == app.maze6:
                    bottomMaze = app.possible6Surrounding[0]
                    bottomMaze.insert(0,bottomMaze.pop())
                else: bottomMaze.surrounding.insert(0, bottomMaze.surrounding.pop())
                app.currMaze = temp.surrounding[1]
                app.maze6.surrounding = app.possible6Surrounding[1]
                app.playerLocation[1] = 4
                catX, catY = app.catLocation
                app.catLocation = (catX, 4)
                if app.catLocation == tuple(app.playerLocation):
                    app.playerLocation[1] = 3
            elif(app.currMaze.list[app.playerLocation[0]][app.playerLocation[1]][1] == 0):
                app.playerLocation[1] -= 1
                app.mouseRotation = 270
        elif (key == 's'):
            if (app.playerLocation[0] + 1) > 4:
                leftMaze = app.currMaze.surrounding[1]
                rightMaze = app.currMaze.surrounding[3]
                if leftMaze == app.maze6:
                    leftMaze = app.possible6Surrounding[1]
                    leftMaze.append(leftMaze.pop(0))
                else: leftMaze.surrounding.append(leftMaze.surrounding.pop(0))
                if rightMaze == app.maze6:
                    rightMaze = app.possible6Surrounding[1]
                    rightMaze.insert(0,rightMaze.pop())
                else: rightMaze.surrounding.insert(0,rightMaze.surrounding.pop())
                app.currMaze = temp.surrounding[0]
                app.maze6.surrounding = app.possible6Surrounding[0]
                app.playerLocation[0] = 0
                catX, catY = app.catLocation
                app.catLocation = (0, catY)
                if app.catLocation == tuple(app.playerLocation):
                    app.playerLocation[0] = 1
            elif(app.currMaze.list[app.playerLocation[0]][app.playerLocation[1]][0] == 0):
                app.playerLocation[0] += 1
                app.mouseRotation = 180
        elif (key == 'd'):
            if (app.playerLocation[1] + 1) > 4:
                topMaze = app.currMaze.surrounding[2]
                bottomMaze = app.currMaze.surrounding[0]
                if topMaze == app.maze6:
                    topMaze = app.possible6Surrounding[0]
                    topMaze.insert(0,topMaze.pop())
                else: topMaze.surrounding.insert(0, topMaze.surrounding.pop())
                if bottomMaze == app.maze6:
                    bottomMaze = app.possible6Surrounding[0]
                    bottomMaze.append(bottomMaze.pop(0))
                else: bottomMaze.surrounding.append(bottomMaze.surrounding.pop(0))
                app.currMaze = temp.surrounding[3]
                app.maze6.surrounding = app.possible6Surrounding[1]
                app.playerLocation[1] = 0
                catX, catY = app.catLocation
                app.catLocation = (catX, 0)
                if app.catLocation == tuple(app.playerLocation):
                    app.playerLocation[1] = 1
            elif(app.currMaze.list[app.playerLocation[0]][app.playerLocation[1]][3] == 0):
                app.playerLocation[1] += 1
                app.mouseRotation = 90
    elif app.screen == '2Player':
        if key == 'w':
            if(app.currMaze.list[app.playerLocation[0]][app.playerLocation[1]][2] == 0):
                app.playerLocation[0] -= 1
                app.mouseRotation = 0
        elif (key == 'a'):
            if(app.currMaze.list[app.playerLocation[0]][app.playerLocation[1]][1] == 0):
                app.playerLocation[1] -= 1
                app.mouseRotation = 270
        elif (key == 's'):
            if(app.currMaze.list[app.playerLocation[0]][app.playerLocation[1]][0] == 0):
                app.playerLocation[0] += 1
                app.mouseRotation = 180
        elif (key == 'd'):
            if(app.currMaze.list[app.playerLocation[0]][app.playerLocation[1]][3] == 0):
                app.playerLocation[1] += 1
                app.mouseRotation = 90
        catX, catY = app.catLocation
        if key == 'up':
            if(app.currMaze.list[app.catLocation[0]][app.catLocation[1]][2] == 0):
                app.catLocation = (catX-1, catY)
        elif key == 'down':
            if(app.currMaze.list[app.catLocation[0]][app.catLocation[1]][0] == 0):
                app.catLocation = (catX + 1, catY)
        elif key == 'left':
            if(app.currMaze.list[app.catLocation[0]][app.catLocation[1]][1] == 0):
                app.catLocation = (catX, catY - 1)
        elif key == 'right':
            if(app.currMaze.list[app.catLocation[0]][app.catLocation[1]][3] == 0):
                app.catLocation = (catX, catY + 1)
        if(app.playerLocation == app.catLocation):
            app.screen = 'loss'
            app.height = 600
            app.width = 600
    mazeKey = numAssigner(app, app.currMaze)
    for cheese in app.cheeseList[mazeKey]:
        if mazeKey not in app.cheeseList:
            continue
        if cheese == tuple(getCenter(app.playerLocation)):
            index = app.cheeseList[mazeKey].index(cheese)
            app.cheeseList[mazeKey].pop(index)
            cheeseX, cheeseY = cheese
            cheeseX -= 25
            cheeseY -= 25
            index = app.trueCheese[mazeKey].index((cheeseX, cheeseY))
            app.trueCheese[mazeKey].pop(index)
            app.collected += 1
            if app.screen == '2Player' and app.cheeseList[3] == []:
                app.screen = 'win'
                app.width = 600
                app.height = 600
    if app.collected == app.numCheese:
        app.screen = 'win'

def onStep(app):
    if app.screen == 'game':
        if app.catLocation == tuple(app.playerLocation):
            app.screen = 'loss'
            app.width = 600
            app.height = 600
        else:
            app.path = specificCost(app.currMaze.list, tuple(app.catLocation), tuple(app.playerLocation))
            app.paths = BFS(app.currMaze.list, tuple(app.catLocation))
            app.catLocation = app.path[0]
            if app.catLocation == tuple(app.playerLocation):
                app.screen = 'loss'
                app.width = 600
                app.height = 600

def onMousePress(app, mouseX, mouseY):
    if app.screen == 'start':
        if (inStartBounds(app,mouseX,mouseY) == True):
            app.screen = 'game'
            app.width = 700
            app.height = 700
        elif (in2PlayerBounds(app,mouseX,mouseY) == True):
            app.screen = '2Player'
            app.width = 700
            app.height = 700
        elif(inControlBounds(app,mouseX,mouseY) == True):
            app.screen = 'controls'
        elif(inDifficultyBounds(app,mouseX,mouseY) == True):
            if(app.stepsPerSecond == 1):
                app.stepsPerSecond = 1.25
            elif(app.stepsPerSecond == 1.25):
                app.stepsPerSecond = 0.75
            elif(app.stepsPerSecond == 0.75):
                app.stepsPerSecond = 1
    elif app.screen == 'controls':
        if (inControlsBackBounds(app,mouseX,mouseY) == True):
            app.screen = 'start'
    elif app.screen == 'game' or app.screen == '2Player':
        if(0 <= mouseX <= 50) and (0 <= mouseY <= 50):
            app.screen = 'start'
            app.width = 600
            app.height = 600
    elif app.screen == 'loss' or app.screen == 'win':
        if(inLossBounds(app,mouseX,mouseY) == True):
            app.screen = 'start'
            reset(app)

def inControlsBackBounds(app, mouseX, mouseY):
    return(200 <= mouseX <= 400) and (500 <= mouseY <= 550)

def inStartBounds(app, mouseX, mouseY):
    return(150 <= mouseX <= 450) and (250 <= mouseY <= 325)

def in2PlayerBounds(app, mouseX, mouseY):
    return (175 <= mouseX <= 425) and (350 <= mouseY <= 425)

def inControlBounds(app, mouseX, mouseY):
    return (200 <= mouseX <= 400) and (450 <= mouseY <= 525)

def inLossBounds(app,mouseX,mouseY):
    return (150 <= mouseX <= 450) and (250 <= mouseY <= 350)

def inDifficultyBounds(app,mouseX,mouseY):
    return (35 <= mouseX <= 135) and (450 <= mouseY <550)

def redrawAll(app): 
    temp = numAssigner(app, app.currMaze)
    diffFill = None
    if app.screen == 'start':
        drawImage(app.startBackgroundPath,0, 0, width = 600, height = 600)
        drawLabel('Cat and Mouse',300,100,size = 60, font = 'Fontdiner Swanky')
        drawLabel('Around the World',300,155,size = 35, font = 'Fontdiner Swanky')
        drawRect(150,250,300,75, fill = 'skyBlue', border = 'black')
        drawLabel('Start',300,287, size = 30, font = 'Fontdiner Swanky')
        drawRect(175,350,250,75, fill = 'lightGreen', border = 'black')
        drawLabel('2 Player',300,387, size = 20, font = 'Fontdiner Swanky')
        drawRect(200,450,200,75,fill= 'crimson', border = 'black')
        drawLabel('Controls',300,487,size=20, font = 'Fontdiner Swanky')
        if(app.stepsPerSecond == 1.25):
            diffFill = 'red'
            difficulty = 'hard'
        elif(app.stepsPerSecond == 1):
            diffFill = 'gold'
            difficulty = 'medium'
        elif(app.stepsPerSecond == 0.75):
            diffFill = 'limeGreen'
            difficulty = 'easy'
        drawRect(35,450,100,100,fill = diffFill,border = 'black')
        drawLabel(difficulty,85,500,size = 22, font = 'Fontdiner Swanky')

    elif app.screen == 'game' or app.screen == '2Player':
        drawImage(app.backgroundPath, 0, 0, width = 700, height = 700)
        drawRect(50,50,500,500, fill='peru')
        drawMaze(app, app.currMaze)
        playerCoords = getCenter(app.playerLocation)
        for coordinates in app.trueCheese[temp]:
            drawImage(app.cheesePath,*coordinates,width = 50, height = 50)
        for i in range(len(playerCoords)):
            playerCoords[i] -= 25
        drawImage(app.mousePath, *playerCoords, width = 50, height = 50, rotateAngle = app.mouseRotation)
        catCoords = getCenter(app.catLocation)
        for i in range(len(catCoords)):
            catCoords[i] -= 25
        drawImage(app.catPath, *catCoords, width = 50, height = 50)
        if temp == 1: drawRect(575,510,40,40,fill='red', border = 'black') #Face 1
        elif temp == 2: drawRect(530,555,40,40,fill='red', border = 'black') #Face 2
        elif temp == 3: drawRect(575,555,40,40,fill='red', border = 'black') #Face 3
        elif temp == 4: drawRect(620,555,40,40,fill='red', border = 'black') #Face 4
        elif temp == 5: drawRect(575,600,40,40,fill='red', border = 'black') #Face 5
        elif temp == 6: drawRect(575,645,40,40,fill='red', border = 'black') #Face 6
        drawRect(575,510,40,40,fill=None, border = 'black') #Face 1
        drawRect(530,555,40,40,fill=None, border = 'black') #Face 2
        drawRect(575,555,40,40,fill=None, border = 'black') #Face 3
        drawRect(620,555,40,40,fill=None, border = 'black') #Face 4
        drawRect(575,600,40,40,fill=None, border = 'black') #Face 5
        drawRect(575,645,40,40,fill=None, border = 'black') #Face 6
        if app.screen == 'game':
            drawLabel(f'Cheese Left: {30-app.collected}',200,595,size = 25,font = 'Fontdiner Swanky')
        elif app.screen == '2Player':
            drawLabel(f'Cheese Left: {len(app.trueCheese[temp])}',200,595,size = 25,font = 'Fontdiner Swanky')

    elif app.screen == 'controls':
        drawImage(app.controlsBackgroundPath,0,0, width = 600, height = 600)
        drawRect(200,500,200,50,fill='beige',border = 'black')
        drawLabel('Back',300,525,size=20, font = 'Fontdiner Swanky')
        drawRect(25,50,275, 334, fill = 'beige', border = 'black')
        drawRect(310,50,275,334, fill = 'beige', border = 'black')
        drawLabel('W',63,88, size = 30, font = 'Fontdiner Swanky')
        drawLabel('A', 63, 174, size = 30, font = 'Fontdiner Swanky')
        drawLabel('S', 63, 260, size = 30, font = 'Fontdiner Swanky')
        drawLabel('D', 63, 346, size = 30, font = 'Fontdiner Swanky')
        drawLabel('Moves the mouse up', 200, 88, size = 15, font = 'Fontdiner Swanky')
        drawLabel('Moves the mouse left',200,174, size = 15, font = 'Fontdiner Swanky')
        drawLabel('Moves the mouse down',200,260, size = 15, font = 'Fontdiner Swanky')
        drawLabel('Moves the mouse right', 200, 346, size = 15, font = 'Fontdiner Swanky')
        drawLabel('Objective:',447.5, 75, size = 30, font = 'Fontdiner Swanky')
        drawLabel('Welcome to the game of Cat & Mouse!',448,115,size = 13, font = 'Fontdiner Swanky')
        drawLabel('Your objective is simple:', 448, 140, size = 14, font = 'Fontdiner Swanky')
        drawLabel(' Collect all the Cheese',448, 165, size=14, bold = True, font = 'Fontdiner Swanky')
        drawLabel('Watch out though!',448, 190, size=14, font = 'Fontdiner Swanky')
        drawLabel('If you get touched by the cat,',448,215,size=14, font = 'Fontdiner Swanky')
        drawLabel('Its game over...',448,240,size = 14, font = 'Fontdiner Swanky')
        drawLabel('Have fun!!',448, 265, size = 14, font = 'Fontdiner Swanky')
        drawLabel('(PS. You might want to try', 448, 290, size = 14, font = 'Fontdiner Swanky')
        drawLabel('and sneak UNDER the mouse)', 448, 315, size = 14, font = 'Fontdiner Swanky')

    elif app.screen == 'loss':
        drawImage(app.lossBackgroundPath,0,0,width = 600, height = 600)
        drawRect(150,250,300,100,fill='beige', border='black')
        drawLabel('The Cat Caught You :(', 300,100,size=45, bold = True, font = 'Fontdiner Swanky')
        drawLabel('Try Again?',300,300, size = 30, font = 'Fontdiner Swanky')

    elif app.screen == 'win':
        drawImage(app.winBackgroundPath,0,0,width = 600, height = 600)
        drawRect(150,250,300,100,fill='beige', border='black')
        drawLabel('You Got All The Cheese!', 300,150,size=40, bold = True, font = 'Fontdiner Swanky')
        drawLabel('Go Again??',300,300, size = 30, font = 'Fontdiner Swanky')

def main():

    runApp()

main()