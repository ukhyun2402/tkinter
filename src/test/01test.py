a = str(input())

list2 = []

for i in range(len(a)):
    list2.append(i-1)
    i = i +1

t = list(zip(list2,a))
print(t)
