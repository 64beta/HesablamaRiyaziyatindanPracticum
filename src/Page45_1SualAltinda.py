#kitabda kod ve sekil uyusmur

n = 5

x = []
y = []

for i in range(n + 1):
    xi = float(input(f"X[{i}] = "))
    yi = float(input(f"Y[{i}] = "))
    x.append(xi)
    y.append(yi)

d = float(input())

f = 0.0
for j in range(n + 1):
    l = 1.0
    for i in range(1,n + 1):
        if i != j:
            c = x[j] - x[i]
            l *= (d - x[i]) / c
    f += l * y[j]

print(f"x = {d:7.5f}   L({d}) = {f:10.6f}")
