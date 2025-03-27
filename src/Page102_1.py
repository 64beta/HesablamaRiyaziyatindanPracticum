def f(x, y):
    return x + y  # Burada istənilən funksiya yazıla bilər

a = float(input())
b = float(input())
y = float(input())
h = float(input())

x = a
while x <= b:
    k1 = h * f(x, y)
    k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
    k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
    k4 = h * f(x + h, y + k3)

    y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    print(f"x = {x:5.3f}   y = {y:10.6f}")
    x = x + h
