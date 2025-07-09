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


### 🛠 Day 5 – Pandas: Data Manipulation II

**Focus:** Reshaping, Transformation, and Combining DataFrames

---

**📂 Dataset Used:**
- Netflix Titles dataset (`superstore.csv`)

**Reshaping Methods Practiced:**
- `.pivot()` and `.pivot_table()` for summarizing data
- `.melt()` to unpivot wide tables back to long format

**Transformation Logic Implemented:**
- `.apply()` with custom functions to classify profit tiers and flag discounts
- `.map()` and `.replace()` for encoding and standardizing column values
- `pd.concat()` to combine data vertically and horizontally

**Any Struggles or Workarounds:**
- Encountered mismatched columns while concatenating (`axis=1`), resolved using `ignore_index=True`
- Took time to understand how `.melt()` reshapes the data and how `id_vars` and `value_vars` work
- Faced confusion between `.pivot()` and `.pivot_table()`—realized `.pivot_table()` is more flexible with aggregations like `sum`, `mean`
- Had to ensure no missing values before applying `.groupby()` and `.pivot()` to avoid NaN in results
- Created intermediate DataFrames to debug reshaping issues more clearly

**Key Takeaways:**
- Mastered reshaping data with `pivot`, `pivot_table`, and `melt`
- Used `.apply()` and lambda functions for powerful column transformations
- Applied `.map()` and `.replace()` to clean and recode data efficiently
- Gained confidence with concatenation using `pd.concat()` for flexible table joins
- Built a complete data pipeline from cleaning to dashboard summary using Pandas


### 🛠 Day 6 – Data Visualization

**Focus:** Data Visualization with Matplotlib and Seaborn

---

### ✅ Tasks Completed:

**Chart Types Learned:**
- Line Plot (`plt.plot`)
- Scatter Plot (`plt.scatter`)
- Histogram (`sns.histplot`)
- Boxplot (`sns.boxplot`)
- Heatmap (`sns.heatmap`)
- Bar Chart (`sns.barplot`)

**Data and Features Visualized:**
- Superstore dataset used throughout
- Visualized sales and profit trends over time
- Correlation between discount, sales, and profit
- Categorical comparison of profits by Sub-Category and Region
- Flagged outliers using boxplots and explored distributions with histograms

**Charts Saved as Image Files:**
- `daily_sales_line_plot.png`
- `sales_vs_profit_scatter.png`
- `publish_quality_monthly_sales.png`

**Most Proud of:**
- ✅ *Monthly Sales Trend – Publish-Quality Line Chart*
  - Applied color styling, font customization, DPI=300, and layout adjustments
  - Ready for inclusion in reports or dashboards
 

---

### 🗓️ Day 7 – SQL Fundamentals

**Focus:** SQL Fundamentals Using SQLite + Superstore Dataset

---

#### 🗃️ Database Used
- SQLite (in-memory)
- Dataset: `Superstore.csv` loaded into SQLite table `superstore`

---

#### 📌 5 Interesting SQL Queries I Wrote

1. **Filter sales greater than 100**
    ```sql
   SELECT * FROM superstore WHERE Sales > 100;
    
  **Filter by discount between 0.1 and 0.3**
      
    SELECT * FROM superstore WHERE Discount BETWEEN 0.1 AND 0.3;
  **Exclude California orders**
  
     SELECT * FROM superstore WHERE State != 'California';
  **Search product names containing “Chair**

      SELECT * FROM superstore WHERE [Product Name] LIKE '%Chair%';

  **Group sales by region**

      SELECT Region, COUNT(*) AS order_count, SUM(Sales) AS total_sales
      FROM superstore
      GROUP BY Region;




 
### 🛠 Day 8 – SQL Integration

**Focus:** SQL Integration with Pandas and Data Manipulation

---

### ✅ Tasks Completed

** Complex SQL Queries Used**
- Used `SELECT`, `WHERE`, `GROUP BY`, `COUNT()`, and `AVG()` to summarize regional sales
- Wrote subqueries in `WHERE` clauses to filter high-value customers
- Updated SQL records using `UPDATE` and removed invalid data using `DELETE`
- Merged customer and order tables using `pd.merge()` (simulating `INNER JOIN`)
- Retrieved SQL results into Pandas with `pd.read_sql_query()`

** SQL vs Pandas – What Worked Best?**
- **SQL:** Excellent for filtering and aggregation tasks
- **Pandas:** Ideal for post-query transformation and data chaining

** Favorite Integration Technique**
- `pd.read_sql_query()` to connect SQL with Pandas workflows
- `pd.merge()` for clean SQL-style joins inside Python

** Key Skills Practiced**
- SQL filtering, joins, and subqueries
- Data updates (`UPDATE`) and cleanup (`DELETE`) in SQLite
- Importing and analyzing SQL output in Pandas
- Merging datasets based on foreign keys

** Easiest vs Hardest**
- **Easiest:** Importing SQL results into Pandas
- **Hardest:** Troubleshooting subqueries and aligning merge keys

** Blockers or Questions**
- Column mismatches during merges (`Customer ID` vs `customer_id`)
- Needed to rename columns for smooth `pd.merge()` execution











