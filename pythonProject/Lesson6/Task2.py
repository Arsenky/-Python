ip_list = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        temp_line = line.split()
        if temp_line[0] in ip_list.keys():
            ip_list[temp_line[0]] += 1
        else:
            ip_list[temp_line[0]] = 1
max_requests = 0
for key in ip_list.keys():
    if ip_list[key] > max_requests:
        max_requests = ip_list[key]
        spammer = key
print('Ip спамера:', spammer, 'количество запросов:', max_requests)
