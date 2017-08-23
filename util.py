import numpy as np
import ship
import grid as g


def row_names():
    return {i: str(i + 1) for i in range(10)}


def col_names():
    return {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}


def row_ind():
    return {str(i+1): i for i in range(10)}


def col_ind():
    return {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}


def random_board():
    ships = []
    my_grid = g.Grid()
    ships.append(place_ship(my_grid.grid, 5))
    ships.append(place_ship(my_grid.grid, 4))
    ships.append(place_ship(my_grid.grid, 3))
    ships.append(place_ship(my_grid.grid, 3))
    ships.append(place_ship(my_grid.grid, 2))
    return ships, my_grid


def place_ship(grid, size):
    done = False
    while not done:
        # pick a starting cell
        row = np.random.randint(0, 10)
        col = np.random.randint(0, 10)

        # check that there is not a ship there already
        if not np.isnan(grid[row, col]):
            continue

        # randomly select a direction to move 0=up, 1=right, 2=down, 3=left
        dir = np.random.randint(0, 4)

        # check that the space is legit
        accept = True
        if dir == 0:
            for i in range(1, size):
                r = row - i
                if r < 0 or r > 9:
                    accept = False
                    continue
                if not np.isnan(grid[r, col]):
                    accept = False
                    continue
        elif dir == 1:
            for i in range(1, size):
                c = col + i
                if c < 0 or c > 9:
                    accept = False
                    continue
                if not np.isnan(grid[row, c]):
                    accept = False
                    continue
        elif dir == 2:
            for i in range(1, size):
                r = row + i
                if r < 0 or r > 9:
                    accept = False
                    continue
                if not np.isnan(grid[r, col]):
                    accept = False
                    continue
        else:
            for i in range(1, size):
                c = col - i
                if c < 0 or c > 9:
                    accept = False
                    continue
                if not np.isnan(grid[row, c]):
                    accept = False
                    continue

        # fill in the grid
        if accept is False:
            continue
        else:
            squares = []
            grid[row, col] = size
            squares.append([col_names()[col], row_names()[row]])
            if dir == 0:
                for i in range(1, size):
                    r = row - i
                    grid[r, col] = size
                    squares.append([col_names()[col], row_names()[r]])
            elif dir == 1:
                for i in range(1, size):
                    c = col + i
                    grid[row, c] = size
                    squares.append([col_names()[c], row_names()[row]])
            elif dir == 2:
                for i in range(1, size):
                    r = row + i
                    grid[r, col] = size
                    squares.append([col_names()[col], row_names()[r]])
            else:
                for i in range(1, size):
                    c = col - i
                    grid[row, c] = size
                    squares.append([col_names()[c], row_names()[row]])
            done = True
    return ship.Ship(squares)
