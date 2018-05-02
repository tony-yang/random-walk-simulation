import math, random

class Location:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def move(self, x_coordinate, y_coordinate):
        return Location(self.x + float(x_coordinate), self.y + float(y_coordinate))

    def get_coordinates(self):
        return self.x, self.y

    def get_distance(self, other):
        x, y = other.get_coordinates()
        x_dist = self.x - x
        y_dist = self.y - y
        return math.sqrt(x_dist ** 2 + y_dist ** 2)

class Direction:
    possible_directions = ('N', 'S', 'E', 'W')

    def __init__(self, direction):
        if direction in Direction.possible_directions:
            self.direction = direction
        else:
            raise ValueError('in Direction.__init__')

    def move(self, distance):
        if 'N' == self.direction:
            return (0, distance)
        elif 'S' == self.direction:
            return (0, -distance)
        elif 'E' == self.direction:
            return (distance, 0)
        elif 'W' == self.direction:
            return (-distance, 0)
        else:
            raise ValueError('in Direction.move')

class Field:
    def __init__(self, drunk, location):
        self.drunk = drunk
        self.location = location

    def move(self, direction, distance):
        old_location = self.location
        new_x, new_y = direction.move(distance)
        self.location = old_location.move(new_x, new_y)

    def get_location(self):
        return self.location

    def get_drunk(self):
        return self.drunk

class Drunk:
    def __init__(self, name):
        self.name = name

    def move(self, field, time=1):
        if field.get_drunk() != self:
            raise ValueError('Drunk.move called with drunk set in field')

        for i in range(time):
            direction = Direction(random.choice(Direction.possible_directions))
            field.move(direction, 1)


def perform_trial(time, field):
    start = field.get_location()
    distances = [0.0]
    for t in range(1, time + 1):
        field.get_drunk().move(field)
        new_location = field.get_location()
        distance = new_location.get_distance(start)
        distances.append(distance)
    return distances



if __name__ == '__main__':
    drunk = Drunk('Test Simpson')
    for i in range(3):
        field = Field(drunk, Location(0, 0))
        distances = perform_trial(500, field)

    print(distances)
