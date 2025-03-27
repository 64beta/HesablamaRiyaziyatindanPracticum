n = 4

a = []
for i in range(n):
    row = []
    for j in range(n + 1):
        row.append(float(input(f"a[{i+1}][{j+1}] = ")))
    a.append(row)

for i in range(n):
    v = a[i][i]
    for j in range(n + 1):
        a[i][j] = a[i][j] / v
    for k in range(i + 1, n):
        v = a[k][i]
        for j in range(i + 1, n + 1):
            a[k][j] = a[k][j] - v * a[i][j]

x = [0] * n
x[n - 1] = a[n - 1][n]
for i in range(n - 2, -1, -1):
    x[i] = a[i][n]
    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]

for i in range(n):
    print(f"x{i+1} = {x[i]:10.4f}")

# 8.2 -3.2 14.2 14.8 -8.4
# 5.6 -12 15 -6.4 4.5
# 5.7 3.6 -12.4 -2.3 3.3
# 6.8 13.2 -6.3 -8.7 14.3
