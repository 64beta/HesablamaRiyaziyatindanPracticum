import math

x = float(input("x-in qiymətini daxil et: "))
eps = float(input("eps-in qiymətini daxil et: "))

s = x
t = x
k = 0

while not abs(t) < eps:
    k += 1
    t *= - (x ** 2) / (2 * k * (2 * k + 1))
    s += t

print(f"sin({x}) = {s:12.10f}")
