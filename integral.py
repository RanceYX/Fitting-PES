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
    i = 0
    S = 0.0
    while i < len(Ang):
        S = S + func[i]*math.sin(Ang[i])*dtheta
        i = i+1
    return S
