# ПЕРЕНУМЕРАЦИЯ СПИСКА ВЕРШИН
# def ReNum(NewOrder_unique, AdjMatrix, points, Nx, Ny):
#     i = 0
#     points_new = []  # Новый список вершин, полученный после перенумерации алгоритмом Катхилла-Макки
#     while i < Nx * Ny:
#         points_new.append(points[NewOrder_unique[i]])
#         i += 1
#     # print(points_new);
#
#     # ЗАПОЛНЕНИЕ НОВОЙ МАТРИЦЫ СМЕЖНОСТИ
#     i = 0
#     j = 0
#     AdjMatrix_new = AdjMatrix  # Новая матрица смежности, полученная после перенумерации вершин
#     while i < len(AdjMatrix_new):
#         j = 0
#         while j < len(AdjMatrix_new[i]):
#             AdjMatrix_new[i][j] = NewOrder_unique[AdjMatrix_new[i][j]]
#             j += 1
#         i += 1
#
#     AdjMatrix_new1 = []
#     i = 0
#     while i < len(NewOrder_unique):
#         AdjMatrix_new1.append(AdjMatrix_new[NewOrder_unique.index(i)])
#         i += 1
#     return [points_new, AdjMatrix_new1]
#
# print(ReNum(CuthillMcKee(triangulation(x0, y0, Nx, Ny, hx, hy)[1]), triangulation(x0, y0, Nx, Ny, hx, hy)[1], triangulation(x0, y0, Nx, Ny, hx, hy)[0], Nx, Ny)[0], Nx, Ny); # Новый массив вершин
# print(ReNum(CuthillMcKee(triangulation(x0, y0, Nx, Ny, hx, hy)[1]), triangulation(x0, y0, Nx, Ny, hx, hy)[1], triangulation(x0, y0, Nx, Ny, hx, hy)[0], Nx, Ny)[1], Nx, Ny); # Новая матрица смежности

# Формирование списка вершин, а также новой матрицы
# смежности (после К-М)
from typing import Dict, List, Tuple


def apply_new_indices(old_to_new_indices: Dict[int, int], vertices: List[Tuple[int, List[float]]],
                      triangle_indices: List[Tuple[int, int, int]], is_boundary_vertex: List[Tuple[int, bool]]
                      ) -> Tuple[List[List[float]], List[Tuple[int, int, int]], List[bool]]:
    new_vertices = [(old_to_new_indices[old_index], coordinates) for old_index, coordinates in vertices]
    new_vertices = [new_vertex[1] for new_vertex in sorted(new_vertices, key=lambda elem: elem[0])]

    new_triangle_indices = [(old_to_new_indices[i],
                             old_to_new_indices[j],
                             old_to_new_indices[k]) for i, j, k in triangle_indices]

    new_is_boundary_vertex = [(old_to_new_indices[old_index], value) for old_index, value in is_boundary_vertex]
    new_is_boundary_vertex = [new_is_boundary[1] for new_is_boundary in
                              sorted(new_is_boundary_vertex, key=lambda elem: elem[0])]

    return new_vertices, new_triangle_indices, new_is_boundary_vertex
