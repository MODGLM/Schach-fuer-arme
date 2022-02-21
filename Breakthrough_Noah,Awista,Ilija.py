import re
import tkinter
from tkinter import *

root=Tk()
root.title('Breakthrough')
canvas = Canvas(root, height= 880, width=880,bg ='#666676')
canvas.pack()

#Horizontal
position = 0
for x in range(12):
    if x == 0:
        position+=40
    elif x == 10:
        position += 40
    elif x == 0:
        continue
    else:
        position += 100
    canvas.create_line(0,position,880,position)
canvas.create_line(0,880,880,880)

#Vertikal
position = 0
for x in range(12):
    if x == 0:
        position+=40
    elif x == 10:
        position += 40
    elif x == 0:
        continue
    else:
        position += 100
    canvas.create_line(position,0,position,880)
canvas.create_line(880,0,880,880)

#Label = ermöglicht es uns etwas ins Fenster hinzuzufügen (wegen root=Tk() Z.4)
#text =  ist...nunja der Text den Einfügen wollen
#front = damit können wir unsere Schrift bearbeiten
#fg = der Vordergrund, also der Text an sich
#bg = der Hintergrund der Schrifft
#Quelle https://www.youtube.com/watch?v=l7ezyYD6V68

def Createletter():
    Buchstaben = 65
    PosX = 90
    PosY = 20
    PosY2 = 860
    for z in range (8):
        canvas.create_text(PosX + z * 100, PosY, text = chr((Buchstaben + z)),fill='white', font=("Arial",15,"bold"))
        canvas.create_text(PosX + z * 100, PosY2, text= chr((Buchstaben + z)),fill='white', font=("Arial",15,"bold"))
Createletter()

def CreateNumber():
    Posx = 20
    Posx2 = 860
    Posy = 90
    for a in range (8):
        canvas.create_text(Posx2, Posy + a * 100, text= (1 + a), fill='white', font=("Arial", 15, "bold"))
        canvas.create_text(Posx, Posy + a * 100, text= (1 + a), fill='white', font=("Arial", 15, "bold"))
CreateNumber()





felder = [[0 for x in range(8)] for y in range(8)]
def mitPlatzhalternFüllen():
    for y in range(8):
        for x in range(8):
            felder[x][y] = 0
mitPlatzhalternFüllen()

"""
1   0   0   0   0   0   0   0   0
2   0   0   0   0   0   0   0   0
3   0   0   0   0   0   0   0   0
4   0   0   0   0   0   0   0   0
5   0   0   0   0   0   0   0   0
6   0   0   0   0   0   0   0   0
7   0   0   0   0   0   0   0   0
8   0   0   0   0   0   0   0   0
"""

def coords(event):
    #2 verschachtelte Schleifen
    #oder 2dim Array z.B. -1 für scharz, für weiß und 0 für leeres Feld
    mousePos = []
    mousePos.append(event.x)
    mousePos.append(event.y)
    calculatePos(mousePos)

def calculatePos(mousePos):
    startPosX = 40
    endPosX = 140
    feldX = 99
    for x in range(8):
        if mousePos[0] > startPosX and mousePos[0] < endPosX:
            feldX = x
            break
        else:
            startPosX = startPosX + 100
            endPosX = endPosX + 100
    startPosY = 40
    endPosY = 140
    feldY = 99
    for y in range(8):
        if mousePos[1] > startPosY and mousePos[1] < endPosY:
            feldY = y
            break
        else:
            startPosY = startPosY+100
            endPosY= endPosY + 100
    pos = []
    pos.append(feldX)
    pos.append(feldY)

    print( "x =" , str(pos[0]))
    print("y =", str(pos[1]))

    """""
    checkIfFieldIsBesetzt(pos)
def checkIfFieldIsBesetzt(angeclicktesFeld):
    if felder[angeclicktesFeld[0]][angeclicktesFeld[1]] == 0:
        print("Frei wie ein Vogel")
        felder[angeclicktesFeld[0]][angeclicktesFeld[1]] = 1
        print("Auf Feld platziert.")
    else:
        print("Besetzt.")
"""""
SpielFiguren = []
Figuren = [[0 for s in range(8)] for w in range(8)]
def DrawBoard():
    colorList = ["white", "#666676"]
    for x in range (8):
        for y in range (8):
            canvas.create_rectangle(40 + x*100, 40 +y*100, 140 + x*100, 140 +y*100, fill=colorList[(x+y)%2])
    for s in range(8):
        for w in range(2):
            Figuren[w][s] = 1
            id = canvas.create_oval(45 + s*100,45 + w*100, 135 + s*100, 135 + w*100, fill = '#404040', width = 2)
            SpielFiguren.append(id)
    for s in range(8):
        for w in range(2):
            Figuren[w][s] = 2
            id = canvas.create_oval(45 + s*100, 645 + w*100, 135 + s*100, 735 + w*100, fill = '#E0E0E0', width = 2)
            SpielFiguren.append(id)

def DrawPiece(player,posX,posY):
    colors = ['#404040','#E0E0E0']
    canvas.create_oval(45 + posX * 100, 45 + posY * 100, 135 + posX * 100, 135 + posY * 100, fill=colors[(player-1)], width=2)
DrawBoard()
#DrawPiece(2,5,5)

#def MovePiece(player,oldPosX,oldPosY,PosY,PosX):

canvas.bind("<Button-1>",coords)

root.mainloop()

