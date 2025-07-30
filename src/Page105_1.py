import math
def f(x, y):
    return x + math.cos(y / math.sqrt(11))  # funksiyanı burada dəyiş

a = float(input())
b = float(input())
y = float(input())
h = float(input())

x = a
n = int((b - a) / h)

for i in range(1, n + 1):
    y = y + h * f(x, y)
    x = x + h
    print(f"{i} x = {x:5.3f} y = {y:20.10f}")
