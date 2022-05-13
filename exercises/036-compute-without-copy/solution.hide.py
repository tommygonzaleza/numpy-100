import numpy as np 

A = np.ones(3)*1
B = np.ones(3)*2

result = (np.multiply(np.add(A,B,out=B),np.divide(np.negative(A,out=A),2,out=A),out=A))

print(result)