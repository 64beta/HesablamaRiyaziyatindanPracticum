x = float(input("x-in qiymətini daxil et: "))
eps = float(input("eps-nin qiymətini daxil et: "))

u = x / 2

while True:
    y = u
    u = (y + x / y) / 2
    if abs(u - y) < eps:
        break

print(f"{x:.4f} ədədinin kvadrat kökü= {u:.10f}")
