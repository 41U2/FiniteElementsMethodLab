#������������� ������ ������
def ReNum(NewOrder_unique, AdjMatrix, points):
    i=0;
    points_new = []; # ����� ������ ������, ���������� ����� ������������� ���������� ��������-�����
    while i < Nx*Ny:
        points_new.append(points[NewOrder_unique[i]]);
        i+=1;
    #print(points_new);

    #���������� ����� ������� ���������
    i=0;
    j=0;
    AdjMatrix_new = AdjMatrix; #����� ������� ���������, ���������� ����� ������������� ������
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

#print(ReNum(CuthillMcKee(triangulation(x0, y0, Nx, Ny, hx, hy)[1]), triangulation(x0, y0, Nx, Ny, hx, hy)[1], triangulation(x0, y0, Nx, Ny, hx, hy)[0])[0]); # ����� ������ ������
#print(ReNum(CuthillMcKee(triangulation(x0, y0, Nx, Ny, hx, hy)[1]), triangulation(x0, y0, Nx, Ny, hx, hy)[1], triangulation(x0, y0, Nx, Ny, hx, hy)[0])[1]); # ����� ������� ���������