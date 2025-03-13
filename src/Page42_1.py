x = float(input("x-in qiymətini daxil et: "))
n = int(input("n-in qiymətini daxil et: "))

A = []
print("Əmsalları daxil et:")
for i in range(n + 1):
    A.append(float(input(f"A[{i}] = ")))

P = A[0]
for i in range(1, n + 1):
    P = P * x + A[i]

print(f"p({x:10.5f}) = {P:20.10f}")
