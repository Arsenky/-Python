def type_logger(function):
    def wrapper(*args):
        calc = function(*args)
        if len(args) == 1:
            print(f'{args[0]}: {type(args[0])}')
        else:
            for el in args:
                print(f'{el}: {type(el)}')
        return calc

    return wrapper


@type_logger
def calculation(y, z, *args):
    x = y / z
    return x


print(calculation(10, 3, 'str', 4.78))
