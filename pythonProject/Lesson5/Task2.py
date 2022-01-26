n = int(input('Введите n: '))
num_generator = (num for num in range(1, n + 1, 2))
for i in num_generator:
    print(i)
