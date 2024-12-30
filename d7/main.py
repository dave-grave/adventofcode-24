file = open(0)
total = 0

def sum(target, nums, total) -> bool:
    if len(nums) == 0:
        return int(total) == int(target)
    
    if total == 0:
        first = nums[0]
        second = nums[1]
        nums = nums[2:]
        return sum(target, nums, int(first) + int(second)) or \
               sum(target, nums, int(first) * int(second)) or \
               sum(target, nums, str(first) + str(second)) # include this line for part 2
    else: 
        first = nums[0]
        nums = nums[1:]
        return sum(target, nums, int(total) + int(first)) or \
               sum(target, nums, int(total) * int(first)) or \
               sum(target, nums, str(total) + str(first)) # include this line for part 2


for line in file:
    target = int(line.split()[0][:-1])
    nums = list(map(int, line.split()[1:]))

    isValid = sum(target, nums, 0)
    if isValid:
        total += target

print(total)