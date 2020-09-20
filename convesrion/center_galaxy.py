import numpy as np
import pylab 
from numpy import exp,arange
from pylab import meshgrid,imshow,contour,clabel,colorbar,axis,title,show
import matplotlib.pyplot as plt
N=100
poc=0
kr=N+1
#############

ime_in= "C:/Users/matij/Desktop/M31_direktna_blizu/txt/DBHSB1/"
ime_out="C:/Users/matij/Desktop/M31_direktna_blizu/txt/DBHSB2/"
kartd="disk_"    
kartb="bulge_"
karth="halo_"
karts="stars_"
kartbnd="bndry_"
def r_3(a,b,c):
    return (a**2 + b**2 + c**2)**0.5
def cm(NIZX,NIZY,NIZZ,NIZM):
    N=len(NIZM)
    ukmass=0
    xc=0
    yc=0
    zc=0
    for i in range(N):
        ukmass+=NIZM[i]
    for i in range(N):
        xc+=NIZM[i]*NIZX[i]    
        yc+=NIZM[i]*NIZY[i]
        zc+=NIZM[i]*NIZZ[i]
    xc/=ukmass    
    yc/=ukmass    
    zc/=ukmass
    r=r_3(xc,yc,zc)
    return xc,yc,zc,r

for k in range(poc,kr):
    print(k/kr*100)
    if k<=9:
        deo = "00"
    if k<=99 and k>=10:
        deo = "0"
    if k>=100:
        deo = ""    
    diskkart = ime_in + kartd + deo + str(k) + ".txt"        
    bulgekart = ime_in + kartb + deo + str(k) + ".txt"
    halokart = ime_in + karth + deo + str(k) + ".txt"    
    starskart = ime_in + karts + deo + str(k) + ".txt"
    bndrykart = ime_in + kartbnd + deo + str(k) + ".txt"    

    #citanje    
    Md,Xd,Yd,Zd,VXd,VYd,VZd= np.loadtxt(diskkart, unpack=True)#ovde ubacujes disk
    Mb,Xb,Yb,Zb,VXb,VYb,VZb= np.loadtxt(bulgekart, unpack=True)#ovde ubacujes bulge
    Mh,Xh,Yh,Zh,VXh,VYh,VZh= np.loadtxt(halokart, unpack=True)#ovde ubacujes halo + disk
    Ms,Xs,Ys,Zs,VXs,VYs,VZs= np.loadtxt(starskart, unpack=True)#ovde ubacujes bulge
    Mbn,Xbn,Ybn,Zbn,VXbn,VYbn,VZbn= np.loadtxt(bndrykart, unpack=True)#ovde ubacujes halo
#     print(len(Md))
    dxd,dyd,dzd,rd=cm(Xd,Yd,Zd,Md)
    dxh,dyh,dzh,rzh=cm(Xh,Yh,Zh,Mh)
    dxb,dyb,dzb,rzb=cm(Xb,Yb,Zb,Mb)
    dxs,dys,dzs,rzs=cm(Xs,Ys,Zs,Ms)
    dxbn,dybn,dzbn,rzbn=cm(Xbn,Ybn,Zbn,Mbn)

    LEND=len(Md)
    LENH=len(Mh)
    LENB=len(Mb)
    LENS=len(Ms)
    LENBN=len(Mbn)
    
    for i in range(LEND):
        Xd[i]-=dxd
        Yd[i]-=dyd
        Zd[i]-=dzd
    for i in range(LENH):
        Xh[i]-=dxh
        Yh[i]-=dyh
        Zh[i]-=dzh
    for i in range(LENB):
        Xb[i]-=dxb
        Yb[i]-=dyb
        Zb[i]-=dzb
    for i in range(LENS):
        Xs[i]-=dxs
        Ys[i]-=dys
        Zs[i]-=dzs
    for i in range(LENBN):
        Xbn[i]-=dxbn
        Ybn[i]-=dybn
        Zbn[i]-=dzbn
    diskout = ime_out + kartd + deo + str(k) + ".txt"        
    bulgeout = ime_out + kartb + deo + str(k) + ".txt"
    haloout = ime_out + karth + deo + str(k) + ".txt"    
    starsout = ime_out + karts + deo + str(k) + ".txt"
    bndryout = ime_out + kartbnd + deo + str(k) + ".txt"    
    
    file= open(diskout,'w')        
    for i in range(LEND):
        file.write(str(Md[i]) + " " + str(Xd[i])  + " " + str(Yd[i]) + " " + str(Zd[i]) + " " + str(VXd[i]) + " " + str(VYd[i]) + " " + str(VZd[i]) + "\n") 
    file.close
    
    file= open(bulgeout,'w')        
    for i in range(LENB):
        file.write(str(Mb[i]) + " " + str(Xb[i])  + " " + str(Yb[i]) + " " + str(Zb[i]) + " " + str(VXb[i]) + " " + str(VYb[i]) + " " + str(VZb[i]) + "\n") 
    file.close
    
    file= open(haloout,'w')        
    for i in range(LENH):
        file.write(str(Mh[i]) + " " + str(Xh[i])  + " " + str(Yh[i]) + " " + str(Zh[i]) + " " + str(VXh[i]) + " " + str(VYh[i]) + " " + str(VZh[i]) + "\n") 
    file.close
    
    file= open(starsout,'w')        
    for i in range(LENS):
        file.write(str(Ms[i]) + " " + str(Xs[i])  + " " + str(Ys[i]) + " " + str(Zs[i]) + " " + str(VXs[i]) + " " + str(VYs[i]) + " " + str(VZs[i]) + "\n") 
    file.close
    
    file= open(bndryout,'w')        
    for i in range(LENBN):
        file.write(str(Mbn[i]) + " " + str(Xbn[i])  + " " + str(Ybn[i]) + " " + str(Zbn[i]) + " " + str(VXbn[i]) + " " + str(VYbn[i]) + " " + str(VZbn[i]) + "\n") 
    file.close
    
    
print('END')