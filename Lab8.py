import pandas as pd

data={
    'name': ['Alice', 'Bob', 'Charlie','David','Eve'], 
    'age': [25, 30, 35, 40, 45],
    'salary': [50000, 60000, 70000, 80000, 90000]}
df=pd.DataFrame(data)
print("DataFrame:\n",df)
print("\nName:",df['name'])
print("\nAge:",df['age'])
print("\nSalary:",df['salary'])


print("\nFirst row:\n",df.iloc[0])
print("\nLast two rows:\n",df.iloc[-2:] )