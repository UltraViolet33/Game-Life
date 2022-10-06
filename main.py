from tkinter import Tk, Canvas
import random

cells = []
for i in range(60):
    cells.append([0] * 60)


for i in range(500):
    x = random.randint(1, 59)
    y = random.randint(1, 59)
    cells[x][y] = 1


def programLoop():
    displayCells()
    evolution()
    window.after(100, programLoop)


def displayCells():
    canvas.delete("all")
    for x in range(60):
        for y in range(60):
            if cells[x][y] == 1:
                xx = x * 10
                yy = y * 10
                c = "black"
                canvas.create_rectangle(xx, yy, xx+10, yy+10, fill=c)


def countAliveCellsAround(x, y):
    count = 0
    V = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    for dx, dy in V:
        count += cells[(x+dx) % 60][(y+dy) % 60]
    return count


def evolution():
    global cells
    new_cells_list = []
    for i in range(60):
        new_cells_list.append([0]*60)

    for x in range(60):
        for y in range(60):
            nbAliveCells = countAliveCellsAround(x, y)
            if cells[x][y] == 0 and nbAliveCells == 3:
                new_cells_list[x][y] = 1
            if cells[x][y] == 1 and nbAliveCells in [2, 3]:
                new_cells_list[x][y] = 1
    cells = new_cells_list


window = Tk()
window.geometry(str(600) + "x" + str(600))
canvas = Canvas(window, width=600, height=600, borderwidth=0,
                highlightthickness=0, bg='lightgray')
canvas.pack()
# the programLoop function will be called 100 milliseconds after the program runs
window.after(100, programLoop)
window.mainloop()
