from typing import List, Dict


# АЛГОРИТМ КАТХИЛЛА-МАККИ (ОБРАТНЫЙ)
# вход: матрица смежности;
# выход: словарь вида {старый индекс вершины: новый индекс вершины}
def CuthillMcKee(adjacency_matrix: List[List[float]]) -> Dict[int, int]:
    n_vertex = len(adjacency_matrix)
    # Вычисление степенй свободы для точек
    freedom_degrees = {}
    for index, row in enumerate(adjacency_matrix):
        freedom_degrees[index] = sum(row)
    # Начинаем с одной из вершин с минимальной степенью свободы
    start_vertex_index = sorted(freedom_degrees, key=lambda key: freedom_degrees[key])[0]
    nodes = [start_vertex_index]
    neighbours = []
    marked_vertex_indices = [start_vertex_index]
    while len(nodes) != n_vertex:
        tmp = []
        for i_col in range(n_vertex):
            adjacency_value = adjacency_matrix[nodes[-1]][i_col]
            if adjacency_value == 1:
                tmp.append((i_col, freedom_degrees[i_col]))
        tmp = sorted(tmp, key=lambda elem: elem[1])
        # Добавляем соседей для рассматриваемой вершины в порядке возрастания их степеней свободы,
        # если они еще не были помечены, как просмотренные
        for neighbour in tmp:
            if neighbour[0] not in marked_vertex_indices:
                marked_vertex_indices.append(neighbour[0])
                neighbours.append(neighbour[0])
        # Добавляем следующую вершину для просмотра, убираем ее из массива соседей
        nodes.append(neighbours[0])
        neighbours = neighbours[1:]
    # Возвращаем словарь для перехода от старой нумерации узлов к новой
    old_to_new_indices = {}
    for index, value in enumerate(nodes[::-1]):
        old_to_new_indices[value] = index
    return old_to_new_indices
