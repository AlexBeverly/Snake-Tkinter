from tkinter import *
from snake import snake

root = Tk()

board_size = 400
cell_size = board_size/10

s = snake()
board = Canvas(root, height=400, width=400, relief=RAISED)
board.pack()

def draw_snake():
    for row in range(len(s.grid)):
        for col in range(len(s.grid[row])):
            board.create_rectangle(cell_size*row, cell_size*col, cell_size*row + cell_size, cell_size*col + cell_size, fill='red')
draw_snake()


mainloop()