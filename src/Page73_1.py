import math
def f(x):
    return math.sin(2 * x + 0.5) / (2 + math.cos(x**2 + 1))  # Burada istənilən funksiya yazıla bilər

n = 100
a = float(input())
b = float(input())

x = a
h = (b - a) / n
s = (f(a) + f(b)) / 2

for i in range(1, n):
    x = x + h
    s = s + f(x)

s = s * h

print(f"İnteqral S = {s:20.10f}")
