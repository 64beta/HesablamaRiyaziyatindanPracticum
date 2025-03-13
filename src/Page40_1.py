import math

x = float(input("x-in qiymətini daxil et: "))
eps = float(input("eps-in qiymətini daxil et: "))

s = 1.0
t = 1.0
k = 0

while not abs(t) < (3 * eps / 2):
    k += 1
    t *= (x ** 2) / ((2 * k - 1) * 2 * k)  
    s += t

print(f"ch({x}) = {s:6.5f}")
