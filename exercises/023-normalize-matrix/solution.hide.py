import numpy as np 

matrix = np.random.random((5,5))
matrix = (matrix - np.mean (matrix)) / (np.std(matrix))
print(Z - np.mean (matrix))