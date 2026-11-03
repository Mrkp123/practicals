
# ==============================
# Q2. MATH AND RANDOM MODULES
# ==============================

# 1. Number of buses required
passengers = 83
capacity = 12

buses = math.ceil(passengers / capacity)
print(buses)


# 2. Convert seconds into hours, minutes and seconds
total_seconds = 5461

hours = total_seconds // 3600
remaining = total_seconds % 3600

minutes = remaining // 60
seconds = remaining % 60

print(hours, minutes, seconds)


# 3. Simplify a fraction
def simplify(n, d):
    gcd = math.gcd(n, d)
    return (n // gcd, d // gcd)


print(simplify(45, 60))


# 4. Calculate tower height
dist = 80
angle = 45

height = dist * math.tan(math.radians(angle))

print(round(height, 2))


# 5. Generate random dice rolls
random.seed(5)

rolls = []

for i in range(5):
    rolls.append(random.randint(1, 6))

print(rolls, sum(rolls))


# 6. Shuffle deck and choose random option
deck = list(range(1, 9))

random.shuffle(deck)
print(deck)

print(random.choice(["rock", "paper", "scissors"]))
