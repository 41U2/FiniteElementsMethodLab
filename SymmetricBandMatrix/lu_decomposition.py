from typing import List

from symmetric_band_matrix import SymmetricBandMatrix
from matrix import Matrix


class LUDecomposition:

    def __init__(self, l: Matrix, u: Matrix):
        self.l = l
        self.u = u

    @staticmethod
    def lu_decompose_sbm(matrix: SymmetricBandMatrix):
        treshold = 0
        l = Matrix.zeros(matrix.size, matrix.size)
        u = Matrix.zeros(matrix.size, matrix.size)

        for i_row in range(matrix.size):
            l.set_value(i_row, i_row, 1)

        for i_row in range(matrix.size):
            for i_col in range(matrix.size):
                i_min_dim = i_row
                if i_row > i_col:
                    i_min_dim = i_col
                value = matrix(i_row, i_col)
                for i_dim in range(i_min_dim):
                    value -= l(i_row, i_dim) * u(i_dim, i_col)

                if i_row <= i_col:
                    u.set_value(i_row, i_col, value)
                else:
                    if u(i_col, i_col) == 0:
                        l.set_value(i_row, i_col, 0)
                    else:
                        l.set_value(i_row, i_col, value / (u(i_col, i_col) + treshold))

        return LUDecomposition(l, u)

    def solve(self, matrix: Matrix):
        kek = 0

    def __str__(self):
        return "L: \n" + self.l.__str__() + "\nU: \n" + self.u.__str__()


arrays = [
    [1, 20, 7],
    [4, 5],
    [6]
]

mat = SymmetricBandMatrix(3, arrays)
lu = LUDecomposition.lu_decompose_sbm(mat)
print(lu)



