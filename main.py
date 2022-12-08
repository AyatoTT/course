from random import randint
import math


def getlink(v, gg):
    for i, weight in enumerate(gg[v]):
        if weight > 0:
            yield i


def arg_min(T, S):
    amin = -1
    m = max(T)  # максимальное значение
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i
    return amin


def creatematrix(value):
    matrx = [[0] * (value) for _ in range(value)]
    i = 0
    while (i < len(matrx)):
        j = i
        while (j < len(matrx[i])):
            if (i == j):
                matrx[i][j] = 0
            else:
                matrx[i][j] = int((randint(0, 1)))
                if (matrx[i][j] == 1):
                    matrx[i][j] = int((randint(0, 99)))
                matrx[j][i] = matrx[i][j]
            j += 1
        i += 1
    return matrx


def start():
    while True:
        try:
            print()
            v=int(input("Введите стартовую вершину: "))  # стартовая вершина (нумерация с нуля)
        except:
            print("Введите число")
        else:
            break
    return v

"""""
def printm(mat,n):
    for i in range(len(mat)):
        print('',i,end=" ")
    print("\n",'-'*len(mat)*3)
    for row in mat:
        print(' '.join(s.rjust(len(str(n * n)), ' ')
        for s in map(str, row)))
    #print()
    #for mat in mat:
        #print(*mat)
"""""
def printm(mtx, n):
    print()
    print('    ', end=' ')
    [print("%2d" % i, end=' ') for i in range(0, len(mtx))]
    print()
    print('-' * (len(mtx[0]) * 3 + 4))

    for i, row in enumerate(mtx):
        print("%2d |" % (i), end=' ')
        for col in row:
            print("%2d" % col, end=' ')
        print()


def print2file(gg, T):
    fout = open('Dxtra.txt', 'w')  # 'w' - это режим "запись" ("write")
    #for i in range(len(gg)):
        #print(gg[i],file=fout)
    print(file=fout)
    print('    ', end=' ',file=fout)
    [print("%2d" % i, end=' ',file=fout) for i in range(0, len(gg))]
    print(file=fout)
    print('-' * (len(gg[0]) * 3 + 4),file=fout)
    for i, row in enumerate(gg):
        print("%2d |" % (i), end=' ',file=fout  )
        for col in row:
            print("%2d" % col, end=' ',file=fout)
        print(file=fout)
    print(file=fout)
    print("Data on shortest paths from a given point",file=fout)
    for i in range(N):
     print("%3d" %  i, end=" " , file=fout)
    print(file=fout)
    for i in range(len(T)):
        if (T[i]== math.inf) or (T[i]==0):
            print("","np",end=" ",file=fout)
        else:
            print("%3d" % T[i],end=" ",file=fout)
    fout.close()
    return


def print2secfile(gg, T):
    fout = open('matrix.txt', 'w')  # 'w' - это режим "запись" ("write")
    for i, row in enumerate(gg):
        for col in row:
            print("%2d" % col, end=' ',file=fout)
        print(file=fout)
    return


def printresult(N, T):
    print()
    for i in range(N):
     print("%3d" % i, end=" ")

    print()
    for i in range(len(T)):
        if (T[i]== math.inf) or (T[i]==0):
            print("","np",end=" ")
        else:
            print("%3d" % T[i],end=" ")
    return


while True:
    try:
        wi = int(input("1)Рандомные связи и значения\n2)Ввод из файла\nВаш выбор: "))
    except:
        print("Введите число")
    else:
        break


while True:
    if wi==1 :
        while True:
            try:
                n = int(input("Введите количество вершин:  "))
            except:
                print("Введите число")
            else:
                break
        gg = creatematrix(n)
        break
    elif wi==2 :
        gg = []
        file = open("matrix.txt", "r")
        with open('matrix.txt') as f:
        #data = file.read()
            for line in f:
                n = len(line)
                gg.append([float(x) for x in line.split()])
        break
    elif wi!=1 or wi!=2:
        while True:
            try:
                print()
                wi = int(input("1)Рандомные связи и значения\n2)Ввод из файла\nВаш выбор: "))
            except:
                print("Введите число 1 или 2 ")
            else:
                break
    else:
        break

#gg=createMatrix(n)
printm(gg, n)
N=len(gg)
T = [math.inf]*N
v=start()


while v>n or v==n :
    print("Введите существующую вершину!!! ")
    v=start()

S = {v}    # просмотренные вершины
T[v] = 0   # нулевой вес для стартовой вершины


while v != -1:  # цикл, пока не просмотрим все вершины
    for j in getlink(v, gg): # перебираем все связанные вершины с вершиной v
        if j not in S:      # если вершина еще не просмотрена
            w = T[v] + gg[v][j]
            if w < T[j]:
                T[j] = w
    v = arg_min(T, S)            # выбираем следующий узел с наименьшим весом
    if v >= 0:                   # выбрана очередная вершина
        S.add(v)                 # добавляем новую вершину в рассмотрение


printresult(N, T)
if wi == 1:
    print2file(gg, T)
print2secfile(gg, T)