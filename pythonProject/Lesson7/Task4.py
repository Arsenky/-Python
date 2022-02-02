import os

dir_stats = {}
keys = []

root_dir = os.path.dirname(__file__)
dir = os.path.join(root_dir, 'some_dir')  # можно вписать имя любой папки

for root, dirs, files in os.walk(dir):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        i = 0
        while size > 10 ** i:
            i += 1
        if 10 ** i in dir_stats.keys():
            dir_stats[10 ** i] += 1
        else:
            dir_stats[10 ** i] = 1
            keys.append(10 ** i)
        i = 0
for key in sorted(keys):
    print(f'{key}: {dir_stats[key]}')
