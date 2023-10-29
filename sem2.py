import matplotlib.pyplot as mpl
import math as m
import numpy as np
import random as rnd

def m_func(x):

    return m.cos(x)*m.sin(x)

start = 0
end = 1
ref = 1/2 - (m.cos(1)**2)/2

def integral_left_rec(func, num):

    integral = 0
    h = (end - start)/num
    x = start

    for i in range(num):
        
        integral += (func(x)*h)
        x += h

    return integral

def integral_right_rec(func, num):

    integral = 0
    h = (end - start)/num
    x = start

    for i in range(num - 1):
        
        x += h
        integral += (func(x)*h)

    integral += (func(x)*h)

    return integral

def integral_trapeze(func, num):

    integral = 0
    h = (end - start)/num
    x = start

    for i in range(num - 1):
        
        integral += ((func(x) + func(x + h))/2*h)
        x += h

    integral += ((func(x) + func(x - h))/2*h)

    return integral

def integral_mid_rec(func, num):

    integral = 0
    h = (end - start)/num
    x = start

    for i in range(num):
        
        integral += (func(x + h/2)*h)
        x += h

    return integral

def integral_simpson(func, num):

    integral = 0
    h = (end - start)/num
    x = start

    for i in range(num - 1):
        
        integral += ((func(x) + func(x + h) + 4*func(x + h/2))/6*h)
        x += h

    integral += ((func(x) + func(x - h) + 4*func(x - h/2))/6*h)

    return integral


def integral_montecarlo(func, num):

    integral = 0
    rnd.seed()

    for i in range(num):
        
        x = rnd.random()*(end - start)
        y = rnd.random()*(end - start)

        if y <= func(x):    integral += 1

    return integral/num

h_list = []
left_list = []
right_list = []
mid_list = []
trapeze_list = []
simpson_list = []
montecarlo_list = []

num = 200


for i in range(6):

    h_list.append(m.log((end-start)/num))
    left_list.append(m.log(abs(ref - integral_left_rec(m_func, num))))
    right_list.append(m.log(abs(ref - integral_right_rec(m_func, num))))
    mid_list.append(m.log(abs(ref - integral_mid_rec(m_func, num))))
    trapeze_list.append(m.log(abs(ref - integral_trapeze(m_func, num))))
    simpson_list.append(m.log(abs(ref - integral_simpson(m_func, num))))
    montecarlo_list.append(m.log(abs(ref - integral_montecarlo(m_func, num))))
    num *= 2

fig, ax = mpl.subplots()
ax.plot(h_list, left_list, '-', h_list, right_list, '--', h_list, mid_list, '-.', h_list, trapeze_list, h_list, simpson_list, h_list, montecarlo_list)
k, b = np.polyfit(h_list, left_list, 1)
print('left_rec', k, b)
k, b = np.polyfit(h_list, right_list, 1)
print('right_rec', k, b)
k, b = np.polyfit(h_list, mid_list, 1)
print('mid_rec', k, b)
k, b = np.polyfit(h_list, trapeze_list, 1)
print('trapeze', k, b)
k, b = np.polyfit(h_list, simpson_list, 1)
print('simpson', k, b)
k, b = np.polyfit(h_list, montecarlo_list, 1)
print('montecarlo', k, b)
mpl.show()

eps = 1E-5
b_0 = eps**3 / 3
m_func = lambda x: 1/m.sqrt(x)

num = 200
end = b_0
start = 0
integral_part1 = integral_right_rec(m_func, num)
start = b_0
end = 1
integral_part2 = integral_right_rec(m_func, num)
integral = integral_part2
ref = 2
print("Несобственный интеграл", integral, 2)