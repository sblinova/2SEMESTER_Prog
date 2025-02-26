import random as r

n = int(input('n --> '))
x = int(input('x --> '))

skaitli = []
for num in range(n):
    skaitlis = r.randint(-100, 100)
    skaitli.append(skaitlis)

kortezi = []
for i in range(len(skaitli)):
    if skaitli[i] > x:
        kortezi.append((i, skaitli[i]))

print(kortezi)
