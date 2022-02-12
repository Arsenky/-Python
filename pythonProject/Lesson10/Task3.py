class Cell:
    def __init__(self, num):
        self.num = num

    def make(self, row):
        result = ['*' * row] * (self.num // row)
        if self.num % row:
            result.append('*' * (self.num % row))
        return '\n'.join(result)

    def __str__(self):
        return f'{self.num}'

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num < other.num:
            raise ValueError('Ячеек в первой клетке меньше чем во второй.')
        return Cell(self.num - other.num)

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __floordiv__(self, other):
        return Cell(self.num // other.num)


cell1 = Cell(10)
cell2 = Cell(25)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 // cell2)
print(cell1 - cell2)  # вызов исключения
