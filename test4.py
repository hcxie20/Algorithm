def permutation(ls):
    rst = []
    find(ls, [], rst)
    return rst

def find(remains, combo, rst):
    if not remains:
        rst.append(combo)
        return
    for i in range(len(remains)):
        find(remains[:i] + remains[i+1:], combo + [remains[i]], rst)


test = ["R", "Y", "B", "G"]
rst = permutation(test)
print(rst)
pass