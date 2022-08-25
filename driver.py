import IO
import integral
import Lib_Func
import Fit_VdW
import math


def driver_intgl(func1, Ang, dtheta, l):
    func2 = Lib_Func.get_Lege_poly(l, Ang)
    print("Get function2 polynomials")
    func = integral.get_func12(func1, func2)
    print("Get func1*func2")
    result = integral.get_integl(func, Ang, dtheta)
    print("Finishing the integral")
    return result


def transfer_angle(Ang_ori):
    Ang = []
    for theta_deg in Ang_ori:
        theta = theta_deg/180*math.pi
        Ang.append(theta)
    return Ang


def const_new_func(l_max, R_max, Ang_ori, PES, dtheta):
    print("Get numerical energy point from input file")
    l = 0
    V = []

    Ang = transfer_angle(Ang_ori)
    while l < l_max:
        j = 0
        V_l = []
        while j < R_max:
            V_l_r = driver_intgl(PES[j], Ang, dtheta, l) * (2*l+1)/2.0
            V_l.append(V_l_r)
            j = j+1
        print("Get V_l")
        V.append(V_l)
        l = l+1
    return V


def driver_fit(V, l_max, R_fit, R_min, R_max):
    l = 0
    C6_array = []
    R6 = []
    for r in R_fit:
        r = r/0.53
        r6 = math.pow(r,-6)
        R6.append(r6)

    while l < l_max:
        V_pri = V[l][R_min:R_max]
        c6=Fit_VdW.get_C6(V_pri, R6)
        l = l+1
        C6_array.append(c6)
    return C6_array


def ReConsV(C6,Ang,R_grid,R_min,R_max):
    L_max = len(C6)
    i = R_min
    V = []
    Poly =[]
    l = 0

    while l < L_max:
        func = Lib_Func.get_Lege_poly(l,Ang)
        Poly.append(func)
        l = l + 1
    while i < R_max:
        r = i/0.53
        V_theta = []
        j = 0
        while j < len(Ang):
            v = 0.0
            l = 0
            while l < L_max:
                v_l_r = C6[l][0]*pow(r,-6)
                pl = Poly[l][j]
                v = v + v_l_r*pl
                l = l + 1
            v = v
            V_theta.append(v)
            j = j+1
        V.append(V_theta)
        i = i + R_grid

    return V


dtheta = 9/180 * math.pi
PES = []
Ang_ori = []
data_name = 'alcl-he_all.csv'
IO.Interface_csv.read_data_deflt(data_name, Ang_ori, PES)
V_fit = const_new_func(8, 82, Ang_ori, PES, dtheta)
#IO.Interface_csv.write_data_bare('V_l.csv', V_fit)

R_fit = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,26,28,30]

Index_R_min = 60
Index_R_max = 80
l_max = 8
C6 = driver_fit(V_fit, l_max, R_fit, Index_R_min, Index_R_max)
print(C6)

R_grid = 1
R_min = 6
R_max = 120
Ang = transfer_angle(Ang_ori)
V_new = ReConsV(C6, Ang, R_grid, R_min, R_max)
IO.Interface_csv.write_data_bare('V_fitting.csv', V_new)
# print(V_new[0])








