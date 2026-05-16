import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Load CSV file
df = pd.read_csv("MachineLearning/Data/polynomial_insurance_testing_data.csv")

# Target variable (output)
y = df["Premium"]

# Feature variable (input)
x = df[["Age"]]

# Convert normal features into polynomial features
poly = PolynomialFeatures(degree=9, include_bias=False)

# Transform x into polynomial form
x_poly = poly.fit_transform(x)

# Create Linear Regression model
model123 = LinearRegression()

# Train model
model123.fit(x_poly, y)

# Predict using transformed data
predictedby = model123.predict(x_poly)

# New data for testing
test_data = pd.DataFrame({
    "Age": [32, 33, 35]
})

# Convert test data into polynomial form
test_poly = poly.transform(test_data)

# Predict premium
test_data["PredictedPremium"] = model123.predict(test_poly)

# Performance metrics
r2 = r2_score(y, predictedby)
mse = np.sqrt(mean_squared_error(y, predictedby))

# Print results
print(test_data)
predictedby = model123.predict(x_poly)
print("\nPredicted Premiums:", predictedby)
print("\nR2 Score:", r2)
print("Mean Squared Error:", mse)