from random import randint


class snake:
    # class variables
    dirs = ('N', 'S', 'E', 'W')
    cur_dir = 'E'
    snake_len = 3
    start_point = (5, 5)
    snake_pos = list(start_point)

    # snake grid list
    grid = []

    def __init__(self):
        # fill grid with lists of 10 0s
        for each in range(10):
            x = []
            for each in range(10):
                x.append(0)
            self.grid.append(x)

    # function to run when starting game
    def start(self):
        # place snake
        self.grid[self.start_point[0]][self.start_point[1]] = self.snake_len
        # place fruit
        self.place_fruit()

    def place_fruit(self):
        # get random fruit location
        fruit_location = (randint(0, 9), randint(0, 9))
        # keep getting random fruit location until it's not the same space as the snake
        while self.grid[fruit_location[0]][fruit_location[1]] != 0:
            fruit_location = (randint(0, 9), randint(0, 9))
        # place fruit
        self.grid[fruit_location[0]][fruit_location[1]] = -1

    def move(self):
        # move right
        if self.cur_dir == 'E':
            self.snake_pos[0] += 1
        # move left
        elif self.cur_dir == 'W':
            self.snake_pos[0] -= 1
        # move up
        elif self.cur_dir == 'N':
            self.snake_pos[1] -= 1
        # move down
        elif self.cur_dir == 'S':
            self.snake_pos[1] += 1
        # invalid direction
        else:
            print("Invalid direction")

        # check if snake is out of bounds
        if (self.snake_pos[0] < 0 or self.snake_pos[0] > 9) or \
           (self.snake_pos[1] < 0 or self.snake_pos[1] > 9) or \
           (self.grid[self.snake_pos[0]][self.snake_pos[1]] > 0):
            return 'Game Over'

        self.update_grid()

    def update_grid(self):
        for row in self.grid:
            for cell in row:
                if cell > 0:
                    cell -= 1
        self.grid[self.snake_pos[0]][self.snake_pos[1]] = self.snake_len
