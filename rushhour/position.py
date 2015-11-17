class Position:
    """todo"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def new(x: int, y: int):
        hash = x + y * 100
        if hash in cache:
            return cache[hash]
        else:
            new_position = Position(x,y)
            cache[hash] = new_position
            return new_position

    def __add__(self, other: 'Position') -> 'Position':
        return Position.new(self.x + other.x, self.y + other.y)

    def __eq__(self, other: 'Position') -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return "Position(" + str(self.x) + ", " + str(self.y) + ")"


cache = {}