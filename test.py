def neighbors(x):
    for direct in [1, -1]:
        yield x + direct

for v in neighbors(2):
    print(v)

for v in neighbors(3):
    print(v)