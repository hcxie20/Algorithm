def find_ls_k(a, k):
    if not a:
        return a

    l = len(a)

    p = [0] * l
    p[0] = a[0]

    p_min = p[0]
    p_first_k = [p[0]]

    def findKth(i):
        if i < k:
            return p_min
        else:
            return p_kth

    for i in range(1, l):
        p[i] = a[i] ^ findKth(i)

        p_min = min(p_min, p[i])

        p_first_k.append(p[i])
        if i == k - 1:
            p_kth = min(p_first_k)
        elif i > k - 1:
            p_first_k.pop(p_first_k.index(min(p_first_k)))
            p_kth = min(p_first_k)

    return p[-1]


if __name__ == '__main__':
    n = 5
    k = 3
    ls = [2, 3, 2, 5, 4]
    print(find_ls_k(ls, k))
    n = 5
    k = 2
    ls = [2, 3, 2, 5, 4]
    print(find_ls_k(ls, k))
