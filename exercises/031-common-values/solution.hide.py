import numpy as np 

vector1 = np.arange(1, 10)
vector2 = np.arange(5, 15)
common_values = np.intersect1d(vector1,vector2)

print(common_values)