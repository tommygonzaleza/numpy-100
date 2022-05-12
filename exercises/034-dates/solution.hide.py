import numpy as np 

yesterday = np.datetime64('today') - np.timedelta64(1)
print(yesterday)