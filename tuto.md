## Let's create game life in Python !

Game of life (which is not a game) is a good programming excercises and it is quite funny.

This cellular automation was invented by a mathematician named John Conway.

This is very easy to understand : it consists of a grid of cells which can live, die or multiply based on two rules.

1 - Each cell with one or two neigbhors die by soliture
2 - Each cell with four or more neigbhors dies by overpopulation
3 - Each cells with two or three neigbors survives

You can have more informations <a href="https://playgameoflife.com/info">here</a>.

Let's create it !


We will use Python, so basics of Python are required.
To create a GUI (graphical user interface), we will use the Pythob library Tkinter.
More infos about tkinter <a href="https://docs.python.org/fr/3/library/tkinter.html">here</a>.

### Create the GUI

Create a python file, you can name it main.py or any other name.

```python
from tkinter import Tk, Canvas

window = Tk()
window.geometry(str(1100) + "x" + str(600))
canvas = Canvas(window, width=1100, height=600, borderwidth=0, highlightthickness=0, bg='lightgray')
canvas.pack()
# window.after(100, programLoop)
window.mainloop()
```

Here we create a window with tkinter of 1100 by 600 and a canvas 