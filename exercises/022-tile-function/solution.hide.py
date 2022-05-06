import numpy as np 

checkerboard_array = np.array([[0,1],[1,0]])
matrix = np.tile( checkerboard_array, (4,4))
print(matrix)