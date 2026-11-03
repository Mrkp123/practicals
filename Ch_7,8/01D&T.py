
from datetime import datetime, timedelta
import math
import random

# ==============================
# Q1. DATE AND TIME
# ==============================

# 1. Check leap year
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


years = [1800, 2012, 2025, 2400, 2028]

for year in years:
    print(year, is_leap_year(year))


# 2. Find day of the week
def day_of_week(text):
    date = datetime.strptime(text, "%Y-%m-%d")
    return date.strftime("%A")


dates = ['2026-02-14', '2026-08-15', '2027-01-26']

for date in dates:
    print(date, day_of_week(date))


# 3. Number of days between two dates
date1 = datetime(2026, 2, 1)
date2 = datetime(2026, 11, 30)

difference = date2 - date1
print(difference.days)


# 4. Date and time formatting
now = datetime(2026, 7, 19, 9, 5, 30)

print(
    now.strftime("%d-%m-%Y"),
    now.strftime("%m/%d/%Y")
)

print(
    now.strftime("%H:%M:%S"),
    now.strftime("%I:%M:%S %p")
)


# 5. Add weeks, days and hours
new_time = now + timedelta(weeks=3, days=2, hours=7)

print(new_time.strftime("%Y-%m-%d %H:%M:%S"))


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
