tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Леонид', 'Михаил'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def dict_generator(list1, list2):
    if len(list1) - len(list2) > 0:
        for i in range(len(list1) - len(list2)):
            list2.append(None)
    for name, klass in zip(list1, list2):
        yield (name, klass)


dict = dict_generator(tutors, klasses)
for i in dict:
    print(i)

# разкоментировав строку ниже, добьемся истощения генератора
# print(next(dict))
