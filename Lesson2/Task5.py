price_list = [57.8, 46.51, 97, 48, 21.87, 90.03, 43.98, 9.01, 63.2, 45.78, 39.81, 31.09, 69.9]

# вывод списка, сразу в нужном по заданию виде, в программе еще два раза используется этот же вывод
for price in price_list:
    ruble = int(price) #количество рублей получается явным приведением к типу int
    kopeck = int(price * 100) % 100 # количество копеек получаем таким образом
    print(f'{ruble} руб {kopeck:02d} коп, ', end='') #нужный формат для копеек получаем f строкой

print()  # пустой print для перехода на новую строку
# сортируем список по возрастанию методом sort, запрашиваем id до и после этого, таким образом мы увидим, что id одинаковый
print(id(price_list))
price_list.sort()
print(id(price_list))
for price in price_list:
    ruble = int(price)
    kopeck = int(price * 100) % 100
    print(f'{ruble} руб {kopeck:02d} коп, ', end='')

print()
# список отсортированный по убыванию получаем реверсом списка по возрастанию, методом reverse
reversed_price_list = price_list.copy()
reversed_price_list.reverse()
print(reversed_price_list)

# пять самых больших цен мы получим выведя первые пять элементов отсортированного по убываию списка
five_most_expensive_goods = (reversed_price_list[:5])
for price in five_most_expensive_goods:
    ruble = int(price)
    kopeck = int(price * 100) % 100
    print(f'{ruble} руб {kopeck:02d} коп, ', end='')