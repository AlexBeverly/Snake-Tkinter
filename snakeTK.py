from tkinter import *
from tkinter import messagebox
from snake import snake

# tkinter window
root = Tk()

# snake grid variables
board_size = 400
cell_size = board_size/10
isRunning = False
# changes how much faster snake moves as it gets larger
snake_speed_multiplier = 100

s = snake()
# save the starting length of the snake for later
start_len = s.snake_len
board = Canvas(root, height=board_size + 2, width=board_size + 3)
board.pack()

def draw_snake():
    for row in range(len(s.grid)):
        for col in range(len(s.grid[row])):
            # http://www.science.smith.edu/dftwiki/index.php/File:TkInterColorCharts.png
            if s.grid[row][col] < 0:    # apple
                color = 'red'
            elif s.grid[row][col] > 0:  # snake
                #check if tile is the head of the snake
                if (row,col) == tuple(s.snake_pos):
                    color = 'green4'
                else:
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
    
    if not isRunning:
        isRunning = True
        s.start()
    state = s.move()
    draw_snake()
    if state != 0:
        # subtract wait time from 1 second as the snake gets larger
        wait_time = 1000 - ((s.snake_len - start_len) * snake_speed_multiplier)
        # keep time between steps at 200 or above
        if wait_time < 200:
            wait_time = 200
        board.after(wait_time, step)
    else:
        isRunning = False
        messagebox.showerror('GAME OVER', 'GAME OVER!')

def change_dir(new_dir):
    global isRunning
    # change direction
    s.change_dir(new_dir)
    # start game if not running
    if not isRunning:
        step()

    
    
# testing the step function
#step()

root.bind('<Up>', lambda d:change_dir('N'))
root.bind('<Down>', lambda d:change_dir('S'))
root.bind('<Right>', lambda d:change_dir('E'))
root.bind('<Left>', lambda d:change_dir('W'))

draw_snake()



mainloop()
