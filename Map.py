import State

class Pixel:
    def __init__(self, property: str, ):
        self.property = property
        self.nord = State.NextTo
        self.south= State.NextTo
        self.east = State.NextTo
        self.west = State.NextTo