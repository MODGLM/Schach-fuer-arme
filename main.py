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
    if x == 1:
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
    if x == 1:
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

#Zahlen
#wäre mit Schleife halt schon cool von andern Stern
label_8_Links = Label(canvas, text="8", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_8_Rechts = Label(canvas, text="8", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_8_Links.place(x=12,y=77)
label_8_Rechts.place(x=852,y=77)

label_7_Links = Label(canvas, text="7", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_7_Rechts = Label(canvas, text="7", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_7_Links.place(x=12,y=177)
label_7_Rechts.place(x=852,y=177)

label_6_Links = Label(canvas, text="6", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_6_Rechts = Label(canvas, text="6", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_6_Links.place(x=12,y=277)
label_6_Rechts.place(x=852,y=277)

label_5_Links = Label(canvas, text="5", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_5_Rechts = Label(canvas, text="5", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_5_Links.place(x=12,y=377)
label_5_Rechts.place(x=852,y=377)

label_4_Links = Label(canvas, text="4", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_4_Rechts = Label(canvas, text="4", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_4_Links.place(x=12,y=477)
label_4_Rechts.place(x=852,y=477)

label_3_Links = Label(canvas, text="3", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_3_Rechts = Label(canvas, text="3", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_3_Links.place(x=12,y=577)
label_3_Rechts.place(x=852,y=577)

label_2_Links = Label(canvas, text="2", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_2_Rechts = Label(canvas, text="2", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_2_Links.place(x=12,y=677)
label_2_Rechts.place(x=852,y=677)

label_1_Links = Label(canvas, text="1", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_1_Rechts = Label(canvas, text="1", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_1_Links.place(x=12,y=777)
label_1_Rechts.place(x=852,y=777)

#Buchstaben
label_A_Oben = Label(canvas, text="A", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_A_Unten = Label(canvas, text="A", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_A_Oben.place(x=80,y=7)
label_A_Unten.place(x=80,y=847)

label_B_Oben = Label(canvas, text="B", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_B_Unten = Label(canvas, text="B", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_B_Oben.place(x=180,y=7)
label_B_Unten.place(x=180,y=847)

label_C_Oben = Label(canvas, text="C", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_C_Unten = Label(canvas, text="C", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_C_Oben.place(x=280,y=7)
label_C_Unten.place(x=280,y=847)

label_D_Oben = Label(canvas, text="D", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_D_Unten = Label(canvas, text="D", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_D_Oben.place(x=380,y=7)
label_D_Unten.place(x=380,y=847)

label_E_Oben = Label(canvas, text="E", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_E_Unten = Label(canvas, text="E", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_E_Oben.place(x=480,y=7)
label_E_Unten.place(x=480,y=847)

label_F_Oben = Label(canvas, text="F", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_F_Unten = Label(canvas, text="F", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_F_Oben.place(x=580,y=7)
label_F_Unten.place(x=580,y=847)

label_G_Oben = Label(canvas, text="G", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_G_Unten = Label(canvas, text="G", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_G_Oben.place(x=680,y=7)
label_G_Unten.place(x=680,y=847)

label_H_Oben = Label(canvas, text="H", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_H_Unten = Label(canvas, text="H", font=("Arial",15,"bold"),fg="white",bg="#666676")
label_H_Oben.place(x=780,y=7)
label_H_Unten.place(x=780,y=847)

Player1 = 0
Player2 = 0


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

canvas.bind("<Button-1>",coords)

root.mainloop()
