from typing import List


class Matrix:

    def __init__(self, n_rows: int, n_cols: int, values: List[float]):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.values = values
        assert n_rows * n_cols == len(values)

    def __call__(self, i_row: int, i_col: int) -> float:
        assert i_row < self.n_rows
        assert i_row >= 0
        assert i_col < self.n_cols
        assert i_col >= 0
        return self.values[self.n_cols * i_row + i_col]

    def __add__(self, matrix: "Matrix") -> "Matrix":
        assert self.n_cols == matrix.n_cols
        assert self.n_rows == matrix.n_rows
        result_matrix = Matrix.zeros(self.n_rows, self.n_cols)
        for i in range(self.n_cols * self.n_rows):
            result_matrix.values[i] = matrix.values[i] + self.values[i]
        return result_matrix

    def __mul__(self, value: float) -> "Matrix":
        result_matrix = Matrix.zeros(self.n_rows, self.n_cols)
        for i in range(self.n_cols * self.n_rows):
            result_matrix.values[i] = value * self.values[i]
        return result_matrix

    def set_value(self, i_row: int, i_col: int, value: float):
        assert i_row < self.n_rows
        assert i_row >= 0
        assert i_col < self.n_cols
        assert i_col >= 0
        self.values[self.n_cols * i_row + i_col] = value

    @staticmethod
    def zeros(n_rows: int, n_cols: int):
        array = [0 for i in range (n_rows * n_cols)]
        return Matrix(n_rows, n_cols, array)

    def __str__(self):
        result_str = ""
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                result_str += str(self(i_row, i_col)) + " "
            result_str += "\n"
        return result_str


def matrix_example():
    matrix = Matrix(2, 3, [0, 1, 2, 3, -10, 12])
    matrix.set_value(0, 0, 100)
    print(matrix * 2)

    zeros_mat = Matrix.zeros(4, 4)
    print(zeros_mat)


#matrix_example()

