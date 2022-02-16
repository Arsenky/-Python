class MyZeroDivizionError(Exception):
    pass


a = 100
b = int(input('Введите делитель: '))
try:
    if b == 0:
        raise MyZeroDivizionError('Делить на ноль нельзя!')
except (MyZeroDivizionError) as err:
    print(err)

else:
    print(a / b)
