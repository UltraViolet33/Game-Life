from hashlib import new
from math import gamma
from operator import ne
from tkinter import Tk, Canvas
import random

TAILLE = 600


game = []
for i in range(60):
    game.append([0] * 60)

for i in range(500):
    x = random.randint(1, 59)
    y = random.randint(1, 59)
    game[x][y] = 1


def programLoop():
    displayCells()
    evolution()
    window.after(100, programLoop)
    
def countCellsAround(x,y):
    count = 0
    V = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    
    for dx, dy in V:
        count += game[(x+dx)%60][(y+dy)%60]
    return count


def evolution():
    global game
    new_list = []
    for i in range(60):
        new_list.append([0]*60)
        
    for x in range(60):
        for y in range(60):
            nbCells = countCellsAround(x,y)
            if game[x][y] == 0 and nbCells == 3:
                new_list[x][y] = 1
            if game[x][y] == 1 and nbCells in [2, 3]:
                new_list[x][y] = 1
    game = new_list
            
    
    
def displayCells():
    canvas.delete("all")
    for x in range(60):
        for y in range(60):
            if game[x][y] == 1:
                xx = x * 10
                yy = y * 10
                c="black"
                canvas.create_rectangle(xx, yy, xx+10, yy+10, fill=c)


window = Tk()
window.geometry(str(TAILLE) + "x" + str(TAILLE))
canvas = Canvas(window, width=TAILLE, height=TAILLE, borderwidth=0, highlightthickness=0, bg='lightgray')
canvas.pack()
window.after(100, programLoop)
window.mainloop()





