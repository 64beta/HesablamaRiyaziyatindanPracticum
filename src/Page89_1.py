n = 4
eps = 10e-11

a = []
b = []
for _ in range(n):
    row = list(map(float, input().split()))
    a.append(row[:-1])
    b.append(row[-1])

x = [0.0] * n
z = [b[i] / a[i][i] for i in range(n)]

while True:
    k = 0
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i][j] * z[j]
        x[i] = (b[i] - s) / a[i][i]
    for i in range(n):
        if abs(z[i] - x[i]) >= eps:
            k = 1
        z[i] = x[i]
    if k == 0:
        break

for i in range(n):
    print(f"x{i+1} = {x[i]}")
