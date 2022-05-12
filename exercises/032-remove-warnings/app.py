import numpy as np 

defaults = np.seterr(all="ignore")
vector = np.ones(1) / 0
print(vector)