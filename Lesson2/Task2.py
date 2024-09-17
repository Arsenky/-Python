strings_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

modifaed_strings_list = []
# формируем новый список, добавляя ковычки перед и после тех элементов, что являются числами
for string in strings_list:
    if string.isdigit():
        modifaed_strings_list.append('"')
        if len(string) < 2:  # этим условием сразу приводим элемент к нужному формату, дополняем до двух знаков
            modifaed_strings_list.append('0' + string)
        else:
            modifaed_strings_list.append(string)
        modifaed_strings_list.append('"')
    elif string[
         1:].isdigit():  # этим условием учитываем те елементы, которые являются числом, но имеют знак + или - в начале
        modifaed_strings_list.append('"')
        if len(string[1:]) < 2:
            modifaed_strings_list.append(string[0] + '0' + string[1:])
        else:
            modifaed_strings_list.append(string)
        modifaed_strings_list.append('"')
    else:
        modifaed_strings_list.append(string)

# выводим для наглядности исходный и обработанный список
print(strings_list)
print(modifaed_strings_list)

#формируем из обработанного списка строку методом join
print(' '.join(modifaed_strings_list))
