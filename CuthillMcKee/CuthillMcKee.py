# АЛГОРИТМ КАТХИЛЛА-МАККИ (ОБРАТНЫЙ) - вход: матрица смежности, Nx, Ny; выход: перенумерованный список вершин
# def CuthillMcKee(AdjMatrix, Nx, Ny):
#     i = 0
#     NewOrder = []
#     NewOrder_unique = []  # Список соответствия старых вершин новым. Старая вершина - индекс элемента, новая вершина - элемент по этому индексу
#     NewOrder.append(0)
#     NewOrder_unique.append(0)
#
#     for i in NewOrder_unique:
#         if len(NewOrder_unique) >= Nx * Ny:
#             break
#         for j in AdjMatrix[i]:
#             NewOrder.append(j)
#         for k in NewOrder:
#             if k not in NewOrder_unique:
#                 NewOrder_unique.append(k)
#
#     NewOrder_unique.reverse()
#     return NewOrder_unique
from typing import List, Dict


def CuthillMcKee(adjacency_matrix: List[List[float]]) -> Dict[int, int]:
    n_cols = len(adjacency_matrix)
    freedom_degrees = {}
    for index, row in enumerate(adjacency_matrix):
        freedom_degrees[index] = sum(row)
    # Начинаем с одной из вершин с минимальной степенью свободы
    start_vertex_index = sorted(freedom_degrees, key=lambda key: freedom_degrees[key])[0]
    nodes = [start_vertex_index]
    neighbours = []
    marked_vertex_indices = [start_vertex_index]
    while len(nodes) != len(adjacency_matrix):
        tmp = []
        for i_col in range(n_cols):
            adjacency_value = adjacency_matrix[nodes[-1]][i_col]
            if adjacency_value == 1:
                tmp.append((i_col, freedom_degrees[i_col]))
        tmp = sorted(tmp, key=lambda elem: elem[1])
        # Добавляем соседей для рассматриваемой вершины в порядке возрастания их степеней свободы
        for neighbour in tmp:
            if neighbour[0] not in marked_vertex_indices:
                marked_vertex_indices.append(neighbour[0])
                neighbours.append(neighbour[0])
        nodes.append(neighbours[0])
        neighbours = neighbours[1:]
    # Возвращаем словарь для перехода от старой нумерации узлов к новой
    old_to_new_indices = {}
    for index, value in enumerate(nodes[::-1]):
        old_to_new_indices[value] = index
    return old_to_new_indices
