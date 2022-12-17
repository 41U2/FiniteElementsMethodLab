#АЛГОРИТМ КАТХИЛЛА-МАККИ (ОБРАТНЫЙ) - вход: матрица смежности; выход: перенумерованный список вершин
def CuthillMcKee(AdjMatrix):
    i=0;
    NewOrder = [];
    NewOrder_unique = []; # Список соответствия старых вершин новым. Старая вершина - индекс элемента, новая вершина - элемент по этому индексу
    NewOrder.append(0);
    NewOrder_unique.append(0);

    for i in NewOrder_unique:
        if len(NewOrder_unique)>=Nx*Ny:
            break;
        for j in AdjMatrix[i]:
            NewOrder.append(j);
        for k in NewOrder:
            if k not in NewOrder_unique:
                NewOrder_unique.append(k);

    NewOrder_unique.reverse();
    return NewOrder_unique;
