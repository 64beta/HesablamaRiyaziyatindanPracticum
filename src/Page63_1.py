import math

def f(x):
    return 2 * math.exp(x) - 2 * x - 3  # Burada istənilən funksiya yazıla bilər

def f1(x):
    return 2 * math.exp(x) - 2    # Burada funksiyanın törəməsini daxil et

eps = 1e-10

x0 = float(input())
M1 = float(input())
M2 = float(input())

eps1 = math.sqrt(2 * M2 * eps / M1)

while True:
    if f(x0) == 0:
        break
    x = x0 - f(x0) / f1(x0)
    if abs(x - x0) < eps1:
        break
    x0 = x

print(f"Tənliyin kökü x = {x0:20.15f}")
