import grid
import util
import numpy as np


class Player:

    def __init__(self):
        self.opponent_grid = grid.Grid()
        self.ships, self.my_grid = util.random_board()
        self.knowledge_state = {}
        self.my_guess = []

    def make_guess(self):
        # make a random guess if we don't know anything
        if len(self.knowledge_state) == 0:
            self.my_guess = self.random_guess()
            return self.my_guess
        #else:
        #    done = False
        #    while not done:
        #        dir = np.random.choice(self.knowledge_state['Dirs'])
        #        hit = self.knowledge_state['Hit']
        #        col = util.col_ind()[hit[0]]
        #        row = util.row_ind()[hit[1]]



    def random_guess(self):
        while True:
            row = np.random.randint(0, 10)
            col = np.random.randint(0, 10)
            if not np.isnan(self.opponent_grid.grid[row, col]):
                continue
            return [util.col_names()[col], util.row_names()[row]]

    def process_result(self, result):
        if result == "Miss":
            self.opponent_grid.set_val(self.my_guess[0], self.my_guess[1], 0)
        else:
            self.opponent_grid.set_val(self.my_guess[0], self.my_guess[1], 1)
            if "Sunk" in result:
                self.knowledge_state = {}
            #elif len(self.knowledge_state) == 0:
            #    self.knowledge_state['Hit'] = self.my_guess
            #    self.knowledge_state['Dirs'] = range(4)

    def check_opponent_guess(self, guess):
        hit = []
        is_sunk = False
        for ship in self.ships:
            is_hit = ship.is_hit(guess)
            if is_hit is True:
                is_sunk = ship.sunk
                if ship.sunk:
                    self.ships.remove(ship)
            hit.append(is_hit)
        if any(hit) and is_sunk:
            return "Hit and Sunk"
        elif any(hit):
            return "Hit"
        else:
            return "Miss"
