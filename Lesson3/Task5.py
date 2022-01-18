import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(jokes_number):
    '''Функция принимает в качестве аргумента переменную типа int - "jokes_number",
     и возвращает это же количество случайно сформированных "шуток" из строк списков "nouns", "adverbs" и "adjectives"'''
    jokes_list = []
    for i in range(jokes_number):
        jokes_list.append(random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives))
    return jokes_list


print(get_jokes(5))
help(get_jokes)
