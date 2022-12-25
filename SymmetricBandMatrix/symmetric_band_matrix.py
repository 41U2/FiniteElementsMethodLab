from matrix import Matrix


class SymmetricBandMatrix:

    def __init__(self, matrix: Matrix):
        self.storage = matrix
        self.size = matrix.n_rows

    def __call__(self, i_row: int, i_col: int) -> float:
        assert i_row < self.size
        assert i_col < self.size
        assert i_row >= 0
        assert i_col >= 0
        if i_row <= i_col:
            return self.storage(i_row, i_col - i_row)

        return self(i_col, i_row)

    def set_value(self, i_row: int, i_col: int, value: float):
        if i_row > i_col:
            return
        self.storage.set_value(i_row, i_col - i_row, value)

    def __add__(self, band_matrix: "SymmetricBandMatrix") -> "SymmetricBandMatrix":
        return SymmetricBandMatrix(self.storage + band_matrix.storage)

    def __mul__(self, value: float) -> "SymmetricBandMatrix":
        return SymmetricBandMatrix(self.storage * value)

    @staticmethod
    def zeros(n_rows: int, band_width: int):
        assert band_width <= n_rows
        return SymmetricBandMatrix(Matrix.zeros(n_rows, band_width))

    def __str__(self):
        result_str = ""
        for i_row in range(self.size):
            for i_col in range(self.size):
                result_str += str(self(i_row, i_col)) + " "
            result_str += "\n"
        return result_str


def symmetric_band_matrix_example():
    mat_1 = Matrix(3, 3, [
        1, 20, 7,
        4, 5, 0,
        6, 0, 0
    ])

    mat_2 = Matrix(3, 3, [
        -1, 12, 3,
        4, 0.4, 0,
        -100, 0, 0
    ])

    band_matrix_1 = SymmetricBandMatrix(mat_1)
    band_matrix_2 = SymmetricBandMatrix(mat_2)
    band_matrix_zeros = SymmetricBandMatrix.zeros(3, 3)
    band_matrix_zeros.set_value(0, 2, 15)
    print(band_matrix_zeros)

    sum = band_matrix_1 + band_matrix_2 * -1
    #sum.set_value(0, 1, 0.1)
    print(sum)


#symmetric_band_matrix_example()
