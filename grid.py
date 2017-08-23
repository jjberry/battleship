import numpy as np
import util


class Grid:

    def __init__(self):
        self.grid = np.empty(shape=(10, 10))
        self.grid[:] = np.NAN

    def get_val(self, col, row):
        return self.grid[util.row_ind()[row], util.col_ind()[col]]

    def set_val(self, col, row, val):
        self.grid[util.row_ind()[row], util.col_ind()[col]] = val
