import random

print("hello,world")
a=[]
for i in range(500):
    a.append([])
    for j in range(3):
        a[i].append(random.randint(0,256))
print(a)
