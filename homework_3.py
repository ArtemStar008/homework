import random
n = int(input("размер списка: "))
A = []
for i in range(n):
    a = random.randint(0, 99)
    A.append(a)
x = A[-1]
y = A[-2]
i = A[-3]
a = (x + y + i) / 3
print("srednee " +str(a))
print("spisok " +str(A))







