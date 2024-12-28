import functools

file = open(0)

rules = []

for line in file:
    if line.isspace(): break
    rules.append(list(map(int, line.split("|"))))

    

cache = {} 

def compare(x: int, y: int):
    if (x,y) not in cache:
        return 0
    return cache[(x,y)] 

def checkline(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if (x,y) in cache and compare(update[i], update[j]) == 1:
                return False
    return True

for x,y in rules:
    cache[(x,y)] = -1
    cache[(y,x)] = 1

total1 = 0
total2 = 0

for line in file:
    update = list(map(int, line.split(",")))
    if checkline(update):
        total1 += update[len(update) // 2]
    else:
        update.sort(key=functools.cmp_to_key(compare))
        total2 += update[len(update) // 2]
            

print(f"totals: {total1} {total2}")
# print(cache)

