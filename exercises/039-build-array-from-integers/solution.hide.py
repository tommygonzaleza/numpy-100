import numpy as np 

def generator():
    for i in range(10):
        yield i

vector = np.fromiter(generator(), int)
print(vector)