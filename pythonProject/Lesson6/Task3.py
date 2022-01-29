import json
import sys

result_dict = {}
with open('users.txt', 'r', encoding='utf-8') as users:
    with open('hobby.txt', 'r', encoding='utf-8') as hobbys:
        for name in users:
            result_dict[name.strip()] = hobbys.readline().strip()
            if not result_dict[name.strip()]:
                result_dict[name.strip()] = None
        if hobbys.read().strip():  # strip() предусматривает то, что после прошлых операций в файле может остаться символ
            # переноса строки
            sys.exit(1)

with open('result_dict.json', 'w', encoding='utf-8') as result_file:
    result_file.write(json.dumps(result_dict))
with open('result_dict.json', 'r', encoding='utf-8') as result_file:
    print(json.loads(result_file.read()))