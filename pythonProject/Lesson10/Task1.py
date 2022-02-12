class Matrix:
    matrix = []
    len1 = 0
    len2 = 0

    def __init__(self, *args):  # в качестве аргументов вводятся кол-во строк, потом столбцов и далее элементы построчно
        # условие ниже это костыль, без этой принудительной отчистки матрицы, каждый следующий созданный объект класса
        # работал с тем же объектом в памяти, что и предыдущий, не нашел иного способа это исправить
        if self.matrix:
            self.matrix = []

        self.len1 = args[0]
        self.len2 = args[1]
        index = 2
        for i in range(self.len1):
            temp_list = []
            for j in range(self.len2):
                temp_list.append(args[index])
                index += 1
            self.matrix.append(temp_list)

    def __str__(self):
        string = ''
        for i in range(self.len1):
            string += '| '
            for j in range(self.len2):
                string += str(self.matrix[i][j]) + ' '
            string += '|\n'
        return string

    def __add__(self, other):
        new_matrix = self.matrix.copy()
        string = ''
        for i in range(self.len1):
            for j in range(self.len2):
                new_matrix[i][j] += other.matrix[i][j]

        for i in range(self.len1):  # преобразование новой матрицы в строку для вывода, так же как в методе __str__
            string += '| '
            for j in range(self.len2):
                string += str(new_matrix[i][j]) + ' '
            string += '|\n'
        return string


a = Matrix(2, 3, 3, 4, 5, 6, 2, 1)
b = Matrix(2, 3, 3, 5, 9, 12, 1, 2)
c = Matrix(3, 3, 5, 16, 7, 18, 13, 11, 52, 10, 1)
d = Matrix(3, 3, 52, 24, 13, 45, 67, 11, 12, 10, 9)
print(a, b, c, d, sep='\n')
print(a + b)
print(c + d)
