Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> # Step 1: Create dictionary
>>> data = {
...     'Name': ['Asha', 'Ravi', 'Kiran', 'Meena'],
...     'Marks': [85, 90, 78, 92]
... }
>>> # Step 2: Create DataFrame
... df = pd.DataFrame(data)
>>> # Step 3: Display DataFrame
... print("Original DataFrame:")
Original DataFrame:
>>> print(df)
    Name  Marks
0   Asha     85
1   Ravi     90
2  Kiran     78
3  Meena     92
>>> # Step 4: Add new column (calculated values)
... df['Percentage'] = df['Marks'] * 1.0
>>> # Step 5: Display updated DataFrame
... print("\nUpdated DataFrame:")

Updated DataFrame:
>>> print(df)
    Name  Marks  Percentage
0   Asha     85        85.0
1   Ravi     90        90.0
2  Kiran     78        78.0
3  Meena     92        92.0
>>> 
>>> 
>>> data = {
...     'Product': ['Pen', 'Book', 'Pencil', 'Eraser'],
...     'Price': [10, 50, 5, 3],
...     'Quantity': [20, 10, 30, 15]
... }
>>> df = pd.DataFrame(data)
>>> print("Original DataFrame:")
Original DataFrame:
>>> print(df)
  Product  Price  Quantity
0     Pen     10        20
1    Book     50        10
2  Pencil      5        30
3  Eraser      3        15
# Add new column: Total Cost = Price * Quantity
df['Total Cost'] = df['Price'] * df['Quantity']
print("\nUpdated DataFrame:")

Updated DataFrame:
print(df)
  Product  Price  Quantity  Total Cost
0     Pen     10        20         200
1    Book     50        10         500
2  Pencil      5        30         150
3  Eraser      3        15          45



# Step 1: Load CSV file
df = pd.read_csv("C:/Users/Chandu/OneDrive/Desktop/11prog_3Salary_Data.csv")
print("Original DataFrame:")
Original DataFrame:
print(df)
    YearsExperience  Salary
0               1.1   39343
1               1.3   46205
2               1.5   37731
3               2.0   43525
4               2.2   39891
5               2.9   56642
6               3.0   60150
7               3.2   54445
8               3.2   64445
9               3.7   57189
10              3.9   63218
11              4.0   55794
12              4.0   56957
13              4.1   57081
14              4.5   61111
15              4.9   67938
16              5.1   66029
17              5.3   83088
18              5.9   81363
19              6.0   93940
20              6.8   91738
21              7.1   98273
22              7.9  101302
23              8.2  113812
24              8.7  109431
25              9.0  105582
26              9.5  116969
27              9.6  112635
28             10.3  122391
29             10.5  121872

# Step 2: Check missing values
print("\nMissing Values:")

Missing Values:
print(df.isnull().sum())
YearsExperience    0
Salary             0
dtype: int64

# Step 3: Fill missing values with mean (for numeric columns)
df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nDataFrame after filling missing values:")
print(df)
SyntaxError: multiple statements found while compiling a single statement

# Step 3: Fill missing values with mean (for numeric columns)
df.fillna(df.mean(numeric_only=True), inplace=True)
    YearsExperience  Salary
0               1.1   39343
1               1.3   46205
2               1.5   37731
3               2.0   43525
4               2.2   39891
5               2.9   56642
6               3.0   60150
7               3.2   54445
8               3.2   64445
9               3.7   57189
10              3.9   63218
11              4.0   55794
12              4.0   56957
13              4.1   57081
14              4.5   61111
15              4.9   67938
16              5.1   66029
17              5.3   83088
18              5.9   81363
19              6.0   93940
20              6.8   91738
21              7.1   98273
22              7.9  101302
23              8.2  113812
24              8.7  109431
25              9.0  105582
26              9.5  116969
27              9.6  112635
28             10.3  122391
29             10.5  121872
print("\nDataFrame after filling missing values:")

DataFrame after filling missing values:
print(df)
    YearsExperience  Salary
0               1.1   39343
1               1.3   46205
2               1.5   37731
3               2.0   43525
4               2.2   39891
5               2.9   56642
6               3.0   60150
7               3.2   54445
8               3.2   64445
9               3.7   57189
10              3.9   63218
11              4.0   55794
12              4.0   56957
13              4.1   57081
14              4.5   61111
15              4.9   67938
16              5.1   66029
17              5.3   83088
18              5.9   81363
19              6.0   93940
20              6.8   91738
21              7.1   98273
22              7.9  101302
23              8.2  113812
24              8.7  109431
25              9.0  105582
26              9.5  116969
27              9.6  112635
28             10.3  122391
29             10.5  121872
