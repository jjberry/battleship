class Ship:

    def __init__(self, squares):
        self.original = list(squares)
        self.squares = squares
        self.sunk = False
        self.n = len(squares)

    def is_hit(self, square):
        if square in self.squares:
            self.squares.remove(square)
            if len(self.squares) == 0:
                self.sunk = True
            return True
        else:
            return False
