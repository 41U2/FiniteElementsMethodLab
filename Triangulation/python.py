Nx = 4;
Ny = 3;
x0 = 0;
y0 = 0;
hx = [0, 1, 2 , 3];
hy = [0, 2, 1];


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

print(points);


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
print(AdjMatrix); 
print(FrDeg);


#�������� ��������-����� (��������)
i=0;
NewOrder = [];
NewOrder_unique = []; # ������ ������������ ������ ������ �����. ������ ������� - ������ ��������, ����� ������� - ������� �� ����� �������
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
print(NewOrder_unique);


#������������� ������ ������
i=0;
points_new = []; # ����� ������ ������, ���������� ����� ������������� ���������� ��������-�����
while i < Nx*Ny:
    points_new.append(points[NewOrder_unique[i]]);
    i+=1;
print(points_new);

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
#print(AdjMatrix_new);
print(AdjMatrix_new1);