def f(x):
    return x**2  # Burada istənilən funksiya yazıla bilər

n = 100
a = float(input())
b = float(input())

h = (b - a) / (2 * n)
s = f(a) + f(b)
x = a
m = 2 * n - 1

for i in range(1, m + 1):
    x = x + h
    if i % 2 == 0:
        s = s + 2 * f(x)
    else:
        s = s + 4 * f(x)


s = s * h / 3

print(f"İnteqral S = {s:20.10f}")
