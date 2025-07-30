n = 4
a = [list(map(float, input().split())) for _ in range(n)]

for i in range(n):
    if a[i][i] == 0:
        for m in range(i + 1, n):
            if a[m][i] != 0:
                a[i], a[m] = a[m], a[i]
                break

    v = a[i][i]
    for j in range(n + 1):
        a[i][j] /= v

    for k in range(i + 1, n):
        v = a[k][i]
        for j in range(i + 1, n + 1):
            a[k][j] -= v * a[i][j]

x = [0] * n
x[n - 1] = a[n - 1][n]
for i in range(n - 2, -1, -1):
    x[i] = a[i][n]
    for j in range(i + 1, n):
        x[i] -= a[i][j] * x[j]

for i in range(n):
    print(f"x{i+1} = {x[i]:.5f}")
