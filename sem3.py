import matplotlib.pyplot as mpl
import math as m
import numpy as np
import random as rnd

def m_func(x):

    return m.cos(x)

eps = 0.001

def bin_search(f, start, end):

    if (end - start) < eps: return start + (start + end)/2

    if abs(f(start)) < eps:  return start

    if abs(f(end)) < eps:    return end
    
    if f(start)*f(end) < 0 or abs(end - start)/2 > eps:

        x1 = bin_search(f, start, (start + end)/2)
        x2 = bin_search(f, (start + end)/2, end)

        if abs(f(x2)) < eps and abs(f(x1)) < eps and abs(x2 - x1) > eps: print (x1, x2)
        if abs(f(x1)) < eps:    
            
            return x1

        if abs(f(x2)) < eps:
            
            return x2

        return x1

    else:   return start + (end - start)/2

m_start = 0
m_end = 2

print( bin_search(m_func, m_start, m_end))

def my_square(p, a):

    x_0 = a/2

    def pos(x, p, a):

        x_n = x - (x**p - a)/(p*(x**p)) 

        return x_n

    for i in range(1000):

        x_0 = pos(x_0, p, a)

    return x_0


print( my_square(3, 2))

m_end = 5

m_func = lambda x: (m.exp(-x) - m.sin(x))

m_diff = lambda x: (-m.exp(-x) - m.cos(x))

def Newton( m_func, m_diff, a):


    x_0 = a
    x_1 = 0
    x_2 = 0

    def pos(x):

        x_n = x - m_func(x)/m_diff(x) 

        return x_n

    for i in range(100):

        x = x_0
        x_0 = pos(x_0)
        m_x = x_0

        if ( x_1 - x ) != 0:

            x_2 = x_1
            x_1 = x

    return x_0, (x_2 - m_x)/(x_2 - x_1)

print(bin_search(m_func, m_start, m_end))
print(Newton( m_func, m_diff, m_start), Newton( m_func, m_diff, m_end/2), sep= ', ')


m_func = lambda x: x*m.sin(x)
m_diff = lambda x: x*m.cos(x) + m.sin(x)

print(Newton( m_func, m_diff, 0.05)[0], round(Newton( m_func, m_diff, 0.05)[1]) )