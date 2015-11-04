class Position:
    """todo"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: 'Position') -> 'Position':
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other: 'Position') -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return "Position(" + str(self.x) + ", " + str(self.y) + ")"


pos = Position(1, 2) + Position(1, 3)
