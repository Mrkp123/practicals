
# ==============================
# Q9. ARRAY MATHS AND STATISTICS
# ==============================

# 1. Array arithmetic and matrix multiplication
A = np.arange(3, 12).reshape(3, 3)
B = np.arange(11, 20).reshape(3, 3)

print(A * B)

print(np.round(A / B, 2))

print(A @ B)


# 2. Calculate Z-score
arr = np.array([5, 15, 25, 35, 45], dtype=float)

mean = np.mean(arr)
std = np.std(arr)

z = (arr - mean) / std

print(
    np.round(z, 2),
    round(float(np.mean(z)), 6)
)


# 3. Euclidean distance
p = np.array([1, 2, 2])
q = np.array([4, 6, 14])

distance = np.sqrt(np.sum((p - q) ** 2))

print(float(distance))


# 4. Array statistics
v = np.array([8, 3, 19, 11, 6, 2])

print(
    np.argmax(v),
    np.argmin(v),
    np.max(v),
    np.min(v)
)

print(
    float(np.mean(v)),
    float(np.median(v)),
    round(float(np.var(v)), 2),
    round(float(np.std(v)), 2)
)


# 5. Sorting arrays
m = np.array([
    [9, 3, 1],
    [6, 8, 2],
    [5, 7, 4]
])

print(np.sort(m, axis=0))

print(np.sort(m, axis=1))


# 6. Count positive, negative and zero values
pn = np.array([4, -2, 0, 9, -6, 0, 3, -1])

positive = np.sum(pn > 0)
negative = np.sum(pn < 0)
zero = np.sum(pn == 0)

print(positive, negative, zero)
