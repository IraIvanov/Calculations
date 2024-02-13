import matplotlib.pyplot as mpl
import math as m
import numpy as np
import random as rnd

A = ([100,4,3,2], [1,80,3,1], [6,7,90,0], [-1,2,3,120])
F = (104 ,6 ,186, -115)
# 1, 0, 2, -1

def Jacobi(mat, f, k):

    x_0 = [0, 0, 0, 0]
    x_1 = []

    for n in range(1000):

        for j in range(k):

            x_1.append(f[j]/mat[j][j])
            
            for i in range(k):

                if i != j:
                    x_1[j] -= mat[j][i]/mat[j][j]*x_0[i]
        
        x_0 = x_1
        x_1 = []

    return x_0


def Nekrasov(mat, f):

    x_0 = [0, 0, 0, 0]

    for n in range(1000):

        for j in range(4):

            x_0[j] = f[j]/mat[j][j]

            for i in range(4):

                if i != j:

                   x_0[j] -= mat[j][i]/mat[j][j]*x_0[i]
        

    print(x_0)

print('метод Якоби',Jacobi(A, F, 4))
print('метод Зейделя-Некрасова', end = ' ')
Nekrasov(A, F)

def mat(x):

    return( x[0] + x[1]**2/2 - 4, x[1] + x[2]**2/2 - 4, x[0]**2/2 + x[2] - 4)

def jacobian(x):

    xyz = x[0]*x[1]*x[2]

    return( [1 - xyz/(1 + xyz), xyz*x[1]*x[2]/(1+xyz) - x[1], x[1]*x[2]/(1 + xyz)], [x[0]*x[2]/(1 + xyz), 1 - xyz/(1 + xyz), -x[2]/(1 + xyz)], [-x[0]/(1 + xyz), xyz/(1 + xyz), 1 / (1 + xyz)] )

def NonLinear():

    x_0 = [3, 2, 2]

    for i in range(100):

        jac = jacobian(x_0)
        f = mat(x_0)

        delta = [0 , 0, 0 ]
        for j in range(3):

            for k in range(3):
                
                delta[j] += jac[j][k]*f[k]

        for j in range(3):  x_0[j] -= delta[j]

    return x_0

x = NonLinear()

print('Решение не линейного уравнения', x)

A = ([100, 1, 0, 0, 0], [1, 100, 1, 0, 0], [0, 1, 100, 1, 0], [0, 0, 1, 100, 1], [0, 0, 0, 1, 100])
F = (101, 102, 102, 102, 101)
#1,1,1,1,1

def Progon(mat, f):

    x = [0 for i in range(5)]
    v = [0 for i in range(5)]
    u = [0 for i in range(5)]

    v[0] = -mat[0][1] / mat[0][0]
    u[0] = f[0]/mat[0][0]

    for i in range(1, 4):
        v[i] =  mat[i][i+1] / ( - mat[i][i] - mat[i][i-1]*v[i-1])
        u[i] = (mat[i][i-1]*u[i-1] - f[i-1]) / (-mat[i][i] - mat[i][i-1]*v[i-1])

    i = 4
    v[i] = 0
    u[i] = (mat[i][i-1]*u[i-1] - f[i-1]) / (-mat[i][i] - mat[i][i-1]*v[i-1])

    x[4] = u[4]

    for i in range(4, 0, -1):

        x[i-1] = v[i-1]*x[i] + u[i-1]

    return x

print('Метод прогонки', Progon(A, F))