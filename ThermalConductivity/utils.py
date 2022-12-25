from typing import List, Tuple


def get_triangle_area(vertices: Tuple[List[float], List[float], List[float]]) -> float:
    x = 0
    y = 1
    return 0.5 * abs((vertices[1][x] - vertices[0][x]) * (vertices[2][y] - vertices[0][y]) -
                     (vertices[2][x] - vertices[0][x]) * (vertices[1][y] - vertices[0][y]))


def intergrate_by_triangle(
        function,
        triangle_vertices: Tuple[List[float], List[float], List[float]],
        i_vertex_in_triangle: int) -> float:
    assert i_vertex_in_triangle <= 2
    assert  i_vertex_in_triangle >= 0
    area = get_triangle_area((triangle_vertices[0], triangle_vertices[1], triangle_vertices[2]))
    neighbours = [1, 2]
    if i_vertex_in_triangle == 1:
        neighbours = [0, 2]
    if i_vertex_in_triangle == 2:
        neighbours = [0, 1]

    middle_point_1 = [
        triangle_vertices[i_vertex_in_triangle][0] + triangle_vertices[neighbours[0]][0],
        triangle_vertices[i_vertex_in_triangle][1] + triangle_vertices[neighbours[0]][1],
    ]

    middle_point_2 = [
        triangle_vertices[i_vertex_in_triangle][0] + triangle_vertices[neighbours[1]][0],
        triangle_vertices[i_vertex_in_triangle][1] + triangle_vertices[neighbours[1]][1],
    ]

    return area * (function(middle_point_1) + function(middle_point_2)) / 6.
