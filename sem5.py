import matplotlib.pyplot as mpl
import math as m
import numpy as np
import random as rnd

def f(x):

    return np.array([-5*x[0] - 6*x[1], 8*x[0] + 9*x[1]])

#Коши x(0)= -4, y(0) = 5

start = 0
end = 1
x_0 = np.array([-4, 5])

def Actual_ans(t):

    return np.array([-3*m.exp(3*t) - m.exp(t), 4*m.exp(3*t) + m.exp(t)])

def Euler_1(n):

    tau = (end - start)/n
    ans = [x_0]

    for i in range(n):

        x_prev = ans[i]
        x_i = x_prev + tau*f(x_prev) 
        ans.append(x_i)

    return ans

def Euler_2(n):

    tau = (end - start)/n
    ans = [x_0]

    for i in range(n):

        x_prev = np.array(ans[i])
        x_calc =  x_prev + tau*f(x_prev)
        x_i = x_prev + tau*f(x_prev/2 + x_calc/2)
        ans.append(x_i)

    return ans

def R_K(n):

    tau = (end - start)/n
    ans = [x_0]

    for i in range(n):

        x_prev = np.array(ans[i])
        f1 = f(x_prev)
        f2 = f(x_prev + tau/2*f1)
        f3 = f(x_prev + tau/2*f2)
        f4 = f(x_prev + tau*f3)
        x_i = x_prev + tau/6*(f1 + 2*f2 + 2*f3 + f4)
        ans.append(x_i)

    return ans

eps_1 = []
eps_2 = []
eps_3 = []
steps = []

for n in range (100, 1100, 100):

    
    eu_1 = Euler_1(n)
    eu_2 = Euler_2(n)
    r_k = R_K(n)
    e1_max = 0
    e2_max = 0
    e3_max = 0
    tau = (end - start)/n

    for i in range(n):

        ref = Actual_ans(tau*i)
        
        e1_max = max(e1_max, abs(eu_1[i] - ref)[0], abs(eu_1[i] - ref)[1]) 
        e2_max = max(e2_max, abs(eu_2[i] - ref)[0], abs(eu_2[i] - ref)[1]) 
        e3_max = max(e3_max, abs(r_k[i] - ref)[0], abs(r_k[i] - ref)[1])

    eps_1.append(m.log(e1_max))
    eps_2.append(m.log(e2_max))
    eps_3.append(m.log(e3_max))
    steps.append(m.log(tau))

k, b = np.polyfit(steps, eps_1, 1)
label = 'Прямой метод Эйлера y = %gx + %g' %(k, b)
mpl.plot(steps, eps_1, 'bo-', label=label)
k, b = np.polyfit(steps, eps_2, 1)
mpl.plot(steps, eps_2, 'go-', label=('Непрямой метод Эйлера с персечётом y = %gx + %g' %(k, b)))
k, b = np.polyfit(steps, eps_3, 1)
mpl.plot(steps, eps_3, 'ro-', label=('метод Рунге-Куты 4-го порядка y = %gx + %g' %(k, b)))
mpl.grid()
mpl.xlabel('Шаг')
mpl.ylabel('Разность')
mpl.title('График погрешности методов')
mpl.legend(loc='best', bbox_to_anchor = (1, -0.1))
mpl.tight_layout()
mpl.show()

n = 5
end = 1
r_k = Euler_1(n)
r_k1 = []
r_k2 = []
ref1 = []
ref2 = []
tau = (end - start)/n
steps = []

for i in range(n):

    ans = Actual_ans(tau*i)
    ref1.append(ans[0])
    ref2.append(ans[1])
    r_k1.append(r_k[i][0])
    r_k2.append(r_k[i][1])
    steps.append(tau*i)

mpl.plot(steps, r_k1, 'bo-', label=('метод Рунге-Куты 4-го порядка x'))
#mpl.plot(steps, r_k2, 'go-', label=('метод Рунге-Куты 4-го порядка y'))
mpl.plot(steps, ref1, 'ro-', label=('Рещение x'))
#mpl.plot(steps, ref2, 'o-', label=('Рещение y'))
mpl.grid()
mpl.xlabel('Шаг')
mpl.ylabel('Значение в точке')
mpl.title('График решений')
mpl.legend(loc='best', bbox_to_anchor = (1, -0.1))
mpl.tight_layout()
mpl.show()
