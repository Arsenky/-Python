def thesaurus_adv(*args):
    names_thesaurus_adv = {}
    for name in args:
        first_name, second_name = name.split(' ')  # разделяем имя на две переменные,
        # чтобы обращаться к первым буквам имени и фамилии далее.
        if second_name[0] in names_thesaurus_adv.keys(): # проверям внешний кортеж на на наличие ключа (первой буквы фамилии),
            if first_name[0] in names_thesaurus_adv[second_name[0]].keys(): # проверяем внутренний кортеж на наличие ключа (первой буквы имени),
                #в обоих случаях если ключь есть, дополняем кортеж только новыми данными, в ином случае создаём полностью новый элемент
                names_thesaurus_adv[second_name[0]][first_name[0]].append(name)
            else:
                names_thesaurus_adv[second_name[0]][first_name[0]] = [name]

        else:
            names_thesaurus_adv[second_name[0]] = {first_name[0]: [name]}
    return names_thesaurus_adv


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева",
                    "Григорий Сапогов", "Владимир Агутин", "Константин Ильин", "Николай Евтушенко"))
