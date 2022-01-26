src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []

for i in range(len(src)):
    if i != 0:
        if src[i] > src[i - 1]:
            new_list.append(src[i])

print(new_list)
