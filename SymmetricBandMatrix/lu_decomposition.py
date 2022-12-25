from copy import deepcopy
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

    @staticmethod
    def solve_upper_matrix(u: Matrix, b: Matrix) -> Matrix:
        assert b.n_cols == 1
        solution = Matrix.zeros(u.n_cols, 1)
        treshold = 1e-4
        for i_row in reversed(range(u.n_cols)):
            solution.set_value(i_row, 0, b(i_row, 0))
            for i_col in range(i_row + 1, u.n_cols):
                diff = solution(i_col, 0) * u(i_row, i_col)
                solution.set_value(i_row, 0, solution(i_row, 0) - diff)
            solution.set_value(i_row, 0, solution(i_row, 0) / (u(i_row, i_row) + treshold))
        return solution

    @staticmethod
    def solve_lower_matrix(l: Matrix, b: Matrix) -> Matrix:
        assert b.n_cols == 1
        assert l.n_rows == b.n_rows
        solution = Matrix.zeros(l.n_cols, 1)
        for i_row in range(l.n_cols):
            solution.set_value(i_row, 0, b(i_row, 0))
            for i_col in range(i_row):
                diff = solution(i_col, 0) * l(i_row, i_col)
                solution.set_value(i_row, 0, solution(i_row, 0) - diff)
        return solution

    def solve(self, matrix: Matrix) -> Matrix:
        first = LUDecomposition.solve_lower_matrix(self.l, matrix)
        second = LUDecomposition.solve_upper_matrix(self.u, first)
        return second


    def __str__(self):
        return "L: \n" + self.l.__str__() + "\nU: \n" + self.u.__str__()


def lu_decomposition_example():
    matrix = Matrix(3, 3,
                    [
                        1, 20, 7,
                        4, 5, 0,
                        6, 0, 0
                    ])

    mat = SymmetricBandMatrix(matrix)
    print(mat)

    lu = LUDecomposition.lu_decompose_sbm(mat)
    print(lu)

    solution = lu.solve(Matrix(3, 1, [5, 0.3, -1]))
    print("Solution: \n", solution)

#lu_decomposition_example()



