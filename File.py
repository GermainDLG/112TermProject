from cmu_graphics import *
import math

def onAppStart(app):
    app.width = 800
    app.height = 800
    app.horizontalFaces = ['red','blue','green','yellow']
    app.horizCounter = 0
    app.vertCounter = 0
    app.leftFace = app.horizontalFaces[app.horizCounter%4]
    app.rightFace = app.horizontalFaces[(app.horizCounter+1)%4]
    app.backFace = app.horizontalFaces[(app.horizCounter+2)%4]
    app.verticalFaces = ['mediumSeaGreen',app.leftFace,'honeydew',app.backFace]
    app.topFaceFill = app.verticalFaces[0]
    app.frontFaceFill = app.horizontalFaces[0]
    app.rightFaceFill = app.horizontalFaces[1]
    pass

def onKeyPress(app, key):
    if(key == 'w'):
        app.vertCounter += 1

    elif(key == 'd'):
        app.horizCounter -= 1
        app.leftFace = app.horizontalFaces[app.horizCounter%4]
        app.rightFace = app.horizontalFaces[(app.horizCounter+1)%4]
        app.backFace = app.horizontalFaces[(app.horizCounter+2)%4]
        app.verticalFaces = ['mediumSeaGreen',app.leftFace,'honeydew',app.backFace]
    elif(key == 'a'):
        app.horizCounter += 1
        app.leftFace = app.horizontalFaces[app.horizCounter%4]
        app.rightFace = app.horizontalFaces[(app.horizCounter+1)%4]
        app.backFace = app.horizontalFaces[(app.horizCounter+2)%4]
        app.verticalFaces = ['mediumSeaGreen',app.leftFace,'honeydew',app.backFace]
    elif(key == 's'):
        app.vertCounter -= 1


def redrawAll(app):
    drawRect(150,250,400,400,fill=app.horizontalFaces[app.horizCounter%4],border='black')
    drawPolygon(150,250,550,250,650,150,250,150,fill=app.topFaceFill,border='black')
    drawPolygon(550,650,550,250,650,150,650,550,fill=app.horizontalFaces[(app.horizCounter+1)%4],border='black')
def main():
    runApp()

main()