
import os
import shutil

# 1. Create exam_data/logs folder
logs = os.path.join("exam_data", "logs")

os.makedirs(logs, exist_ok=True)
os.makedirs(logs, exist_ok=True)


# 2. Create three files
x_file = os.path.join(logs, "x.txt")
y_file = os.path.join(logs, "y.txt")
z_file = os.path.join(logs, "z.csv")

with open(x_file, "w") as f:
    f.write("one\ntwo\n")

with open(y_file, "w") as f:
    f.write("three\n")

with open(z_file, "w") as f:
    f.write("x,y\n1,2\n")


# 3. Print sorted .txt files
txt_files = sorted(
    file for file in os.listdir(logs)
    if file.endswith(".txt")
)

print(txt_files)


# 4. Read x.txt and print line count and first line
with open(x_file, "r") as f:
    lines = f.readlines()

print(len(lines), lines[0].strip())


# 5. Create archive and move x.txt
archive = os.path.join("exam_data", "archive")
os.makedirs(archive, exist_ok=True)

shutil.move(
    x_file,
    os.path.join(archive, "x.txt")
)

print(sorted(os.listdir(logs)), os.listdir(archive))


# 6. Rename y.txt to old_y.txt
old_y = os.path.join(logs, "old_y.txt")

os.rename(y_file, old_y)

print(
    os.path.exists(y_file),
    os.path.isfile(old_y)
)


# 7. Delete exam_data completely
shutil.rmtree("exam_data")

print(os.path.exists("exam_data"))
