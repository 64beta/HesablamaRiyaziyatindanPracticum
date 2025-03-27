#kitabda kod ve sekil uyusmur

def f(x):
    return x**3 - x - 2  # Burada istənilən funksiya yazıla bilər

eps = 1e-10

a = float(input())
b = float(input())

if f(a) * f(b) > 0:
    exit()

while True:
    c = 0.5 * (a + b)
    if f(c) == 0 or abs(b - a) < eps:
        break
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print(f"Tənliyin kökü x = {c:20.15f}")
