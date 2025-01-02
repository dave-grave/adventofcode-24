from collections import defaultdict

grid = list(map(list, open(0).read().splitlines()))

antennas = defaultdict(list)
total = set()

# grid check 
def inGrid(loc):
    if loc[0] >= 0 and loc[0] < len(grid) and loc[1] >= 0 and loc[1] < len(grid[0]):
        return True
    return False

# find all possible multiples of antinodes 
def find(first: tuple, diff: tuple):
    print(f"first is {first}, diff is {diff}")
    antinodes = set()
    antinodes.add(first)
    loc = list(first)

    # search by adding difference in one way
    while True:
        list(loc)
        loc[0] += diff[0]
        loc[1] += diff[1]
        if inGrid(loc):
            antinodes.add(tuple(loc))
        else:
            break

    # search by subtracting difference in the other way
    loc = list(first)
    while True:
        list(loc)
        loc[0] -= diff[0]
        loc[1] -= diff[1]
        if inGrid(loc):
            antinodes.add(tuple(loc))
        else:
            break

    return antinodes

# parse through grid and append items into 2d array
for r in range(len(grid)):
    for c in range(len(grid[0])):
        item = grid[r][c]
        if item != ".":
            antennas[item].append((r,c))

# search for each combination of antennas of same type
for key in antennas:
    locations = antennas[key]
    for i in range(len(locations)):
        for j in range(i+1, len(locations)):
            diff = tuple([x-y for x,y in zip(list(locations[i]), list(locations[j]))])

            test = find(locations[i], diff)
            print(f"test is {test}")
            
            for item in test:
                total.add(item)
    
print(len(total))
            
