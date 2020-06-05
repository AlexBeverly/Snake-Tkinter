from tkinter import *
from snake import snake

# tkinter window
root = Tk()

# snake grid variables
board_size = 400
cell_size = board_size/10
isRunning = False

s = snake()
board = Canvas(root, height=board_size + 2, width=board_size + 3)
board.pack()

def draw_snake():
    for row in range(len(s.grid)):
        for col in range(len(s.grid[row])):
            # http://www.science.smith.edu/dftwiki/index.php/File:TkInterColorCharts.png
            if s.grid[row][col] < 0:    # apple
                color = 'red'
            elif s.grid[row][col] > 0:  # snake
                color = 'green2'
            else:                       # empty
                color = 'snow'

            board.create_rectangle(
                2 + cell_size*row, cell_size*col, # starting point
                3 + cell_size*row + cell_size, cell_size*col + cell_size, # ending point
                fill = color, #fill color
                #outline = color,
                width=1 # remove border
            )

def step():
    global isRunning
    global board
    if isRunning:
        state = s.move()
        draw_snake()
        if state != 0:
            board.after(1000, step)
        else:
            isRunning = False
    else:
        isRunning = True
        s.start()
    
step()
board.after(2000, step)
board.after(10000, step)
board.after(11000, step)

mainloop()
