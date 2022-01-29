result = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        temp_line = line.split()
        result.append((temp_line[0], temp_line[5][1:], temp_line[6]))
print(result)

