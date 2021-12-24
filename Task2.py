number_list = []
for i in range(1, 1000, 2):
    number_list.append(i ** 3)

# пункт a
numbers_summ = 0
for number in number_list:
    # переменная number_copy нужна, чтобы не влиять на переменную цикла - number
    number_copy = number
    figure_summ = 0
    while number_copy > 0:
        figure_summ += number_copy % 10
        number_copy = number_copy // 10
    if figure_summ % 7 == 0:
        numbers_summ += number
print('Сумма чисел из списка, сумма цифр которых делится нацело на 7 =', numbers_summ)

# пункт b
numbers_summ = 0
for number in number_list:
    #просто работаем с числами, увеличенными на 17
    number_copy = number + 17
    figure_summ = 0
    while number_copy > 0:
        figure_summ += number_copy % 10
        number_copy = number_copy // 10
    if figure_summ % 7 == 0:
        numbers_summ += number + 17
print('Та же сумма для пункта b =', numbers_summ)
