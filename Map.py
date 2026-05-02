import State

class Pixel:
    def __init__(self, property: State.State, nord: State.State, south: State.State, east: State.State, west: State.State):
        self.property = property
        self.nord = nord
        self.south= south
        self.east = east
        self.west = west