import math

x = float(input("x-in qiymətini daxil et: "))
eps = float(input("eps-in qiymətini daxil et: "))

s = 1.0
t = 1.0
k = 0

while not abs(t) < eps:
    k += 1
    t *= - (x ** 2) / (2 * k * (2 * k - 1))
    s += t

print(f"cos({x}) = {s:12.10f}")
