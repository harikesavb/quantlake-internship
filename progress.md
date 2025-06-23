### **✅ Week 1:**

### 🛠 Day 1:Onboarding and Environment Setup
---

**Environment Chosen:**
- Google Colab (easy setup and runs in browser)

**Installed or Configured:**
- No installations needed with Colab
- Linked Google Drive for file storage

**What I Learned:**
- Basics of Python variables and data types
- How to use lists, tuples, and dictionaries
- Practiced arithmetic and comparison operators
- Used if-else conditions and loops

**Questions:**
- Need more clarity on when to use tuples vs lists
- Want to explore real-world use cases for dictionaries

  


### 🛠 Day 2:Python Fundamentals
---

**Environment Chosen:**

- Google Colab

**Installed:**

- Continued using previous setup

**What I Learned:**

- Writing custom functions (factorial, prime checker)

- How recursion works in Python

- Using built-in modules: math, random, datetime

- try-except-finally for handling runtime errors

- Validating input and preventing crashes

- Solving beginner-level problems (FizzBuzz, reverse string, max finder)

- Practicing Git workflow with commit and push

**Questions:**

- Initially forgot to return base case for recursion in factorial

- Needed to revisit string slicing for reversing

- Forgot to handle ValueError when input is not an integer

**Concepts Practiced:**

- User-defined functions and recursion

- Built-in modules like math, random, datetime

- Exception handling (try, except, finally)

- Problem solving with logic and conditions


**Logic Errors Solved:**

- Fixed a logic error in the prime number loop condition

- Replaced random.random() with random.randint() for integer generation

- Caught ZeroDivisionError with exception handling

- Handled invalid user input using try-except

- Debugged logic in FizzBuzz using modulo conditions

**Easiest vs Hardest:**

- Easiest: Using built-in modules and writing FizzBuzz

- Hardest: Debugging recursive functions, handling input errors, and deep exception tracing

### 🛠 Day 3 – Python + Pandas Introduction
---

**📂 Dataset Used:**  
- `tested.csv` (Titanic dataset)

**Features Explored:**

- Created Series and DataFrame from scratch

- Inspected data with .head(), .tail(), .shape, .columns, .dtypes

- Loaded data using pd.read_csv()

- Used .info(), .describe(), .isnull().sum() for exploration

- Accessed data using df['col'], df[['col1','col2']], df.loc[], df.iloc[]

- Added a new column (family_size = SibSp + Parch)

- Dropped a column (Cabin) and a row (index 0)

- Used .sort_values(), .value_counts(), .unique()

- Calculated summary stats with .mean(), .sum(), .min(), .max()

**Key Learnings & Observations:**
- `value_counts()` is great for analyzing categorical features like `Sex`
- `df.loc[]` (label-based) vs `df.iloc[]` (position-based) clarified
- Pandas arithmetic makes creating new columns easy
- `isnull().sum()` quickly reveals missing values
- `describe()` gives powerful statistical summaries with one line

** Bugs or Blockers:**
- No major blockers; clarified confusion between `.loc[]` and `.iloc[]` with examples

### 🛠 Day 4 – Pandas: Data Manipulation I
---

**📂 Dataset Used:**
- Netflix Titles dataset (`netflix_titles.csv`)

**Indexing & Slicing**
- Used `df.loc[]` and `df.iloc[]` to:
  - Access full rows and specific columns
  - Extract rows using conditional logic (e.g., TV Shows released after 2018)

**Filtering & Sorting**
- Applied filters like:
  - Movies released before 2010
  - TV Shows or shows from India
- Sorted records by:
  - `release_year` (descending)
  - Combination of `country` + `release_year`

**Handling Missing Data**
- Detected null values with `df.isnull().sum()`
- Dropped missing data rows using `df.dropna()`
- Replaced missing values using:
  - `df['country'].fillna('Unknown')`
  - `df['director'].fillna('Not Provided')`

**GroupBy Operations**
- Grouped by `type` to compute average `release_year`
- Grouped by `country` and aggregated:
  - `count` of titles
  - `min`, `max`, and `mean` of `release_year`

**🔗 Merging DataFrames**
- Created a second table with `show_id` and `origin_platform`
- Performed:
  - `INNER JOIN` to match Netflix titles
  - `LEFT JOIN` to keep all Netflix titles with platform info
  - `OUTER JOIN` to retain unmatched records from both


**What I Learned**
- Learned when to use `loc[]` vs `iloc[]`
- Practiced data cleaning techniques for missing data
- Strengthened understanding of `groupby()` and `merge()` operations
- Understood differences between `inner`, `left`, and `outer` joins






