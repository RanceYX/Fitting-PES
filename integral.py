import math


def get_func12(func1, func2):
    func = []
    length = len(func1)
    i = 0
    while i < length:
        y = func1[i] * func2[i]
        func.append(y)
        i = i+1
    return func


def get_integl(func, Ang, dtheta):
    i = 1
    S = 0.0
    h = (Ang[-1] - Ang[0]) / len(Ang)
    while i < len(Ang)/2:
        y1 = func[2*i-2]*math.sin(Ang[2*i-2])
        y2 = func[2*i-1]*math.sin(Ang[2*i-1])
        y3 = func[2*i]*math.sin(Ang[2*i])
        s = h*(y1+4*y2+y3)/3
        S = S + s
        i = i+1

    return S
