class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Ручкой удобно писать текст')


class Pencil(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Карандашом рисуют')


class Handle(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Маркером можно что-то выделить ')


stationery1 = Stationery()
pen1 = Pen('Erikcrauzer')
pencil1 = Pencil('Балашихинская карандашная фабрика')
handle1 = Handle('WorldOfColors')

stationery1.draw()
pen1.draw()
pencil1.draw()
handle1.draw()
