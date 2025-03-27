n = 2

a = [[0 for j in range(n + 1)] for i in range(n)]

for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input(f"a[{i + 1}][{j + 1}] = "))

D = a[0][0] * a[1][1] - a[1][0] * a[0][1]

if D == 0:
    print("Tənliyin sonsuz həlli var")
else:
    Dx = a[0][2] * a[1][1] - a[1][2] * a[0][1]
    Dy = a[0][0] * a[1][2] - a[1][0] * a[0][2]

    x = Dx / D
    y = Dy / D

    print("x =", x)
    print("y =", y)
