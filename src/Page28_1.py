import math

x = float(input("x-in qiymətini daxil et: "))
p = float(input("p-nin qiymətini daxil et: "))
eps = float(input("eps-nin qiymətini daxil et: "))

u = x / 2

while True:
    y = u
    u = ((p - 1) * y + x / math.exp((p - 1) * math.log(y))) / p
    if abs(u - y) < eps:
        break

print(f"{x:.6f} ədədinin {p}-ci dərəcədən kökü= {u:.10f}")
