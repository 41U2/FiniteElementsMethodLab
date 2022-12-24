from typing import List


class BandMatrix:

    def __init__(self, size: int, arrays: List[List[float]]):
        self.arrays = arrays
        self.size = size

        assert len(arrays) == size

    def __call__(self, i_row: int, i_col: int) -> float:
        assert i_row < self.size
        assert i_col < self.size
        if i_row <= i_col:
            n_elements = len(self.arrays[i_row])
            if i_col >= i_row + n_elements:
                return 0
            return self.arrays[i_row][i_col - i_row]

        return self.__call__(i_col, i_row)

    def __add__(self, band_matrix: "BandMatrix") -> "BandMatrix":
        assert self.size == band_matrix.size
        n_rows = len(self.arrays)
        assert n_rows == len(band_matrix.arrays)
        result_arrays = self.arrays
        for i_row in range(n_rows):
            n_cols = len(self.arrays[i_row])
            assert n_cols == len(band_matrix.arrays[i_row])
            for i_col in range(n_cols):
                result_arrays[i_row][i_col] += band_matrix.arrays[i_row][i_col]
        return BandMatrix(self.size, result_arrays)

    def __str__(self):
        result_str = ""
        for i_row in range(self.size):
            for i_col in range(self.size):
                result_str += str(self(i_row, i_col)) + " "
            result_str += "\n"
        return result_str


def example():
    arrays_1 = [
        [1, 2, 0, 3],
        [4],
        [6, 2],
        [-10]
    ]

    arrays_2 = [
        [1, 0.1, 14, -5],
        [4],
        [6, 2],
        [9.9]
    ]

    band_matrix_1 = BandMatrix(4, arrays_1)
    band_matrix_2 = BandMatrix(4, arrays_2)

    print(band_matrix_1 + band_matrix_2)

example()
