import random
N = int(input("How many random points to generate: "))
inside = 0
for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside += 1
pi = 4 * inside / N
print("Approximation of pi:", pi)