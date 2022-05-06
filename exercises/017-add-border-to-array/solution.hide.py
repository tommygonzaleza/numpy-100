import numpy as np

matrix = np.ones((5,5))
matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values=0)
print(matrix)