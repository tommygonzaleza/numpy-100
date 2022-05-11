import numpy as np 

vector = np.arange(11)
vector[(3 < vector) & (vector < 8)] *= -1
print(vector)