def threesmooth():
    S = [1]
    i2 = 0  # current index in 2S
    i3 = 0  # current index in 3S
    while True:
        print(S[-1])
        n2 = 2 * S[i2]
        n3 = 3 * S[i3]
        S.append(min(n2, n3))
        i2 += n2 <= n3
        i3 += n2 >= n3


# threesmooth()
print(-23//2)