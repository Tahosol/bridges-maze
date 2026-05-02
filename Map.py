import State
import random

class Pixel:
    def __init__(self, property: State.State=State.State.Water, nord: State.State=State.State.Water, south: State.State=State.State.Water, east: State.State=State.State.Water, west: State.State=State.State.Water):
        self.property = property
        self.nord = nord
        self.south= south
        self.east = east
        self.west = west

def empty_map(height: int, width: int):
    the_map = []
    for _ in range(height):
        j = []
        for _ in range(width):
            j.append(Pixel())
        the_map.append(j)

    south_line = []
    for i in range(width):
        if i == 0:
            south_line.append(Pixel(State.State.Bridge, State.State.Water, State.State.SouthBorder, State.State.Bridge,State.State.Water))
        elif i == 49:
            south_line.append(Pixel(State.State.Bridge, State.State.Water, State.State.SouthBorder, State.State.Water,State.State.Bridge))
        else :
            south_line.append(Pixel(State.State.Bridge, State.State.Water, State.State.SouthBorder, State.State.Bridge,State.State.Bridge))
    the_map.reverse()
    the_map.append(south_line)
    the_map.reverse()


    nord_line = []
    for i in range(width):
        if i == 0:
            nord_line.append(Pixel(State.State.Bridge, State.State.Water, State.State.NordBorder, State.State.Bridge,State.State.Water))
        elif i == 49:
            nord_line.append(Pixel(State.State.Bridge, State.State.Water, State.State.NordBorder, State.State.Water,State.State.Bridge))
        else :
            nord_line.append(Pixel(State.State.Bridge, State.State.Water, State.State.NordBorder, State.State.Bridge,State.State.Bridge))
    the_map.append(nord_line)
    return the_map

def init_map(height: int, width: int):
    the_map = empty_map(height, width)
    


if __name__ == "__main__":
    test_map = empty_map(50, 100)
    for i in test_map:
        for a in i:
            if a.property == State.State.Bridge:
                print('*', end='')
        print()