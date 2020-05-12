num = input("정수 입력: ")
num2=len(num)
num = int(num)

b = []

for i in range(2*num2+num2):
    b.append(num%2)
    num=num//2
    if  num <= 0:
        break
print(b)