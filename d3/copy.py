import re


with open("d3/input.txt", "r") as f:
    text = f.read()

    is_on = True
    muls = []
    
    sum = 0

    start_match = re.search(r"mul[(][0-9]+[,][0-9]+[)].*?don't[(][)]", text)
    mul_matches = re.findall(r"mul[(][0-9]+[,][0-9]+[)]", start_match.group())
    for j in mul_matches:
        muls.append(j)
    
    do_dont_matches = re.findall(r"do[(][)].*?mul[(][0-9]+[,][0-9]+[)].*?don't[(][)]", text)
   
    for i in do_dont_matches:
        mul_matches = re.findall(r"mul[(][0-9]+[,][0-9]+[)]", i)
        for j in mul_matches:
            muls.append(j)

    for match in muls:
        nums = re.findall(r"[0-9]+", match)
        sum += int(nums[0]) * int(nums[1])
        # print(f"adding up product of {nums[0]} and {nums[1]}. sum is now {sum}")

    print(f"sum is {sum}")

