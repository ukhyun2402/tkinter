def go(row = 5 , col = 5):
    result = list()
    for i in range(row):
        tmp = list()
        for j in range(col):
            tmp.append("X")
        result.append(tmp)
    return result

A = go(6,8)
for i in A:
    print(i)


array= [[None] * 50 for i in range(10)]
print(array)    