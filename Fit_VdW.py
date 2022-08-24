import numpy as np
from numpy import polyfit, poly1d

def get_C6(V, R_fit):
    x = R_fit
    y = V
    coeff = polyfit(x, y, 1)
    # print(coeff)
    C6 =coeff[0]
    return C6


