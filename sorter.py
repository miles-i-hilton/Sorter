import random
num=[]
for n in range(100):
<<<<<<< HEAD
    nu=random.randint(1, 2)
=======
    nu=random.randint(1, 2000)
>>>>>>> seperate-printed-numbers
    num.append(nu)
print("100 randomly generated numbers:")
print(num)
print()
num.sort()
print("Sorted numbers in order of smallest to largest:")
for item in num:
    print(item)
