def num_translate(number_for_translate):
    nums_relation = {'zero' : 'ноль',
    'one' : 'один',
    'two' : 'два',
    'three' : 'три',
    'four' : 'четыре',
    'five' : 'пять',
    'six' : 'шесть',
    'seven' : 'семь',
    'eight' : 'восемь',
    'nine' : 'девять',
    'ten' : 'десять'}

    return (nums_relation.get(number_for_translate))

number = input('введите число для перевода: ')
print(num_translate(number))