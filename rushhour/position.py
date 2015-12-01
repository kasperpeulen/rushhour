class Position:
    """
    Class to store positions on the board. 0,0 is top left
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def new(x: int, y: int):
        """
        Check if position is already in cache and otherwise make new instance
        """
        hash = x + y * 100
        if hash in cache:
            return cache[hash]
        else:
            new_position = Position(x,y)
            cache[hash] = new_position
            return new_position

    def __add__(self, other: 'Position') -> 'Position':
        """
        Ability to use + with positions
        """
        return Position.new(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        """
        String representation
        """
        return "Position(" + str(self.x) + ", " + str(self.y) + ")"


cache = {}