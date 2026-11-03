
# ==============================
# Q8. BOOLEAN MASKS, np.where AND VIEWS
# ==============================

# 1. Boolean masks using ages
ages = np.array([19, 42, 16, 28, 33, 15, 51])

# Ages 18 or more
print(ages[ages >= 18])

# Ages strictly between 25 and 45
print(ages[(ages > 25) & (ages < 45)])

# Ages not 18 or more
print(ages[~(ages >= 18)])


# 2. Using np.where()
scores = np.array([48, 91, 66, 73, 59, 85])

result = np.where(scores >= 70, "Pass", "Fail")

print(result)


# 3. Modify temperatures using Boolean mask
temps = np.array([31, 27, 36, 40, 29, 33])

mask = temps > 35

temps[mask] = 34

print(temps, int(mask.sum()))


# 4. Create 5x5 matrix and slicing
mat = np.arange(3, 28).reshape(5, 5)

print(mat[1:4, 2:5])


# 5. View vs Copy

# View
view = mat[0]

view[0] = 99

print(mat[0, 0])


# Copy
copy = mat[1].copy()

copy[0] = -1

print(mat[1, 0])

# A view shares memory with the original array, so changes
# affect mat. A copy has separate memory, so changes do not
# affect the original mat.
