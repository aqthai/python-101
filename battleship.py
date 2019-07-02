#
# Author: Alvin Thai
# Description:
#     Battleship is a game where players call coordinates to fire missles at the other player's field in attempt to sink ships.
#
def reader():
    p1_coordinates = input()
    p1 = open(p1_coordinates).readlines()
    process = []
    for coordinates in p1:
        coordinates = coordinates.strip('\n').split()
        process.append(coordinates)
    return process
    #p2_coordinates = input()
    #p2 = open(p2_coordinates)


class GridPos:
    def __init__(self, x, y, instance):
        grid = []
        row = []
        for i in range(0, 10):
            for j in range(0, 10):
                row.append(tuple([i, j]))
            grid.insert(0, row)
            row = []
        print(grid)
        self._x = grid[x][y][0]
        self._y = grid[x][y][1]
        self._ship = instance
    def __str__(self):
        return str(x, y)
    
class Board:
    def __init__(self, grid, collection):
        self.grid = grid
        self.collection = collection
    def __str__(self):
        return str(grid) + str(collection)
    
class Ship:
    def __init__(self, kind, size, pos, space):
        self.kind = kind
        self.size = size 
        self.pos = pos  # grid positions occupied
        self.space = space  # grid positions not yet hit on ship
    def __str__(self):
        return self.kind + "," + self.size + "," + self.pos + "," + self.space
        
def main():
    file = input()
    p1_pos = open(file)
    p1_pos = p1_pos.readlines()
    pos = []
    for line in p1_pos:
        line = line.strip("\n").split()
        if line[0] == 'A':
            size = 5
        elif line[0] == 'P':
            size = 2
        elif line[0] == 'D':
            size = 3
        elif line[0] == 'B':
            size = 4
        elif line[0] == 'S':
            size = 3
        pos.append((line[1], line[2]))
        if line[2] == line[4] and line[1] != line[3]:
            for i in range(line[1]+1, line[3]):
                pos.append((line[i], line[2]))
        elif line[1] == line[3] and line[2] != line[4]:
            for i in range(line[2]+1, line[4]):
                pos.append((line[i], line[1]))
        space = size
        instance = Ship(line[0], size, pos, space)
#main()
    