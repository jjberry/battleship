import grid
import util


class Player:

    def __init__(self):
        self.opponent_grid = grid.Grid()
        self.ships, self.my_grid = util.random_board()

    def make_guess(self):
        pass

    def process_result(self, result):
        pass

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
