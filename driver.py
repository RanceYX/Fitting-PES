import input
import integral
import Lib_Func
import Fit_VdW


def driver_intgl(func1, l):
    result = 0.0
    func2 = Lib_Func.get_Lege_poly(l)
    print("Get function2 polynomials")
    integral.get_fitfunc(func, func1, func2)
    print("Get Fitting functions")
    integral.get_integl(func, result)
    print("Finishing the integral")
    return result


def const_new_func(data_name, l_max, R_max):
    PES = []
    input.get_energy(data_name, PES)
    print("Get numerical energy point from input file")
    l = 1
    V = []
    while l < l_max:
        j = 0
        V_l = []
        while j <= R_max:
            V_l_r = driver_intgl(PES[j], l)
            V_l.append(V_l_r)
            j = j+1
        print("Get V_l")
        V.append(V_l)
        l = l+1
    return V


def driver_fit(V, l_max):
    l=0
    C6_array=[]
    while l < l_max:
        Fit_VdW.get_C6(V[l],C6)
        l = l+1
        C6_array.append(C6)
    return C6_array


V_fit = const_new_func('file_name', 8, 100)
C6 = driver_fit(V_fit, 8)
print(C6)


