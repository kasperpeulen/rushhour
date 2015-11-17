class Position:
    """todo"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def new(x: int, y: int):
        hash0 = hash((x, y))
        if hash0 in positions:
            return positions[hash0]
        else:
            positions[hash0] = Position(x, y)
            return positions[hash0]

    def __add__(self, other: 'Position') -> 'Position':
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other: 'Position') -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return "Position(" + str(self.x) + ", " + str(self.y) + ")"

positions = {}