import numpy as np

matrix = np.ones((5,5))
matrix[1:-1, 1:-1] = 0
print(matrix)