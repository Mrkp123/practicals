# Python Units 7 & 8 – Lab Practical Exam

## Overview
This repository contains solutions for the Python Units 7 & 8 Lab Practical Examination. It demonstrates the use of Python standard libraries, file and directory operations, custom modules, packages, NumPy, and Pandas.

## Topics Covered

### Unit 7: Python Modules and Packages

**Q1–Q3: Standard Python Modules**
- `datetime` – Date and time operations
- `math` – Mathematical calculations
- `random` – Random number generation
- `uuid` – Unique identifier generation
- `time` – Timestamp and performance measurement

**Q4: OS and File Operations**
- Create, list, rename, move, and delete files and folders
- Read and write file contents
- Use `os` and `shutil` modules

**Q5: Custom Modules**
- Create and import user-defined modules
- Use functions and constants from modules
- Understand `__name__` and `if __name__ == "__main__"`

**Q6: Python Packages**
- Create packages using `__init__.py`
- Import modules from packages and subpackages
- Organize Python code into multiple files

### Unit 8: NumPy and Pandas

**Q7–Q10: NumPy**
- Create and access NumPy arrays
- Array indexing and slicing
- Boolean indexing and filtering
- Array arithmetic and statistical operations
- Reshaping and broadcasting
- Splitting and combining arrays

**Q11–Q15: Pandas**
- Create Series and DataFrames
- Read CSV files
- Detect and remove duplicate records
- Handle missing values
- Convert data types and date columns
- Create new columns and filter records
- Apply functions and categorical data
- Sort and group data
- Create pivot tables
- Merge DataFrames
- Set and reset indexes
- Read and write JSON files

## Project Files

| File / Folder | Description |
|---|---|
| `A_standard_modules.py` | Standard Python module programs (Q1–Q3) |
| `B_os_demo.py` | OS and file handling operations (Q4) |
| `scoretools.py` | Custom module (Q5) |
| `B_main_module.py` | Main program for custom module (Q5) |
| `textkit/` | Custom Python package and subpackage (Q6) |
| `B_main_package.py` | Main program for package imports (Q6) |
| `C_numpy_tasks.py` | NumPy practical programs (Q7–Q10) |
| `D_pandas_tasks.py` | Pandas practical programs (Q11–Q15) |
| `students.csv` | Student dataset for Pandas operations |
| `mentors.csv` | Course mentor dataset for merge operations |
| `names.json` | JSON output generated in Q15 |

## Requirements

- Python 3.x
- Pandas
- NumPy
- Matplotlib (if required by the standard module exercises)

## Installation

Install the required libraries using:

```bash
pip install numpy pandas matplotlib
```

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code, PyCharm, or Jupyter Notebook.
3. Make sure the CSV files are in the same folder as `D_pandas_tasks.py`.
4. Run the required Python file.

Example:

```bash
python A_standard_modules.py
python B_os_demo.py
python B_main_module.py
python B_main_package.py
python C_numpy_tasks.py
python D_pandas_tasks.py
```

## Dataset Information

### students.csv
Contains student information such as:
- StudentID
- Name
- Course
- City
- AdmitDate
- Fees
- Scholarship

### mentors.csv
Contains course and mentor information:
- Course
- Mentor

These datasets are used for data cleaning, filtering, grouping, merging, and other Pandas operations.

## Learning Outcomes

After completing these practical exercises, students will be able to:

- Use Python's built-in modules.
- Perform file and directory operations.
- Create and import custom modules and packages.
- Work with NumPy arrays and mathematical operations.
- Manipulate and analyze tabular data using Pandas.
- Handle missing and duplicate data.
- Perform grouping, sorting, filtering, and merging.
- Import and export CSV and JSON files.

## Conclusion

This practical examination demonstrates essential Python programming skills, including modular programming, file handling, numerical computing, and data analysis using NumPy and Pandas.
