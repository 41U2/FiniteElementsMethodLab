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

    def set_value(self, i_row: int, i_col: int, value: float):
        assert i_row < self.n_rows
        assert i_row >= 0
        assert i_col < self.n_cols
        assert i_col >= 0
        self.values[self.n_cols * i_row + i_col] = value

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
    print(matrix)


matrix_example()

