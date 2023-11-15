import numpy as np
from scipy.optimize import brent
import matplotlib.pyplot as plt

def golden_mean_search(f, a, b, tol=1e-7):
    z = (1 + np.sqrt(5)) / 2

    x1 = a
    x4 = b
    x2 = x4 - (x4 - x1) / z
    x3 = x1 + (x4 - x1) / z

    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    f4 = f(x4)

    while (x4 - x1) > tol:
        if f2 < f3:
            x4, f4 = x3, f3
            x3, f3 = x2, f2
            x2 = x4 - (x4 - x1) / z
            f2 = f(x2)
        else:
            x1, f1 = x2, f2
            x2, f2 = x3, f3
            x3 = x1 + (x4 - x1) / z
            f3 = f(x3)

    return 0.5 * (x1 + x4)

def Brent_golden(f, a, b, delta=1e-7):
    if abs(f(a)) < abs(f(b)):
        a, b = b, a  # swap bounds

    c = a
    flag = True
    err = abs(b - a)

    while err > delta:
        s = golden_mean_search(f, a, b, tol=delta)  

        if (
            (s >= b)
            or ((flag == True) and (abs(s - b) >= abs(b - c)))
            or ((flag == False) and (abs(s - b) >= abs(c - d)))
        ):
            s = golden_mean_search(f, a, b, tol=delta)  
            flag = True
        else:
            flag = False

        c, d = b, c  
        a = s

        if abs(f(a)) < abs(f(b)):
            a, b = b, a 

        err = abs(b - a)  

    return b

if __name__ == "__main__":
    f = lambda x: (x - 0.3)**2 * np.exp(x)
    a, b = 0, 1

    result_custom_brent_golden = Brent_golden(f, a, b)
    print(f"Implemented Brent (Golden Mean) result: {result_custom_brent_golden}")
    result_scipy_brent = brent(f, brack=(a, b))
    print(f"Scipy's Brent result: {result_scipy_brent}")
