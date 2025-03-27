def f(x):
    return x**2  # Burada istənilən funksiya yazıla bilər

n = 100
a = float(input())
b = float(input())

h = (b - a) / n
s = 0
x = a - h / 2


for i in range(1, n + 1):
    x = x + h
    s = s + f(x)

s = s * h

print(f"İnteqral S = {s:20.10f}")
