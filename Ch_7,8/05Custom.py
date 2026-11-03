
# Custom module: scoretools.py

PASS_MARK = 40


# Calculate average marks
def average(marks):
    return round(sum(marks) / len(marks), 1)


# Calculate grade
def grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= PASS_MARK:
        return "C"
    else:
        return "F"


# Main guard
if __name__ == "__main__":
    print("Testing scoretools directly")
    print(average([70, 80, 90]), grade(82))
