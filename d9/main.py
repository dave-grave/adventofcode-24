file = list(map(list, open(0).read().split()))
file = [int(x) for x in file[0]]

total = 0

nums = []
empty_indices = []
num_indices = []

empty_cache = []
num_cache = []
id = 0
current_index = 0

# parse through file
for i in range(len(file)):
    if i % 2 == 0:
        num_cache.append((current_index, file[i]))
        for j in range(file[i]):
            nums.append(id) 
        id += 1
    else:
        empty_cache.append((current_index, file[i]))
        for j in range(file[i]):
            nums.append(".")
    current_index += file[i]

num_cache.reverse()


# part 2 bwlow
# num: index, length
# empty: index, length
for num in num_cache:
    for i, empty in enumerate(empty_cache):
        if empty[0] > num[0]:
            break
        if empty[1] >= num[1]:
            # print(f"empty is {empty_cache[i]}")
            for j in range(num[1]):
                nums[empty[0] + j], nums[num[0] + j] = \
                    nums[num[0] + j], nums[empty[0] + j]

            # print(nums)

            empty_cache[i] = (empty[0] + num[1], empty[1] - num[1])
            # print(f"empty is now {empty_cache[i]}")

            break



# convert data into file blocks (part 1)
# for i in range(len(nums)):
#     if nums[i] == ".":
#         empty_indices.append(i) 
#     else:
#         num_indices.append(i)

# rearrange indices of files (part 1)
# final_index = len(num_indices) - 1
# num_indices.reverse()
# for i in range(len(num_indices)):
#     if num_indices[i] == final_index: 
#         break
#     # print(num_indices[i], empty_indices[i])
#     nums[num_indices[i]], nums[empty_indices[i]] = \
#        nums[empty_indices[i]], nums[num_indices[i]]

for i, num in enumerate(nums):
    if type(num) is int:
        total += i*num

print(f"total is {total}")