import player
import util
import numpy as np


class BasicStrategyPlayer(player.Player):

    def __init__(self):
        player.Player.__init__(self)
        self.last_guess = []
        self.knowledge_state = {}

    def make_guess(self):
        if len(self.knowledge_state) == 0:
            self.last_guess = self.random_guess()
            return self.last_guess
        else:
            last_hit = self.knowledge_state["Hit"]
            col = util.col_ind()[last_hit[0]]
            row = util.row_ind()[last_hit[1]]
            resp = self.get_guess(row, col)
            if len(resp) == 2:
                return self.last_guess

            # try moving back to the nearest hit
            else:
                up, down, left, right = resp[0], resp[1], resp[2], resp[3]
                if up == 1 and row < 9:
                    row += 1
                    resp = self.get_guess(row, col)
                elif right == 1 and col > 0:
                    col -= 1
                    resp = self.get_guess(row, col)
                elif down == 1 and row > 0:
                    row -= 1
                    resp = self.get_guess(row, col)
                elif left == 1 and col < 9:
                    col += 1
                    resp = self.get_guess(row, col)
                if len(resp) == 2:
                    return self.last_guess
                # give up and randomly guess
                else:
                    self.last_guess = self.random_guess()
                    return self.last_guess

    def process_result(self, result):
        if result == "Miss":
            self.opponent_grid.set_val(self.last_guess[0], self.last_guess[1], 0)
        elif result == "Hit and Sunk":
            self.opponent_grid.set_val(self.last_guess[0], self.last_guess[1], 1)
            self.knowledge_state = {}
        else:
            self.opponent_grid.set_val(self.last_guess[0], self.last_guess[1], 1)
            self.knowledge_state["Hit"] = self.last_guess

    def random_guess(self):
        while True:
            row = np.random.randint(0, 10)
            col = np.random.randint(0, 10)
            if not np.isnan(self.opponent_grid.grid[row, col]):
                continue
            return [util.col_names()[col], util.row_names()[row]]

    def get_guess(self, row, col):
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
        # look for hits in adjacent squares
        if 0 in dir and down == 1:
            self.last_guess = [util.col_names()[col], util.row_names()[row - 1]]
            return self.last_guess
        if 1 in dir and left == 1:
            self.last_guess = [util.col_names()[col + 1], util.row_names()[row]]
            return self.last_guess
        if 2 in dir and up == 1:
            self.last_guess = [util.col_names()[col], util.row_names()[row + 1]]
            return self.last_guess
        if 3 in dir and right == 1:
            self.last_guess = [util.col_names()[col - 1], util.row_names()[row]]
            return self.last_guess
        # if no adjacent hits are found, pick a direction
        if len(dir) > 0:
            d = np.random.choice(dir)
            if d == 0:
                self.last_guess = [util.col_names()[col], util.row_names()[row - 1]]
                return self.last_guess
            if d == 1:
                self.last_guess = [util.col_names()[col + 1], util.row_names()[row]]
                return self.last_guess
            if d == 2:
                self.last_guess = [util.col_names()[col], util.row_names()[row + 1]]
                return self.last_guess
            if d == 3:
                self.last_guess = [util.col_names()[col - 1], util.row_names()[row]]
                return self.last_guess
        else:
            return [up, down, left, right]
