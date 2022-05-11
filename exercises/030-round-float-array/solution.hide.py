import numpy as np 

vector = np.random.uniform(-10,+10,10)
vector = np.copysign(np.ceil(np.abs(vector)), vector)
print(vector)