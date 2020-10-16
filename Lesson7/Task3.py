class Cell:
    def __init__(self, cells_num):
        self.cells_num = cells_num

    def __str__(self):
        return(f'Клетка с количеством ячеек = {self.cells_num}')

    def __add__(self, other):
        return Cell(self.cells_num + other.cells_num)

    def __sub__(self, other):
        res = self.cells_num - other.cells_num
        if res > 0:
            return Cell(res)
        else:
            print('Нельзя вычесть из меньшей клетки большую!')

    def __mul__(self, other):
        return Cell(self.cells_num * other.cells_num)

    def __truediv__(self, other):
        return Cell(self.cells_num // other.cells_num)

    def make_order(self, cell_row):
        result = ''
        total = self.cells_num
        while total >= cell_row:
            result += ('*' * cell_row) + '\n'
            total -= cell_row
        result += ('*' * total) + '\n'
        return result

amyoba = Cell(125)
cell1 = Cell(90)
print(amyoba)
print(amyoba + cell1)
print(amyoba - cell1)
print(amyoba * cell1)
print(amyoba / cell1)
print(amyoba.make_order(20))