import numpy as np #Complaex Mathematical Calculations.
import pandas as pd #Data Manipulation and Analysis.
from sklearn.linear_model import LinearRegression
from MachineLearning.Data.DataRegression import Data # Data for Regression.
import MachineLearning.Model.InsuranceModel as m
#print(m)
#print(dir(m))

df=pd.read_csv("MachineLearning/Data/insurance.csv")
y = df["Premium"]
x = df[["Age"]]  # 2D feature input for sklearn [] to make it a 2D array.

model123 = LinearRegression()
model123.fit(x, y)

test_data=pd.DataFrame({"Age":[32,33,35]})
  
test_data["PredictedPremium"] = model123.predict(test_data)

print(test_data)