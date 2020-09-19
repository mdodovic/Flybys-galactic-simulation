import numpy as np
import matplotlib.pyplot as plt

M,X,Y,Z,VX,VY,VZ = np.loadtxt('gala.txt', unpack = True)

max_x=max(X)
max_y=max(Y)
R=[]
for i in range(len(X)):
    R.append(X[i]**2+Y[i]**2)**0.5
print(R)
        