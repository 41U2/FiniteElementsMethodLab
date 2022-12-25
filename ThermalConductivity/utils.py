from typing import List, Tuple


def get_triangle_area(vertices: Tuple[List[float], List[float], List[float]]) -> float:
    x = 0
    y = 1
    return 0.5 * abs((vertices[1][x] - vertices[0][x]) * (vertices[2][y] - vertices[0][y]) -
                     (vertices[2][x] - vertices[0][x]) * (vertices[1][y] - vertices[0][y]))
