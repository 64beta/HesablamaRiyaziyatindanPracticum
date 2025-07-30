n = 4
x = [0.0] * (n + 1)
y = [0.0] * (n + 1)
dy = [0.0] * (n + 1)

for i in range(n + 1):
    x[i], y[i] = map(float, input().split())

h = x[1] - x[0]  # düyünlər müntəzəm yerləşdiyi üçün h sabitdir

dy[0] = (-25*y[0] + 48*y[1] - 36*y[2] + 16*y[3] - 3*y[4]) / (12*h)
dy[1] = (-3*y[0] - 10*y[1] + 18*y[2] - 6*y[3] + y[4]) / (12*h)
dy[2] = (y[0] - 8*y[1] + 8*y[3] - y[4]) / (12*h)
dy[3] = (-y[0] + 6*y[1] - 18*y[2] + 10*y[3] + 3*y[4]) / (12*h)
dy[4] = (3*y[0] - 16*y[1] + 36*y[2] - 48*y[3] + 25*y[4]) / (12*h)

print("\nƏdədi diferensiallama nəticələri:")
for i in range(n + 1):
    print(f"y'({x[i]:.3f}) = {dy[i]:.10f}")
