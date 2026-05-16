import torch

scaler=torch.tensor(2.7)
print(scaler)
print(scaler.shape)

vector_1D = torch.tensor([1,2,3,4,5])
print(vector_1D)    
print(vector_1D.shape)
print(vector_1D.dtype)

matrix_2D = torch.tensor([[1,2],[3,4]])
print(matrix_2D)     
print(matrix_2D.shape)
print(matrix_2D.dtype)

matrix_3D = torch.tensor([[[1,2],[3,4]],[[5,6],[7,8]]])
print(matrix_3D)
print(matrix_3D.shape)
print(matrix_3D.dtype)

cube1=torch.ones((2,3,4))
print(cube1)
print(cube1.shape)
print(cube1.dtype)  