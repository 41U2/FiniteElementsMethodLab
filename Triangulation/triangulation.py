#������� ��������� �������
Nx = 4;
Ny = 3;
x0 = 0;
y0 = 0;
hx = [0, 1, 2 , 3];
hy = [0, 2, 1];


def triangulation(x0, y0, Nx, Ny, hx, hy):
    #������������ ������ ������
    points = [];
    i=0;
    points.append([ x0+hx[0], y0 + hy[0] ]);

    while i < Nx*Ny:
        j=i;
        if j>=Nx:
            j=j%Nx;
        points.append([ points[i%Nx][0]+hx[j], points[i-j][1] + hy[i//Nx] ])
        i+=1;
    points.pop(0);


    #������������ ������� ��������� - ������������ ������ ������� ������� ��������� ������ � ������� ����������� �������� �������
    #������������ ������� �������� ������� ��� ������ �������
    AdjMatrix = []; #Adjacency Matrix
    FrDeg=[]; #Freedom Degree
    i=0;
    while i < Nx*Ny:
        #������� - ����� ������ ��� ������ ������� ����
        if i == 0:
            AdjMatrix.append([i+1, i+Nx]);
            FrDeg.append(2);
        elif i == (Nx*Ny-1):
            AdjMatrix.append([i-Nx, i-1]);
            FrDeg.append(2);
        #������� - ������ ������ ��� ����� ������� ����
        elif i == Nx-1:
            AdjMatrix.append([i-1, i+Nx, i+(Nx-1)]);
            FrDeg.append(3);
        elif i == Nx*(Ny-1):
            AdjMatrix.append([i-Nx, i+1, i-(Nx-1)]);
            FrDeg.append(3);
        #������� - ������ ��� ������� �������, �� ����������� �����
        elif 0 < i < Nx:
            if i == 1:
                AdjMatrix.append([i-1, i+1, i+Nx-1, i+Nx]);
            elif i == Nx-2:
                AdjMatrix.append([i+1, i-1, i+Nx-1, i+Nx]);
            FrDeg.append(4);
        elif Nx*(Ny-1) < i < Nx*Ny-1:
            if i == Nx*Ny-2:
                AdjMatrix.append([i+1, i-1, i-(Nx-1), i-Nx]);
            elif i == Nx*(Ny-1)+1:
                AdjMatrix.append([i-1, i+1, i-(Nx-1), i-Nx]);
            FrDeg.append(4);
        #������� - ������ ��� ����� �������
        elif i%Nx == Nx-1:
            if i == Nx*(Ny-1)-1:
                AdjMatrix.append([i+Nx, i-Nx, i+Nx-1, i-1]);
            elif i == 2*Nx-1:
                AdjMatrix.append([i-Nx, i+Nx, i+Nx-1, i-1]);
            FrDeg.append(4);
        elif i%Nx == 0:
            if i == Nx:
                AdjMatrix.append([i-Nx, i+Nx, i-(Nx-1), i+1]);
            elif i == Nx*(Ny-2):
                AdjMatrix.append([i+Nx, i-Nx, i-(Nx-1), i+1]);
            FrDeg.append(4);
        #������� ����� ������ ������
        else:
            if i == Nx+1:
                AdjMatrix.append([i+Nx-1, i-Nx+1, i-Nx, i+Nx, i-1, i+1]);
            elif i == Nx*(Ny-2)+1:
                AdjMatrix.append([i-Nx+1, i+Nx-1, i-Nx, i+Nx, i-1, i+1]);
            elif i == 2*(Nx-1):
                AdjMatrix.append([i-Nx+1, i+Nx-1, i-Nx, i+Nx, i+1, i-1]);
            elif i == Nx*(Ny-1)-2:
                AdjMatrix.append([i+Nx-1, i-Nx+1, i-Nx, i+Nx, i+1, i-1]);
            else:
                AdjMatrix.append([i+Nx-1, i-Nx+1, i-Nx, i+Nx, i+1, i-1]);
            FrDeg.append(6);
        i+=1;
    return [points, AdjMatrix]

#print(triangulation(x0, y0, Nx, Ny, hx, hy)[0]); - ����� ��������������� ������� �����
#print(triangulation(x0, y0, Nx, Ny, hx, hy)[1]); - ����� ������� ���������