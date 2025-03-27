def f(x):
    return (x**2 + 2) / 3  # Burada istənilən funksiya yazıla bilər

eps = 1e-10

x0 = float(input())
q = float(input())

eps1 = ((1 - q) / q) * eps

while abs(f(x0) - x0) > eps1:
    x0 = f(x0)

print(f"Tənliyin kökü x = {x0:20.15f}")
