from .matrix import Matrix


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
            if i_row < 0 or i_row >= self.storage.n_rows:
                return 0
            if i_col - i_row < 0 or i_col - i_row >= self.storage.n_cols:
                return 0
            return self.storage(i_row, i_col - i_row)

        return self(i_col, i_row)

    def set_value(self, i_row: int, i_col: int, value: float):
        if i_row > i_col:
            return
        if i_row < 0 or i_row >= self.storage.n_rows:
            return
        if i_col - i_row < 0 or i_col - i_row >= self.storage.n_cols:
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

    @staticmethod
    def mtimes(m1: "SymmetricBandMatrix", m2: Matrix):
        assert m1.size == m2.n_rows
        result_matrix = Matrix.zeros(m1.size, m2.n_cols)
        for i_row in range(m1.size):
            for i_col in range(m2.n_cols):
                sum = 0
                for i_dim in range(m1.size):
                    sum += m1(i_row, i_dim) * m2(i_dim, i_col)
                result_matrix.set_value(i_row, i_col, sum)
        return result_matrix

    def __str__(self):
        result_str = ""
        for i_row in range(self.size):
            for i_col in range(self.size):
                result_str += str(self(i_row, i_col)) + " "
            result_str += "\n"
        return result_str

    def __repr__(self):
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

    band_matrix_zeros = SymmetricBandMatrix.zeros(3, 3)
    band_matrix_zeros.set_value(0, 2, 15)
    print(band_matrix_zeros)

    band_matrix_1 = SymmetricBandMatrix(mat_1)
    print(band_matrix_1)

    band_matrix_2 = SymmetricBandMatrix(mat_2)
    sum = band_matrix_1 + band_matrix_2 * -1
    print(sum)

    mat_3 = Matrix(3, 1, [1, 2, 3])
    multiplied = SymmetricBandMatrix.mtimes(band_matrix_1, mat_3)
    print(multiplied)


#symmetric_band_matrix_example()
