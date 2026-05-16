
1. Check Python installation

Open terminal / command prompt:

python --version

Step 2: Install JupyterLab

Open Command Prompt:

pip install jupyterlab


Step 3: Launch it

For JupyterLab:

jupyter lab


Optional: Use virtual environment (recommended)
python -m venv myenv

Step 4: TO Make heavy calculation install Numpy.
c:/StudyPY/QuestpondPY/.venv/Scripts/python.exe -m pip install numpy
Note- NumPy is the core Python library for numerical computing.

If Pandas is for table-like data, NumPy is for arrays and math operations.
high-performance arrays
matrix operations
mathematical computations
foundation for AI/ML libraries

Many libraries like Pandas, TensorFlow, and PyTorch are built on NumPy-like arrays.

Why NumPy exists

Normal Python lists are slower for heavy calculations:

numbers = [1, 2, 3, 4]

NumPy arrays are optimized:

import numpy as np

arr = np.array([1, 2, 3, 4])



Step 5:  To install Pandas into your virtual environment
c:/StudyPY/QuestpondPY/.venv/Scripts/python.exe -m pip install pandas
Note- Pandas is a Python library used for working with structured data (tables, CSVs, Excel, SQL data).

Think of it like:

Excel in code
or SQL + Excel + data transformation inside Python (programming language)
import pandas as pd

df = pd.read_csv("employees.csv")
print(df)


