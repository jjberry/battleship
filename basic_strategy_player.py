import player
import util
import numpy as np


class BasicStrategyPlayer(player.Player):

    def __init__(self):
        player.Player.__init__(self)
        self.last_guess = []
        self.candidates = []

    def make_guess(self):
        if len(self.candidates) == 0:
            self.last_guess = self.random_guess()
            return self.last_guess
        else:
            self.last_guess = self.candidates.pop(0)
            return self.last_guess

    def process_result(self, result):
        if result == "Miss":
            self.opponent_grid.set_val(self.last_guess[0], self.last_guess[1], 0)
        else:
            self.opponent_grid.set_val(self.last_guess[0], self.last_guess[1], 1)
            self.get_candidates()

    def random_guess(self):
        while True:
            row = np.random.randint(0, 10)
            col = np.random.randint(0, 10)
            if not np.isnan(self.opponent_grid.grid[row, col]):
                continue
            return [util.col_names()[col], util.row_names()[row]]

    def get_candidates(self):
        col = util.col_ind()[self.last_guess[0]]
        row = util.row_ind()[self.last_guess[1]]
        # look at the adjacent squares
        up = down = left = right = None
        if row - 1 >= 0:
            up = self.opponent_grid.grid[row - 1, col]
        if row + 1 < 10:
            down = self.opponent_grid.grid[row + 1, col]
        if col - 1 >= 0:
            left = self.opponent_grid.grid[row, col - 1]
        if col + 1 < 10:
            right = self.opponent_grid.grid[row, col + 1]
        # eliminate invalid directions
        dir = [i for i in range(4)]
        if up is None or up >= 0:
            dir.remove(0)
        if right is None or right >= 0:
            dir.remove(1)
        if down is None or down >= 0:
            dir.remove(2)
        if left is None or left >= 0:
            dir.remove(3)
        # add remaining to the queue
        if len(dir) > 0:
            if 0 in dir:
                self.candidates.append([util.col_names()[col], util.row_names()[row - 1]])
            if 1 in dir:
                self.candidates.append([util.col_names()[col + 1], util.row_names()[row]])
            if 2 in dir:
                self.candidates.append([util.col_names()[col], util.row_names()[row + 1]])
            if 3 in dir:
                self.candidates.append([util.col_names()[col - 1], util.row_names()[row]])
