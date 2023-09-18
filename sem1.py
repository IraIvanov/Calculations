import matplotlib.pyplot as mpl
import math as m

def dif_h1(func, h):

    dif = []
    h

    for i in range(1, len(func) - 1):
        
        dif_i = (func[i+1] - func[i])/h
        dif.append(dif_i)

    dif.append(dif[-1])
    dif = [dif[0]] + dif
    return dif

def dif_h2(func, h):

    dif = []

    for i in range(1, len(func) - 1):
        
        dif_i = (func[i + 1] - func[i - 1])/(2*h)
        dif.append(dif_i)

    dif_0 = (-3*func[0] + 4*func[1] - func[2])/(2*h)
    dif_n = (3*func[-1] - 4*func[-2] + func[-3])/(2*h)
    dif = [dif_0] + dif + [dif_n]

    return dif

def dif_2_h2(func, h):

    dif = []

    for i in range(1, len(func) - 1):
        
        dif_i = (func[i - 1] + func[i + 1] - 2*func[i])/(h*h)
        dif.append(dif_i)

    dif_0 = (2*func[0] - 5*func[1] + 4*func[2] - func[3])/(2*h*h)
    dif_n = (-2*func[-1] + 5*func[-2] - 4*func[-3] + func[-4])/(2*h)
    dif = [dif_0] + dif + [dif_n]

    return dif

def m_func(x):

    return m.cos(x)*m.sin(x)

def m_dif(x):

    return m.cos(x)*m.cos(x) - m.sin(x)*m.sin(x)

def m_dif_2(x):

    return - 4*m.cos(x)*m.sin(x)

def main(h, num):

    main_func = m_func
    main_dif = m_dif
    main_dif_2 = m_dif_2
    func = []
    seg = []
    start = 0
    th_dif_1 = [] 
    th_dif_2 = []

    for i in range(num):
        
        func.append(main_func(start))
        th_dif_1.append(main_dif(start))
        th_dif_2.append(main_dif_2(start))
        seg.append(start)
        start += h
    
    dif_h_1, dif_h_2, dif_2 = dif_h1(func, h), dif_h2(func, h), dif_2_h2(func, h)

    for i in range(num):

        dif_h_1[i] = m.log(abs(dif_h_1[i] - th_dif_1[i]), m.e)
        dif_h_2[i] = m.log(abs(dif_h_2[i] - th_dif_1[i]), m.e)
        dif_2[i] = m.log(abs(dif_2[i] - th_dif_2[i]), m.e)

    return max(dif_h_1), max(dif_h_2), max(dif_2)

num = 200
h_lst = []
dif_h1_lst = []
dif_h2_lst = []
dif_2_lst = []


for i in range(4):

    h = m.pi/num
    dif_h_1, dif_h_2, dif_2 = main(h, num)
    h_lst.append(m.log(h, m.e))
    dif_h1_lst.append(dif_h_1)
    dif_h2_lst.append(dif_h_2)
    dif_2_lst.append(dif_2)
    num *= 2   

fig, ax = mpl.subplots()
ax.plot(h_lst, dif_h1_lst, '-', h_lst, dif_h2_lst, '--', h_lst, dif_2_lst, '-.')
mpl.savefig("plot")
    