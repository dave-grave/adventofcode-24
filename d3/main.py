from re import findall

total = 0
enabled = True
data = open("d3/input.txt").read()

for a, b, do, dont in findall(r"mul\(([0-9]+),([0-9]+)\)|(do[(][)])|(don't[(][)])", data):
    if do or dont:
        enabled = bool(do)
    else:
        x = int(a) * int(b)
        total += x * enabled

print(f"sum is {total}")