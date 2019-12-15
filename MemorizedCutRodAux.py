import numpy as np


def memorizedCutRod(p, n):
    r = []
    for i in range(n+1):
        r.append(float("-inf"))
    return memorizedCutRodAux(p, n, r)


def memorizedCutRodAux(p, n, r):
    if r[n]>=0:
        return r[n]
    if n==0:
        q = 0
    else:
        q = float("-inf")
        for i in range(1, n+1):
            q = max(q, p[i-1] + memorizedCutRodAux(p, n-i, r))
    r[n] = q
    return q

def buttomUpCutRod(p, n):
    r = list(np.zeros(n + 1))
    r[0] = 0
    for i in range(1, n + 1):
        q = float("-inf")
        for j in range(1, i + 1):
            q = max(q, p[j - 1] + r[i - j])
        r[i] = q
    return r[n]



if __name__ == "__main__":
    p = [1, 5, 8, 9]
    n = 4
    #print(memorizedCutRod(p, n))
    print(buttomUpCutRod(p, n))
    pass
