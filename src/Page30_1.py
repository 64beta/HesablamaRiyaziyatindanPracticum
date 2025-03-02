x = float(input("x-in qiymətini daxil et: "))
eps = float(input("eps-in qiymətini daxil et: "))

s = 1.0
t = 1.0
k = 0

while not abs(t) < eps:
    k += 1
    t *= x / k
    s += t

print(f"{s:20.10f}")
