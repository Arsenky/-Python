from abc import ABC, abstractmethod


class Clothes(ABC):
    calculated_cost = 0

    @abstractmethod
    def calc_cost(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.calculated_cost += self.calc_cost

    @property
    def calc_cost(self):
        return float(f'{self.size / 6.5 + 0.5}')

    def __str__(self):
        return f'Расход ткани: {self.calc_cost:.02f}, общий расход ткани: {Coat.calculated_cost:.02f}'


class Suit(Clothes):
    def __init__(self, size):
        self.size = size
        Suit.calculated_cost += self.calc_cost

    @property
    def calc_cost(self):
        return float(f'{self.size * 2 + 0.3}')

    def __str__(self):
        return f'Расход ткани: {self.calc_cost:.02f}, общий расход ткани: {Suit.calculated_cost:.02f}'


coat1 = Coat(50)
print(coat1)
coat2 = Coat(55)
print(coat2)
suit1 = Suit(160)
print(suit1)
suit2 = Suit(180)
print(suit2)
