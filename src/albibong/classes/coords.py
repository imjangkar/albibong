class Coords:

    def __init__(self, x, y):
        self.x: float = x
        self.y: float = y

    @staticmethod
    def serialize(coords):
        return {"x": coords.x, "y": coords.y}
