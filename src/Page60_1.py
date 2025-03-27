def f(x):
    return x**3 - x - 2  # Burada istənilən funksiya yazıla bilər

eps = 1e-10

x0 = float(input())
x1 = float(input())
M1 = float(input())
M2 = float(input())

eps1 = eps * M2 / (M1 - M2)

while True:
    x = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
    if abs(x - x1) < eps1:
        break
    x1 = x

print(f"Tənliyin kökü x = {x1:20.15f}")
