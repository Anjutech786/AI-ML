import numpy as np

arr1=np.array([1,2,3,4,5])

arr2=np.array([[1,2,3],[4,5,6]])

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a + b)

print("add 10:",arr1+10)
print("Multiply by 2:",arr1*2)
print("Square:",arr1**2)
print("add 10:",arr2+10)

arr = np.array([10, 20, 30])

print(arr.mean())
print(arr.sum())
print(arr.max())

# 4. Random data generation

# Useful for testing and ML:
np.random.rand(5)

#5. Linear algebra
np.dot(a, b)