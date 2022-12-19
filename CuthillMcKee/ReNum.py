#ПЕРЕНУМЕРАЦИЯ СПИСКА ВЕРШИН
def ReNum(NewOrder_unique, AdjMatrix, points, Nx, Ny):
    i=0;
    points_new = []; # Новый список вершин, полученный после перенумерации алгоритмом Катхилла-Макки
    while i < Nx*Ny:
        points_new.append(points[NewOrder_unique[i]]);
        i+=1;
    #print(points_new);

    #ЗАПОЛНЕНИЕ НОВОЙ МАТРИЦЫ СМЕЖНОСТИ
    i=0;
    j=0;
    AdjMatrix_new = AdjMatrix; #Новая матрица смежности, полученная после перенумерации вершин
    while i < len(AdjMatrix_new):
        j=0;
        while j < len(AdjMatrix_new[i]):
                AdjMatrix_new[i][j] = NewOrder_unique[AdjMatrix_new[i][j]];
                j+=1;
        i+=1;

    AdjMatrix_new1 = [];
    i=0;
    while i < len(NewOrder_unique):
        AdjMatrix_new1.append(AdjMatrix_new[NewOrder_unique.index(i)]);
        i+=1;
    return [points_new, AdjMatrix_new1]

#print(ReNum(CuthillMcKee(triangulation(x0, y0, Nx, Ny, hx, hy)[1]), triangulation(x0, y0, Nx, Ny, hx, hy)[1], triangulation(x0, y0, Nx, Ny, hx, hy)[0], Nx, Ny)[0], Nx, Ny); # Новый массив вершин
#print(ReNum(CuthillMcKee(triangulation(x0, y0, Nx, Ny, hx, hy)[1]), triangulation(x0, y0, Nx, Ny, hx, hy)[1], triangulation(x0, y0, Nx, Ny, hx, hy)[0], Nx, Ny)[1], Nx, Ny); # Новая матрица смежности
