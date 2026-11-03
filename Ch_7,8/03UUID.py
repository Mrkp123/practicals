
# ==============================
# Q3. UUID AND TIME MODULES
# ==============================

import uuid
import time
from datetime import timezone


# 1. Generate UUID5 for names
names = ['Neha', 'Imran', 'Dev', 'Sana']

ids = {}

for name in names:
    ids[name] = uuid.uuid5(
        uuid.NAMESPACE_DNS,
        name.lower() + ".example"
    )

for name, uid in ids.items():
    print(name, str(uid)[:8])

print(len(set(ids.values())) == len(ids.values()))


# 2. Create UUID3 and UUID5
uuid3 = uuid.uuid3(uuid.NAMESPACE_DNS, "example.com")
uuid5 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")

print(uuid3 != uuid5, uuid3.version, uuid5.version)


# 3. Working with timestamps
ts = 1000000000

# Convert timestamp using gmtime and strftime
utc_time = time.gmtime(ts)

print(time.strftime("%Y-%m-%d %H:%M:%S", utc_time))

# Display using asctime
print(time.asctime(time.gmtime(ts)))

# Convert timestamp into datetime
dt = datetime.fromtimestamp(ts, timezone.utc)

print(dt.strftime("%d %b %Y"))


# 4. Measure execution time
start = time.perf_counter()

total = sum(range(1_000_000))

end = time.perf_counter()

elapsed = end - start

print(total, type(elapsed).__name__, elapsed >= 0)
