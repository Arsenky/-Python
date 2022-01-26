def num_generator(n):
    for num in range(1, n + 1, 2):
        yield num


generator_len = int(input('Введите n: '))
generator = num_generator(generator_len)
for i in generator:
    print(i)
