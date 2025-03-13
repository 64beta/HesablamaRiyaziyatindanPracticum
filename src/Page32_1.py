import math

a = float(input("a-nın qiymətini daxil et: "))
x = float(input("x-in qiymətini daxil et: "))
eps = float(input("eps-in qiymətini daxil et: "))

s = 1.0
t = 1.0
k = 0

while not abs(t) < eps:
    k += 1
    t *= (x * math.log(a)) / k
    s += t

print(f"s = {s:20.10f}")
