def num_translation(number_for_translate):
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
    #внешняя проверка, проверяет есть ли вообще такой ключ, при этом предусмотренно, что он может быть введен с большой буквы
    if nums_relation.get(number_for_translate.lower()) != None:
        #внутри идёт проверка регистра первого символа, и вывод перевода в соответствии с ним
        if number_for_translate[0].isupper():
            return (nums_relation.get(number_for_translate.lower()).capitalize())
        else:
            return (nums_relation.get(number_for_translate))

number= input('введите число для перевода: ')
print(num_translation(number))