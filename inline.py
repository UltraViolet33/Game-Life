from tkinter import Tk, Canvas
import random


window = Tk()
window.geometry(str(1100) + "x" + str(600))
canvas = Canvas(window, width=1100, height=600, borderwidth=0, highlightthickness=0, bg='lightgray')
canvas.pack()
# window.after(100, programLoop)
window.mainloop()