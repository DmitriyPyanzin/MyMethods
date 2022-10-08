# НегаФибоначчи

list_1 = list()
a0 = 0
a1 = 1
n = int(input())
for i in range(n + 1):
    list_1.append(a0)
x = a0 + a1
a0 = a1
a1 = x
list_2 = [list_1[i] * (-1) ** (i + 1) for i in range(len(list_1))][::-1]
print(list_2 + list_1[1:])