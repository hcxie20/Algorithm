import math
import numpy as np

def func(t, s, n):
    return (1-10**(-t/4))*math.sqrt(s)*(1+1.414*10**(-(n-1)/6))


if __name__ == "__main__":
    t = 4
    n = 4
    s = 10
    ni = list(np.linspace(1, 10, 10))
    a = [func(t, s, x) for x in ni]
    b = a[:]
    b = [x/b[len(b)-1] for x in b]
    pass