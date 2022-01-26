src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_nums = set()
for el in src:
    if el in unique_nums:
        unique_nums.discard(el)
    else:
        unique_nums.add(el)
result = [el for el in src if el in unique_nums]
print(result)
