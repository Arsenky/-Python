class Worker:
    total_income = {'wage': 0, 'bonus': 0}
    _income = total_income['wage'] + total_income['bonus']
    name = ''
    surname = ''
    position = ''


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.total_income['wage'] = wage
        self.total_income['bonus'] = bonus
        self._income = self.total_income['wage'] + self.total_income['bonus']

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income)


Position1 = Position('Светлана', 'Леснова', 'Бухалтер', 40000, 15500)
Position2 = Position('Игорь', 'Попов', 'Охранник', 25500, 5300)
Position1.get_full_name()
Position1.get_total_income()
print(Position1.name, Position1.surname, Position1.position, Position1.total_income)
Position2.get_full_name()
Position2.get_total_income()
print(Position2.name, Position2.surname, Position2.position, Position2.total_income)
