import re

data = open("d4/input.txt").read()

total1 = 0
total2 = 0
lines = data.split()
chars = []

# 140x140 grid
for line in lines:
    chars.append(list(line))

num_rows = len(lines)
num_cols = len(lines[0])

# left and rights
total1 += len(re.findall(r"XMAS", data)) + len(re.findall(r"SAMX", data))

# ups and downs
for r in range (num_rows-3):
    for c in range(num_cols):
        if chars[r][c] == "X" and \
          chars[r+1][c] == "M" and \
          chars[r+2][c] == "A" and \
          chars[r+3][c] == "S":
            total1 += 1
        if chars[r][c] == "S" and \
          chars[r+1][c] == "A" and \
          chars[r+2][c] == "M" and \
          chars[r+3][c] == "X":
            total1 += 1

# left diagonal
for r in range(num_rows - 3):
    for c in range(num_cols - 3):
        if chars[r][c] == "X" and \
          chars[r+1][c+1] == "M" and \
          chars[r+2][c+2] == "A" and \
          chars[r+3][c+3] == "S":
              total1 += 1
        if chars[r][c] == "S" and \
          chars[r+1][c+1] == "A" and \
          chars[r+2][c+2] == "M" and \
          chars[r+3][c+3] == "X":
            total1 += 1
            
# right diagonal
for r in range(num_rows-3):
    for c in range(num_cols-3):
        if chars[r][c+3] == "X" and \
        chars[r+1][c+2] == "M" and \
        chars[r+2][c+1] == "A" and \
        chars[r+3][c] == "S":
            total1 += 1
        if chars[r][c+3] == "S" and \
        chars[r+1][c+2] == "A" and \
        chars[r+2][c+1] == "M" and \
        chars[r+3][c] == "X":
            total1 += 1
        

# find all instances of A, then store diags into a list
for r in range(1, num_rows-1):
    for c in range(1, num_cols-1):
        diags = []
        if (chars[r][c] == "A"):
            diags.append(chars[r-1][c-1]+chars[r][c]+chars[r+1][c+1])
            diags.append(chars[r-1][c+1]+chars[r][c]+chars[r+1][c-1])
            total2 += 1 if ((diags[0] == "MAS" or diags[0] == "SAM") and (diags[1] == "SAM" or diags[1] == "MAS")) else 0
            

print(f"total1 is {total1}, total2 is {total2}")


