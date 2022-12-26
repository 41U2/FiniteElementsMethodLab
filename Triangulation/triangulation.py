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
    # Для первой горизонтальной строки
    for j in range(vertices_num_x - 1):
        # Добавляем единицу в строку
        adjacency_matrix[j][j + 1] = 1
        # Зеркально добавляем единицу в столбец
        adjacency_matrix[j + 1][j] = 1
    # Для всех горизонтальных сторон прямоугольной области, кроме первой
    for i in range(vertices_num_y - 1):
        # Тут каждая вершина связывается с тремя другими
        for j in range(vertices_num_x - 1):
            # Сохраняем индексы вершин, образующие треугольные элементы
            triangle_indices.append((
                (vertices_num_x * i) + vertices_num_x + j,
                (vertices_num_x * i) + 1 + j,
                (vertices_num_x * i) + vertices_num_x + 1 + j
            ))
            triangle_indices.append((
                (vertices_num_x * i) + vertices_num_x + j,
                (vertices_num_x * i) + j,
                (vertices_num_x * i) + 1 + j
            ))
            # Добавляем единицы в строку
            adjacency_matrix[(vertices_num_x * i) + vertices_num_x + j][(vertices_num_x * i) + vertices_num_x + 1 + j] = 1
            adjacency_matrix[(vertices_num_x * i) + vertices_num_x + j][(vertices_num_x * i) + 1 + j] = 1
            adjacency_matrix[(vertices_num_x * i) + vertices_num_x + j][(vertices_num_x * i) + j] = 1
            # Добавляем единицы зеркально в столбец
            adjacency_matrix[(vertices_num_x * i) + vertices_num_x + 1 + j][(vertices_num_x * i) + vertices_num_x + j] = 1
            adjacency_matrix[(vertices_num_x * i) + 1 + j][(vertices_num_x * i) + vertices_num_x + j] = 1
            adjacency_matrix[(vertices_num_x * i) + j][(vertices_num_x * i) + vertices_num_x + j] = 1
        # Связь последней вершины в строке с нижестоящей (добавление в строку и в столбец)
        j = vertices_num_x - 2
        adjacency_matrix[(vertices_num_x * i) + vertices_num_x + 1 + j][(vertices_num_x * i) + 1 + j] = 1
        adjacency_matrix[(vertices_num_x * i) + 1 + j][(vertices_num_x * i) + vertices_num_x + 1 + j] = 1
    return vertices, adjacency_matrix, triangle_indices, is_boundary_vertex
