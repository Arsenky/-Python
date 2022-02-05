import re


def email_parse(address):
    dict_pattern = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    if dict_pattern.findall(address):
        for el in dict_pattern.finditer(address):
            return (el.groupdict())
    else:
        msg = f'wrong email: {address}'
        raise ValueError(msg)


email_address = input('Введите e-mail: ')
print(email_parse(email_address))
