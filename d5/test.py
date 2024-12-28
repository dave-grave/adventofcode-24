with open("d5/input.txt", 'r') as file:
    data = file.read().split()

total1 = 0 
total2 = 0

# dict of {left num, set of right nums}
rules = {}

# list of given page numbers of each update
all_pages = []
correct_pages = set()
incorrect_pages = set()

# parse thru data
for item in data:
    if "|" in item:
        split = item.split("|")
        if split[0] in rules:
            rules[split[0]].add(split[1])
        else:
            rules[split[0]] = {split[1]}
    else:
        all_pages.append(item.split(","))

# print(rules)
# print(all_pages)

for pages in all_pages:
    # print(pages)
    is_correct = True
    for page in pages:
        if page in rules:
            # print(page, rules[page]) 
            for rule in rules[page]:
                # print(page, rule)
                
                if rule in pages and (pages.index(page) > pages.index(rule)):
                    # print(pages.index(page), pages.index(rule))
                    is_correct = False
    
    if is_correct:
        # print("correct")
        correct_pages.add(tuple(pages))

        # add up the middle numbers
        middle_index = int(len(pages)/2)
        total1 += int(pages[middle_index])

    if not is_correct:
        sorted_rules = {}
        sorted_pages = []
        for page in pages:
            if page in rules:
                sorted_rules[page] = len(rules[page])
            else: 
                sorted_rules[page] = 0

        sorted_rules = dict(sorted(sorted_rules.items(), key=lambda item: item[1]))
        for page in sorted_rules:
            sorted_pages.append(page)
        
        middle_index = int (len(sorted_rules) / 2)
        total2 += int(sorted_pages[middle_index])
        print(sorted_rules, middle_index, sorted_pages[middle_index])
        

        
# print(rules)
# print(incorrect_pages)


print(f"{total1}, {total2}")





