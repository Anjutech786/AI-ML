import numpy as np #Complaex Mathematical Calculations.
import pandas as pd #Data Manipulation and Analysis.
from sklearn.linear_model import LinearRegression
from MachineLearning.Data.DataRegression import Data # Data for Regression.
#import MachineLearning.Model.InsuranceModel as m
#print(m)
#print(dir(m))
df = pd.DataFrame([(d.Age, d.Premium) for d in 
                   Data.GetLinearInsuranceData()], 
                   columns=["Age", "Premium"])
y = df["Premium"]
x = df[["Age"]]  # 2D feature input for sklearn [] to make it a 2D array.

modelx = LinearRegression()
modelx.fit(x, y)

age = float(input("Enter age: "))
agedf=pd.DataFrame({"Age":[age]})
predict = modelx.predict(agedf)
print(predict[0])