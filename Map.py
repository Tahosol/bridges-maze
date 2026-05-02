import random
import State

class Pixel:
    def __init__(self, property: State.State = State.State.Water,
                 north: State.State = State.State.Water,
                 south: State.State = State.State.Water,
                 east: State.State = State.State.Water,
                 west: State.State = State.State.Water,
                 x: int = 0, y: int = 0):
        self.property = property
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.x = x
        self.y = y

    def available_water_direction(self):
        available = []
        if self.north == State.State.Water:
            available.append((self.y - 1, self.x, "north"))
        if self.south == State.State.Water:
            available.append((self.y + 1, self.x, "south"))
        if self.east == State.State.Water:
            available.append((self.y, self.x + 1, "east"))
        if self.west == State.State.Water:
            available.append((self.y, self.x - 1, "west"))
        return available
    def available_bridge_direction(self):
        available = []
        if self.north == State.State.Bridge:
            available.append((self.y-1,self.x))
        if self.south == State.State.Bridge:
            available.append((self.y+1,self.x))
        if self.east == State.State.Bridge:
            available.append((self.y,self.x+1))
        if self.west == State.State.Bridge:
            available.append((self.y,self.x-1))
        return available

    def turn_self_bridge(self):
        self.property = State.State.Bridge

    def turn_direction_bridge(self, name: str):
        match name:
            case "north":
                self.north = State.State.Bridge
            case "south":
                self.south = State.State.Bridge
            case "east":
                self.east = State.State.Bridge
            case "west":
                self.west = State.State.Bridge

# this part was fix wiht chatgpt
def empty_map(height: int, width: int) -> list[list[Pixel]]:
    the_map = []
    for y in range(height + 2):
        row = []
        for x in range(width):
            if y == 0:  
                row.append(Pixel(property=State.State.Bridge, north=State.State.NorthBorder, x=x, y=y))
            elif y == 1:
                row.append(Pixel(property=State.State.Water, north=State.State.Bridge, x=x, y=y))
            elif y == height + 1: 
                row.append(Pixel(property=State.State.Bridge, south=State.State.SouthBorder, x=x, y=y))
            elif y == width -2:
                row.append(Pixel(property=State.State.Water, south=State.State.Bridge, x=x, y=y))
            elif x == 0: 
                row.append(Pixel(west=State.State.No, x=x, y=y))
            elif x == width - 1:
                row.append(Pixel(east=State.State.No, x=x, y=y))
            else: 
                row.append(Pixel(x=x, y=y))
        the_map.append(row)
    return the_map

# this part was fix wiht chatgpt
def init_map(height: int, width: int) -> list[list[Pixel]]:
    the_map = empty_map(height, width)

    for _ in range(random.randint(int(0.3*width), int(0.6*width))):
        while True:
            first_pixel_x = random.randint(1, width - 2)
            first_pixel_y = random.randint(1, height - 1)
            first_pixel = the_map[first_pixel_y][first_pixel_x]
            if first_pixel.available_water_direction():
                break

        current_pixel = random.choice(first_pixel.available_water_direction())

        first_pixel.turn_direction_bridge(current_pixel[2])
        first_pixel.turn_self_bridge()

        while the_map[current_pixel[0]][current_pixel[1]].south != State.State.SouthBorder:
            available_dirs = the_map[current_pixel[0]][current_pixel[1]].available_water_direction()
            if not available_dirs:
                break
            new_random_direction = random.choice(available_dirs)
            the_map[current_pixel[0]][current_pixel[1]].turn_direction_bridge(new_random_direction[2])
            the_map[current_pixel[0]][current_pixel[1]].turn_self_bridge()
            current_pixel = new_random_direction

    return the_map


if __name__ == "__main__":
    test_map = init_map(100, 100)
    for row in test_map:
        for pixel in row:
            if pixel.property == State.State.Bridge:
                print('*', end='')
            else:
                print('=', end='')
        print()
