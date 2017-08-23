import player
import util
import numpy as np


class SimpleRandomGuesser(player.Player):

    def __init__(self):
        player.Player.__init__(self)
        self.my_guess = []

    def make_guess(self):
        while True:
            row = np.random.randint(0, 10)
            col = np.random.randint(0, 10)
            if not np.isnan(self.opponent_grid.grid[row, col]):
                continue
            self.my_guess = [util.col_names()[col], util.row_names()[row]]
            return self.my_guess

    def process_result(self, result):
        if result == "Miss":
            self.opponent_grid.set_val(self.my_guess[0], self.my_guess[1], 0)
        else:
            self.opponent_grid.set_val(self.my_guess[0], self.my_guess[1], 1)
