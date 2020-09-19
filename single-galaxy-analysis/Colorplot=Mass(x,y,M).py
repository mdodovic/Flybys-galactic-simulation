## OVO RADI U POTPUNOSTI!!!
import numpy as np
import pylab 
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
import matplotlib.pyplot as plt

def func(xl,xd,yl,yd):
    mmm=0
    for i in range(n):
        if xl <= arx[i] and arx[i]<xd and yl<=ary[i] and ary[i]<yd:
            mmm +=arm[i] 
    
    """    
        if mmm != 0:
            return np.log10(mmm)
        else:
            return 0
    """
    return mmm
arx=[]
ary=[]
arz=[]
arm=[]



ime_in= "C:/Users/matij/Desktop/Patuljak_direktna/txt/DBHSB2/"
sn_out='C:/Users/matij/Desktop/Patuljak_direktna/txt/rezultati/bin/squ/'

kartd="disk_"    
#sn_dbxz="dbxz_"
sn_xy="xy_"
snmin_xy="xy_rez_"
snumin_xy="xy_urez_"
#sn_xz="xz_"
#sn_yz="yz_"

N=100
poc= 0
kr=N+1
#############

for k in range(poc,kr):
    
    if k<=9:
        deo = "00"
    if k<=99 and k>=10:
        deo = "0"
    if k>=100:
        deo = ""
        
    diskkart = ime_in + kartd + deo + str(k) + ".txt"        
    M,X,Y,Z,VX,VY,VZ= np.loadtxt(diskkart, unpack=True)#ovde ubacujes disk
    
    N=len(M)
    
    #######################################
    limit = 20 #8.666666666666667

    for i in range(N):
        if -limit < X[i] and X[i] < limit and -limit < Y[i] and Y[i] < limit:
            arx.append(X[i])
            ary.append(Y[i])
            arz.append(Z[i])
            arm.append(M[i])
                
    n=len(arx)        
    
    # define the grid over which the function should be plotted (xx and yy are matrices)
    xx, yy = pylab.meshgrid(
        pylab.linspace(-limit,limit, 100),
        pylab.linspace(-limit,limit, 100))
    zz = pylab.zeros(xx.shape) #popunjava matricu nulama dimenzija [xx.shape] sto su oni 3. brojevi gore kod pylab
    
    for i in range(0,xx.shape[0]-1):
        for j in range(0,xx.shape[1]-1):        
            zz[i,j] = func(xx[i,j], xx[i,j+1], yy[i,j], yy[i+1,j])/1e7
    pylab.pcolor(xx,yy,zz,cmap='inferno')
    plt.xlabel("X[kpc]", color='black')#  , fontsize=13)
    plt.ylabel("Y[kpc]", color='black')#  , fontsize=13)
    plt.xlim(-limit,limit)
    plt.ylim(-limit,limit)
    cb = plt.colorbar()
    cb.set_label('M [10^7 Msol]')
    plt.title("T = " + str(k/10*0.5) + ' Gyr')
    plt.text(-19,17,"T = " + str(k/10*0.5) + ' Gyr',fontsize=13, color='red', style = 'oblique')
    plt.savefig(sn_out + '_20_' + 'disk_' + deo + str(k) + '.jpg')
    pylab.show()
    
    arx[:]=[]
    ary[:]=[]
    arz[:]=[]
    arm[:]=[]
    
    ###################################
    limit = 10
    
    for i in range(N):
        if -limit < X[i] and X[i] < limit and -limit < Y[i] and Y[i] < limit:
            arx.append(X[i])
            ary.append(Y[i])
            arz.append(Z[i])
            arm.append(M[i])
                
    n=len(arx)        
    
    # define the grid over which the function should be plotted (xx and yy are matrices)
    xx, yy = pylab.meshgrid(
        pylab.linspace(-limit,limit, 100),
        pylab.linspace(-limit,limit, 100))
    zz = pylab.zeros(xx.shape) #popunjava matricu nulama dimenzija [xx.shape] sto su oni 3. brojevi gore kod pylab
    
    for i in range(0,xx.shape[0]-1):
        for j in range(0,xx.shape[1]-1):        
            zz[i,j] = func(xx[i,j], xx[i,j+1], yy[i,j], yy[i+1,j])/1e6
    pylab.pcolor(xx,yy,zz,cmap='inferno')
    plt.xlabel("X[kpc]", color='black')#  , fontsize=13)
    plt.ylabel("Y[kpc]", color='black')#  , fontsize=13)
    plt.xlim(-limit,limit)
    plt.ylim(-limit,limit)
    cb = plt.colorbar()
    #cb.set_label('log10(M)')
    cb.set_label('M [10^6 Msol]')
    plt.title("T = " + str(k/10*0.5) + ' Gyr')
    plt.text(-9,8,"T = " + str(k/10*0.5) + ' Gyr',fontsize=15, color='red', style = 'oblique')
    plt.savefig(sn_out + '_10_' + 'disk_' + deo + str(k) + '.jpg')
    pylab.show()
    
    arx[:]=[]
    ary[:]=[]
    arz[:]=[]
    arm[:]=[]
    
    
    #####################################################
    
    limit = 30
    
    for i in range(N):
        if -limit < X[i] and X[i] < limit and -limit < Y[i] and Y[i] < limit:
            arx.append(X[i])
            ary.append(Y[i])
            arz.append(Z[i])
            arm.append(M[i])
                
    n=len(arx)        
    
    # define the grid over which the function should be plotted (xx and yy are matrices)
    xx, yy = pylab.meshgrid(
        pylab.linspace(-limit,limit, 100),
        pylab.linspace(-limit,limit, 100))
    zz = pylab.zeros(xx.shape) #popunjava matricu nulama dimenzija [xx.shape] sto su oni 3. brojevi gore kod pylab
    
    for i in range(0,xx.shape[0]-1):
        for j in range(0,xx.shape[1]-1):        
            zz[i,j] = func(xx[i,j], xx[i,j+1], yy[i,j], yy[i+1,j])/1e7
    pylab.pcolor(xx,yy,zz,cmap='inferno')
    plt.xlabel("X[kpc]", color='black')#  , fontsize=13)
    plt.ylabel("Y[kpc]", color='black')#  , fontsize=13)
    plt.xlim(-limit,limit)
    plt.ylim(-limit,limit)
    cb = plt.colorbar()
    #cb.set_label('log10(M)')
    cb.set_label('M [10^7 Msol]')
    plt.title("T = " + str(k/10*0.5) + ' Gyr')
    plt.text(-29,25,"T = " + str(k/10*0.5) + ' Gyr',fontsize=15, color='red', style = 'oblique')
    plt.savefig(sn_out + 'disk_' + deo + str(k) + '.jpg')
    pylab.show()
    
    arx[:]=[]
    ary[:]=[]
    arz[:]=[]
    arm[:]=[]
    
print('END')