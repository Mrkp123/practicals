
# ==============================
# Q10. RESHAPE, BROADCASTING AND SPLITTING
# ==============================

# 1. Reshape and flatten
vals = np.arange(1, 16)

print(vals.reshape(5, -1).shape)

print(
    vals.reshape(3, 5).flatten().tolist() == vals.tolist()
)


# 2. Broadcasting
sales = np.array([
    [30, 10],
    [20, 40],
    [15, 25]
])

bonus = np.array([5, 1, 4])[:, np.newaxis]

print(sales + bonus)

# Multiply sales by rates
rates = np.array([0.2, 0.1])

print(np.round(sales * rates, 2))


# 3. Array splitting
arr = np.arange(1, 14 + 1)

try:
    parts = np.split(arr, 3)
except ValueError:
    print("ValueError")


# Split into nearly equal parts
parts = np.array_split(arr, 3)

print([part.tolist() for part in parts])
