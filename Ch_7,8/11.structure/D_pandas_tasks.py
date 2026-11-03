
import pandas as pd

# 1. Create a Series
s = pd.Series(
    ["Student_1", "Student_2", "Student_3"],
    index=["a", "b", "c"]
)

print(s["b"], s.iloc[2], len(s))


# 2. Create a DataFrame from list of dictionaries
data = [
    {"item": "pen", "qty": 10},
    {"item": "book", "qty": 4},
    {"item": "bag", "qty": 2}
]

df_items = pd.DataFrame(data)

print(df_items)


# 3. Read CSV file
df = pd.read_csv("students.csv")

print(df.head(3))

print(df.shape, list(df.columns))


# 4. Check duplicate rows and missing values
print(df.duplicated().sum())

print(df.isnull().sum())



# Q12. Clean and convert

# 1. Remove duplicate rows
df = df.drop_duplicates()

# 2. Convert Scholarship to numeric and fill missing values with 0
df["Scholarship"] = pd.to_numeric(df["Scholarship"], errors="coerce")
df["Scholarship"] = df["Scholarship"].fillna(0).astype(int)

# 3. Fill missing Fees with rounded mean and convert to int
fill_value = int(round(df["Fees"].mean()))
df["Fees"] = df["Fees"].fillna(fill_value).astype(int)

# 4. Convert AdmitDate and create new columns
df["AdmitDate"] = pd.to_datetime(df["AdmitDate"])

df["Year"] = df["AdmitDate"].dt.year
df["Weekday"] = df["AdmitDate"].dt.day_name()

df["Years"] = (
    (pd.Timestamp("2026-01-01") - df["AdmitDate"]).dt.days // 365
)

# 5. Print results
print(fill_value, df.shape, df["Fees"].dtype, df["Scholarship"].dtype)

print(df[["StudentID", "Year", "Weekday", "Years"]].head(4))



# Q13. New column, filtering, indexing and categories

# 1. Add Payable column
df["Payable"] = df["Fees"] + df["Scholarship"]

# 2. Filter Data students whose Payable is greater than 40000
filtered = df[(df["Course"] == "Data") & (df["Payable"] > 40000)]

print(filtered[["StudentID", "Name", "Payable"]])

# 3. Series, DataFrame and indexing
print(type(df["Name"]).__name__, type(df[["Name"]]).__name__)
print(df.loc[0, "Name"], df.iloc[1, 1])

# 4. Create Band column
def band(n):
    if n >= 48000:
        return "High"
    elif n >= 35000:
        return "Mid"
    else:
        return "Low"

df["Band"] = df["Payable"].apply(band)

df["Band"] = pd.Categorical(
    df["Band"],
    categories=["Low", "Mid", "High"],
    ordered=True
)

# 5. Sort Band highest first, then StudentID ascending
sorted_df = df.sort_values(
    by=["Band", "StudentID"],
    ascending=[False, True]
)

print(sorted_df[["StudentID", "Band"]].head(3))

print(df["Band"].value_counts().sort_index())



# Q14. Grouping and pivot table

# 1. Group by Course and calculate mean, max and count of Fees
group_result = df.groupby("Course")["Fees"].agg(
    ["mean", "max", "count"]
)

group_result["mean"] = group_result["mean"].round(1)

group_result = group_result.sort_values(
    by="mean", ascending=False
)

print(group_result)

# 2. Calculate percentage of Fees within each Course group
group_total = df.groupby("Course")["Fees"].transform("sum")

df["PctOfGroup"] = (df["Fees"] / group_total * 100).round(1)

print(df[["StudentID", "Course", "PctOfGroup"]].head(4))

# 3. Create pivot table
pivot = pd.pivot_table(
    df,
    index="Course",
    columns="City",
    values="Fees",
    aggfunc="sum",
    fill_value=0
)

print(pivot)



# Q15. Merge, index and JSON

# 1. Read mentors.csv and perform a left merge
mentors = pd.read_csv("mentors.csv")

left_result = pd.merge(df, mentors, on="Course", how="left")

print(left_result["Mentor"].isnull().sum(), left_result.shape)

# 2. Inner and outer merge
inner_result = pd.merge(df, mentors, on="Course", how="inner")
outer_result = pd.merge(df, mentors, on="Course", how="outer")

print(len(inner_result), len(outer_result))

# 3. Set StudentID as index and find student 308
emp = df.set_index("StudentID")

print(emp.loc[308, "Name"])

# Reset index and rename Fees
emp = emp.reset_index()
emp = emp.rename(columns={"Fees": "Monthly Fees"})

print(list(emp.columns[:6]))

# 4. Save StudentID and Name to JSON
df[["StudentID", "Name"]].to_json("names.json", orient="records")

# Read JSON file
names = pd.read_json("names.json")

print(names.shape)

