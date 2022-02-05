from functools import wraps


def val_valid(callback):
    def _val_valid(function):
        @wraps(function)
        def wrapper(*args):
            for arg in args:
                if not callback(arg):
                    raise ValueError(f'wrong wal {arg}')
            return function(*args)

        return wrapper

    return _val_valid


@val_valid(lambda x: x != 0)
def div(a):
    return (100 / a)


print(div(10))
print(div(0))
