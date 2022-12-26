from typing import Dict, List, Tuple


# Формирование списка вершин, индексов вершин треугольных элементов с учетом новой нумерации
# вход: словарь перехода старых индексов в новые, массив вершин, массив вершин которые составляют треугольные элементы,
# словарь принадлежности вершин к границе
# выход: массив вершин с новой нумерацией вида [[x0, y0], [x1, y1], ...],
# массив вершин которые составляют треугольные элементы с новой нумерацией вида [(i, j, k), ...]
# массив принадлежности вершин к границе с учетом новой нумерации
def apply_new_indices(old_to_new_indices: Dict[int, int], vertices: List[Tuple[int, List[float]]],
                      triangle_indices: List[Tuple[int, int, int]], is_boundary_vertex: List[Tuple[int, bool]]
                      ) -> Tuple[List[List[float]], List[Tuple[int, int, int]], List[bool]]:
    # Перенумерование списка вершин
    new_vertices = [(old_to_new_indices[old_index], coordinates) for old_index, coordinates in vertices]
    new_vertices = [new_vertex[1] for new_vertex in sorted(new_vertices, key=lambda elem: elem[0])]

    # Перенумерование списка вершин треугольных элементов
    new_triangle_indices = [(old_to_new_indices[i],
                             old_to_new_indices[j],
                             old_to_new_indices[k]) for i, j, k in triangle_indices]

    # Изменение порядка массива принадлежности точек к границе
    new_is_boundary_vertex = [(old_to_new_indices[old_index], value) for old_index, value in is_boundary_vertex]
    new_is_boundary_vertex = [new_is_boundary[1] for new_is_boundary in
                              sorted(new_is_boundary_vertex, key=lambda elem: elem[0])]

    return new_vertices, new_triangle_indices, new_is_boundary_vertex
