import numpy as np
import pylab 
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
T,Rmax=np.loadtxt('C:/Users/matij/Desktop/M31_direktna_blizu/txt/rezultati/rotacione_krive/Rmax.txt',unpack=True)
plt.plot(T,Rmax)
plt.xlabel('R [kpc]')
plt.ylabel('T [Gyr]') 
plt.show