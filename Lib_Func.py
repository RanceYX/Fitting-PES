import math


def get_Lege_poly(l,Ang):
    func =[]
    if l == 0:
        for x in Ang:
            y = 1
            func.append(y)
    elif l == 1:
        for x in Ang:
            t = math.cos(x)
            y = t
            func.append(y)
    else:
        for x in Ang:
            t = math.cos(x)
            p0 = 1
            p1 = t
            i = 1
            tem = 0.0

            while i < l:
                tem = ((2*i+1)*t*p1-i*p0)/(i+1)
                p0 = p1
                p1 = tem
                i = i+1

            y = tem
            func.append(y)
    return func


