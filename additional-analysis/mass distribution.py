## OVO RADI U POTPUNOSTI!!!
import numpy as np
import pylab 
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
import matplotlib.pyplot as plt
NIZM,NIZX,NIZY,NIZZ,NIZVX,NIZVY,NIZVZ= np.loadtxt("C:/Users/matij/Desktop/Galaksije/M31_txt/Nerasejano/disk_000.txt", unpack=True)
arx=[]
ary=[]
arz=[]
arm=[]
N=len(NIZM)
limit=15
for i in range(N):
    if limit > (NIZX[i]**2 + NIZY[i]**2)**0.5:
        arx.append(NIZX[i])
        ary.append(NIZY[i])
        arz.append(NIZZ[i])
        arm.append(NIZM[i])
        

n=len(arx)        

# the function to be plotted
def func(xl,xd,yl,yd):
    mmm=0
    for i in range(n):
        if xl <= arx[i] and arx[i]<xd and yl<=ary[i] and ary[i]<yd:
            mmm +=arm[i] 
    
    # gives vertical color bars if x is horizontal axis
    return mmm



# define the grid over which the function should be plotted (xx and yy are matrices)
xx, yy = pylab.meshgrid(
    pylab.linspace(-limit,limit, 10),
    pylab.linspace(-limit,limit, 10))

#print(xx[0,0])
#print(xx[1,0])
#print(xx[0,1])
#print(xx[1,1])

#print(yy[0,0])
#print(yy[1,0])
#print(yy[0,1])
#print(yy[1,1])

#print(xx.shape[0])
#print(xx.shape[1])

#print(xx)

# indexing of xx and yy (with the default value for the
# 'indexing' parameter of meshgrid(..) ) is as follows:
#
#   first index  (row index)    is y coordinate index
#   second index (column index) is x coordinate index
#
# as required by pcolor(..)

# fill a matrix with the function values
zz = pylab.zeros(xx.shape) #popunjava matricu nulama dimenzija [xx.shape] sto su oni 3. brojevi gore kod pylab
#print(xx.shape)
#print(zz)

for i in range(0,xx.shape[0]-1):
    for j in range(0,xx.shape[1]-1):        
        zz[i,j] = func(xx[i,j], xx[i,j+1], yy[i,j], yy[i+1,j])
    print(i/(xx.shape[0]-1)*100)

# plot the calculated function values
pylab.pcolor(xx,yy,zz)

# and a color bar to show the correspondence between function value and color
pylab.colorbar()

pylab.show()
