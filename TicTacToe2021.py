from tkinter import *
import tkinter.messagebox

root = Tk() #zwischen Zeile 4 und 8 -> Endlosschleife
root.title("Tic Tac Toe")
canvas = Canvas(root, height=300, width=300, bg='#ffdead')
canvas.pack()
canvas.create_line(0,100,300,100)
canvas.create_line(0,200,300,200)
canvas.create_line(100,0,100,300)
canvas.create_line(200,0,200,300)
c = 0   #counter
History = []
matt = [7, 56, 448, 73, 146, 292, 273, 84]
Player1 = 0
Player2 = 0

def Pos2Index(event = NONE):
    x = int(event.x / 100)
    y = int(event.y / 100)
    Feld = x + 3 * y
    return Feld

def Index2Pos(event=NONE):
    for i in range(9):
        if Pos2Index(event) == i:
            x = i%3*100
            y = int(i/3)%3*100
            return(x,y) #Tupel

def SetSign(event):
    global c, Player1, Player2
    x = Index2Pos(event)[0]
    y = Index2Pos(event)[1]
    if (Pos2Index(event) in History) == False:
        History.append(Pos2Index(event))
        print(History)
        for i in range(len(History)):
            if i % 2 == 0:
                Player1 = Player1 + 2 ** History[i]
            else:
                Player2 = Player2 + 2 ** History[i]
        if c % 2 == 0:
            canvas.create_oval(x + 10, y + 10, x + 90, y + 90, width=4)
        else:
            canvas.create_line(x + 10, y + 10, x + 90, y + 90, width=4)
            canvas.create_line(x + 10, y + 90, x + 90, y + 10, width=4)
        c = c + 1
    print('Player1: ',Player1)
    print('Player2: ',Player2)
    for i in matt:
        if Player1 & i == i:
            tkinter.messagebox.showinfo('TTT', 'Kreis hat gewonnen, Bratan')
            root.quit()
        if Player2 & i == i:
            tkinter.messagebox.showinfo('TTT', 'Kreuz hat gewonnen, Bratan')
            root.quit()
    Player1 = 0
    Player2 = 0

#Liste anlegen namens History
#nach jedem Click wird die Liste um den Eintrag Pos2Index() erweitert
#z.B. History = [0,4,8]

def coords(event=NONE):
    Index2Pos(event)
    SetSign(event)

canvas.bind("<Button-1>",coords)
root.mainloop()