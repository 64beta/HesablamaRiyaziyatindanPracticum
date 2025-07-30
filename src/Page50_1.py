y = []

n = int(input())
x = float(input())
xn = float(input())
h = float(input())

for i in range(n + 1):
    y.append(float(input()))

f = y[n]
p = 1
n1 = n
q = (x - xn) / h

for i in range(1, n + 1):
    p = p * (q + i - 1) / i
    n1 -= 1
    for j in range(n1 + 1):
        a = y[j + 1] - y[j]
        y[j] = a
    f = f + p * y[n1]

print(f"x = {x:6.4f}   N(x) = {f:6.4f}")
