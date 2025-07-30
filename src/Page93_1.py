n = 4
eps = 1e-10

a = []
b = []
for _ in range(n):
    row = list(map(float, input().split()))
    a.append(row[:-1])
    b.append(row[-1])

x = [b[i] / a[i][i] for i in range(n)]

while True:
    k = 0
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i][j] * x[j]
        new_xi = (b[i] - s) / a[i][i]
        if abs(x[i] - new_xi) >= eps:
            k = 1
        x[i] = new_xi
    if k == 0:
        break

for i in range(n):
    print(f"x{i+1} = {x[i]}")
