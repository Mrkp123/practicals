
import numpy as np

# 1. Create array using arange
a = np.arange(5, 56, 5)
print(a)


# 2. Create zeros and ones arrays
zeros = np.zeros((2, 6))
ones = np.ones((3, 3), dtype=float)

print(zeros.shape, ones.shape, np.sum(ones))


# 3. Identity matrix multiplied by 6
print(np.eye(3) * 6)


# 4. Create array using linspace
lin = np.linspace(0, 10, 50)

print(
    len(lin),
    round(float(lin[1]), 4),
    float(lin[-1])
)


# 5. Random array and slicing
np.random.seed(3)

r = np.random.randint(1, 21, size=(4, 4))

print(r)


# Replace first row with 100
r[0, :] = 100

print(r[0, :])


# Print bottom-right 2 x 2 block
print(r[-2:, -2:])
