def thesaurus(*args):
    names_thesaurus = {}
    for name in args:
        if name[0] in names_thesaurus.keys():
            names_thesaurus[name[0]].append(name)
        else:
            names_thesaurus[name[0]] = [name]
    return names_thesaurus


print(thesaurus('Владислав', 'Анна', 'Константин', 'Роман', 'Алексей', 'Борис', 'Кирилл', 'Антонина', 'Василий'))
