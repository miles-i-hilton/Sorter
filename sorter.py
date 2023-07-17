import random
num=[]
for n in range(100):
    nu=random.randint(1, 2000)
    num.append(nu)
print(num)
print()
num.sort()
for item in num:
    print(item)
