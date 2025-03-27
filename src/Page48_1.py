n = 5
y = []

x = float(input())
x0 = float(input())
h = float(input())

for i in range(n + 1):
    y.append(float(input()))

f = y[0]
p = 1
n1 = n
q = (x - x0) / h

for i in range(1, n + 1):
    p = p * (q - i + 1) / i
    n1 -= 1
    for j in range(n1 + 1):
        a = y[j + 1] - y[j]
        y[j] = a
    f = f + p * y[0]

print(f"x = {x:10.6f}   N({x}) = {f:20.10f}")
