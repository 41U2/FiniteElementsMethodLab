# ЗАДАНИЕ НАЧАЛЬНЫХ УСЛОВИЙ
# Nx = 4;
# Ny = 3;
# x0 = 0;
# y0 = 0;
# hx = [0, 1, 2 , 3];
# hy = [0, 2, 1];
#
#
# def triangulation(x0, y0, Nx, Ny, hx, hy):
#     # ФОРМИРОВАНИЕ СПИСКА ВЕРШИН
#     points = []
#     i = 0
#     points.append([x0 + hx[0], y0 + hy[0]])
#
#     while i < Nx * Ny:
#         j = i
#         if j >= Nx:
#             j = j % Nx
#         points.append([points[i % Nx][0] + hx[j], points[i - j][1] + hy[i // Nx]])
#         i += 1
#     points.pop(0)
#
#     # ФОРМИРОВАНИЕ МАТРИЦЫ СМЕЖНОСТИ - СООТВЕТСТВИЕ КАЖДОЙ ВЕРШИНЕ НОМЕРОВ СВЯЗАННЫХ ВЕРШИН В ПОРЯДКЕ ВОЗРАСТАНИЯ СТЕПЕНЕЙ СВОБОДЫ
#     # ФОРМИРОВАНИЕ МАССИВА СТЕПЕНЕЙ СВОБОДЫ ДЛЯ КАЖДОЙ ВЕРШИНЫ
#     AdjMatrix = []  # Adjacency Matrix
#     FrDeg = []  # Freedom Degree
#     i = 0
#     while i < Nx * Ny:
#         # вершина - левый нижний или правый верхний угол
#         if i == 0:
#             AdjMatrix.append([i + 1, i + Nx])
#             FrDeg.append(2)
#         elif i == (Nx * Ny - 1):
#             AdjMatrix.append([i - Nx, i - 1])
#             FrDeg.append(2)
#         # вершина - правый нижний или левый верхний угол
#         elif i == Nx - 1:
#             AdjMatrix.append([i - 1, i + Nx, i + (Nx - 1)])
#             FrDeg.append(3)
#         elif i == Nx * (Ny - 1):
#             AdjMatrix.append([i - Nx, i + 1, i - (Nx - 1)])
#             FrDeg.append(3)
#         # вершина - нижняя или верхняя сторона, за исключением углов
#         elif 0 < i < Nx:
#             if i == 1:
#                 AdjMatrix.append([i - 1, i + 1, i + Nx - 1, i + Nx])
#             elif i == Nx - 2:
#                 AdjMatrix.append([i + 1, i - 1, i + Nx - 1, i + Nx])
#             FrDeg.append(4)
#         elif Nx * (Ny - 1) < i < Nx * Ny - 1:
#             if i == Nx * Ny - 2:
#                 AdjMatrix.append([i + 1, i - 1, i - (Nx - 1), i - Nx])
#             elif i == Nx * (Ny - 1) + 1:
#                 AdjMatrix.append([i - 1, i + 1, i - (Nx - 1), i - Nx])
#             FrDeg.append(4)
#         # вершина - правая или левая сторона
#         elif i % Nx == Nx - 1:
#             if i == Nx * (Ny - 1) - 1:
#                 AdjMatrix.append([i + Nx, i - Nx, i + Nx - 1, i - 1])
#             elif i == 2 * Nx - 1:
#                 AdjMatrix.append([i - Nx, i + Nx, i + Nx - 1, i - 1])
#             FrDeg.append(4)
#         elif i % Nx == 0:
#             if i == Nx:
#                 AdjMatrix.append([i - Nx, i + Nx, i - (Nx - 1), i + 1])
#             elif i == Nx * (Ny - 2):
#                 AdjMatrix.append([i + Nx, i - Nx, i - (Nx - 1), i + 1])
#             FrDeg.append(4)
#         # вершина лежит внутри фигуры
#         else:
#             if i == Nx + 1:
#                 AdjMatrix.append([i + Nx - 1, i - Nx + 1, i - Nx, i + Nx, i - 1, i + 1])
#             elif i == Nx * (Ny - 2) + 1:
#                 AdjMatrix.append([i - Nx + 1, i + Nx - 1, i - Nx, i + Nx, i - 1, i + 1])
#             elif i == 2 * (Nx - 1):
#                 AdjMatrix.append([i - Nx + 1, i + Nx - 1, i - Nx, i + Nx, i + 1, i - 1])
#             elif i == Nx * (Ny - 1) - 2:
#                 AdjMatrix.append([i + Nx - 1, i - Nx + 1, i - Nx, i + Nx, i + 1, i - 1])
#             else:
#                 AdjMatrix.append([i + Nx - 1, i - Nx + 1, i - Nx, i + Nx, i + 1, i - 1])
#             FrDeg.append(6)
#         i += 1
#     return [points, AdjMatrix]
#
# print(triangulation(x0, y0, Nx, Ny, hx, hy)[0]); - Вывод сформированного массива точек
# print(triangulation(x0, y0, Nx, Ny, hx, hy)[1]); - Вывод Матрицы смежности
from typing import List, Tuple


# Метод, в котором реализованы формирование списка вершин разбиения, матрицы смежности и
# списка вершин, составляющих треугольные элементы
def triangulation(
        x_start: float, y_start: float,
        vertices_num_x: int, vertices_num_y: int,
        steps_x: List[float], steps_y: List[float]
       ) -> Tuple[List[Tuple[int, List[float]]], List[List[float]], List[Tuple[int, int, int]], List[Tuple[int, bool]]]:
    vertices_num = vertices_num_x * vertices_num_y
    vertices = []
    adjacency_matrix = []
    for i in range(vertices_num):
        row = [0] * vertices_num
        adjacency_matrix.append(row)
    triangle_indices = []
    is_boundary_vertex = []
    vertex_index = 0
    # Заполняем координаты точек, имеющие стартовое значение y-координаты
    current_y_coord = y_start
    for i_x in range(vertices_num_x):
        if i_x == 0:
            vertices.append((vertex_index, [x_start, current_y_coord]))
            is_boundary_vertex.append((vertex_index, True))
        else:
            current_x_coord = vertices[-1][1][0] + steps_x[i_x - 1]
            vertices.append((vertex_index, [current_x_coord, current_y_coord]))
            is_boundary_vertex.append((vertex_index, True))
        vertex_index += 1
    # Заполняем координаты остальных точек
    for i_y in range(1, vertices_num_y):
        current_y_coord = vertices[-1][1][1] + steps_y[i_y - 1]
        for i_x in range(vertices_num_x):
            if i_x == 0:
                vertices.append((vertex_index, [x_start, current_y_coord]))
                is_boundary_vertex.append((vertex_index, True))
            elif i_x == vertices_num_x - 1 or i_y == vertices_num_y - 1:
                current_x_coord = vertices[-1][1][0] + steps_x[i_x - 1]
                vertices.append((vertex_index, [current_x_coord, current_y_coord]))
                is_boundary_vertex.append((vertex_index, True))
            else:
                current_x_coord = vertices[-1][1][0] + steps_x[i_x - 1]
                vertices.append((vertex_index, [current_x_coord, current_y_coord]))
                is_boundary_vertex.append((vertex_index, False))
            vertex_index += 1
    # Заполняем матрицу смежности
    # Для всех горизонтальных сторон прямоугольной области, кроме последней
    for i in range(vertices_num_y - 1):
        # Тут каждая вершина связывается с тремя другими
        for j in range(vertices_num_x - 1):
            # Сохраняем индексы вершин, образующие треугольные элементы
            triangle_indices.append((
                (vertices_num_x * i) + j,
                (vertices_num_x * i) + vertices_num_x + 1 + j,
                (vertices_num_x * i) + 1 + j
            ))
            triangle_indices.append((
                (vertices_num_x * i) + j,
                (vertices_num_x * i) + vertices_num_x + j,
                (vertices_num_x * i) + vertices_num_x + 1 + j
            ))
            # Добавляем единицы в строку
            adjacency_matrix[(vertices_num_x * i) + j][(vertices_num_x * i) + 1 + j] = 1
            adjacency_matrix[(vertices_num_x * i) + j][(vertices_num_x * i) + vertices_num_x + j] = 1
            adjacency_matrix[(vertices_num_x * i) + j][(vertices_num_x * i) + vertices_num_x + 1 + j] = 1
            # Добавляем единицы зеркально в столбец
            adjacency_matrix[(vertices_num_x * i) + 1 + j][(vertices_num_x * i) + j] = 1
            adjacency_matrix[(vertices_num_x * i) + vertices_num_x + j][(vertices_num_x * i) + j] = 1
            adjacency_matrix[(vertices_num_x * i) + vertices_num_x + 1 + j][(vertices_num_x * i) + j] = 1
        # Связь последней вершины в строке с нижестоящей (добавление в строку и в столбец)
        adjacency_matrix[vertices_num_x + (vertices_num_x * i) - 1][2 * vertices_num_x + (vertices_num_x * i) - 1] = 1
        adjacency_matrix[2 * vertices_num_x + (vertices_num_x * i) - 1][vertices_num_x + (vertices_num_x * i) - 1] = 1
    # Для последней горизонтальной строки (добавление в строку и столбец)
    for j in range(vertices_num_x - 1):
        adjacency_matrix[vertices_num_x * (vertices_num_y - 1) + j][vertices_num_x * (vertices_num_y - 1) + j + 1] = 1
        adjacency_matrix[vertices_num_x * (vertices_num_y - 1) + j + 1][vertices_num_x * (vertices_num_y - 1) + j] = 1
    return vertices, adjacency_matrix, triangle_indices, is_boundary_vertex
