import re


class ListElemValid(Exception):
    pass


list = []
el = ''
# вводите числа типа int и float. Чтобы завершить скрипт введите 'stop'
while el != 'stop':
    el = input('Введите следующий элемент: ')
    num_patter_int = re.compile(r'^[-]?\d+$')
    num_patter_float = re.compile(r'^[-]?\d+\.\d+$')
    try:
        if not num_patter_int.findall(el) and not num_patter_float.findall(el) and el != 'stop':
            raise ListElemValid('Вводите только числа!')
    except (ListElemValid) as err:
        print(err)
    else:
        if num_patter_int.findall(el):
            list.append(int(el))
        if num_patter_float.findall(el):
            list.append(float(el))
print(list)
