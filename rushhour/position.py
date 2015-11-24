class Position:
    """todo"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def new(x: int, y: int):
        hash = (x + 2) + 15 * (y + 1)
        if hash in cache:
            return cache[hash]
        else:
            new_position = Position(x,y)
            cache[hash] = new_position
            return new_position

    def __add__(self, other: 'Position') -> 'Position':
        return Position.new(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return "Position(" + str(self.x) + ", " + str(self.y) + ")"


cache = {}