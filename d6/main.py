from enum import Enum
import time

file = open(0)

grid = []
obstacles = set()
positions = set()

# heading enumerated type
class Heading(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __add__(self, num: int):
        return Heading((self.value + num) % 4)

# parse thru file
for line in file:
    grid.append(list(line.strip()))

# create height and length
print(f"length: {len(grid[0])}, height: {len(grid)}")
height = len(grid)
length = len(grid[0])

class Guard():
    def __init__(self, position, heading):
        self.position = position
        self.heading = heading

    def move(self):
        (x,y) = self.position
        if self.heading.value == 0:
            self.position = (x-1, y)
        elif self.heading.value == 1:
            self.position = (x, y+1)
        elif self.heading.value == 2:
            self.position = (x+1, y)
        else:
            self.position = (x, y-1)

    def turn(self):
        self.heading += 1

    # true if next square is obstacle, false otherwise
    def obstacleCheck(self) -> bool:
        x = self.position[0]
        y = self.position[1]
        if self.heading.value == 0:
            x -= 1
            return (x,y) in obstacles
        elif self.heading.value == 1:
            y += 1
            return (x,y) in obstacles
        elif self.heading.value == 2:
            x += 1
            return (x,y) in obstacles
        else:
            y -= 1
            return (x,y) in obstacles

    # true if outside boundary, false otherwise
    def boundaryCheck(self) -> bool:
        return self.position[0] < 0 or \
               self.position[1] < 0 or \
               self.position[0] >= height or \
               self.position[1] >+ length 
    
# store obstacle locations in set
for r in range(height):
    for c in range(length):
        if grid[r][c] == '#':
            obstacles.add((r,c))
        if grid[r][c] == '^':
            positions.add((r,c))
            start_pos = (r,c)
   
guard = Guard(start_pos, Heading.NORTH)

while not guard.boundaryCheck():
    if not guard.obstacleCheck(): 
        guard.move()
        positions.add(guard.position)
    else:
        guard.turn()    
total2 = 0

# check if guard makes infinite loop
def loopCheck():
    global total2
    cache = set()
    guard = Guard(start_pos, Heading.NORTH)
    cache.add((start_pos, guard.heading))
    print(cache)
    
    while not guard.boundaryCheck():
        if not guard.obstacleCheck(): 
            guard.move()
            cache_length = len(cache)
            cache.add((guard.position, guard.heading))
            if len(cache) == cache_length:
                total2 += 1 
                return
        else:
            guard.turn()   

loopnum = 0
for pair in positions:
    print(f"testing {loopnum}")
    if pair == start_pos: 
        continue
    if pair not in obstacles:
        obstacles.add(pair)
        loopCheck()
        obstacles.remove(pair)
    loopnum += 1


print(total2)
# print(len(positions) - 1)
# print(cache)
# print(obstacles)
# print(positions)

# print(grid)