import numpy as np
import matplotlib.pyplot as plt
#############
N=101
poc=0
kr=N+1
#############
ime_in= "C:/Users/matij/Desktop/Galaksije/M31_txt/dbh_za_upotrebu/"
kartd="disk_"    
kartb="bulge_"
karth="halo_"
kartbar="bar_"
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
    return r,xc,yc,zc

razd=[]
razb=[]
razh=[]
razbar=[]
DISKX=[]
DISKY=[]
DISKZ=[]
HALOX=[]
HALOY=[]
HALOZ=[]
BULGEX=[]
BULGEY=[]
BULGEZ=[]
BARIONIX=[]
BARIONIY=[]
BARIONIZ=[]
ind=[]
t=0
dt=0.1    
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
    barkart = ime_in + kartbar + deo + str(k) + ".txt"    
    
    #citanje    
    Md,Xd,Yd,Zd,VXd,VYd,VZd= np.loadtxt(diskkart, unpack=True)#ovde ubacujes disk
    Mb,Xb,Yb,Zb,VXb,VYb,VZb= np.loadtxt(bulgekart, unpack=True)#ovde ubacujes bulge
    Mh,Xh,Yh,Zh,VXh,VYh,VZh= np.loadtxt(halokart, unpack=True)#ovde ubacujes halo
    Mbar,Xbar,Ybar,Zbar,VXbar,VYbar,VZbar= np.loadtxt(barkart, unpack=True)#ovde ubacujes halo
    BULGEX.append(Xb)    
    BULGEY.append(Yb)    
    BULGEZ.append(Zb)    
    HALOX.append(Xh)    
    HALOY.append(Yh)    
    HALOZ.append(Zh)    
    DISKX.append(Xd)    
    DISKY.append(Yd)    
    DISKZ.append(Zd)    
    BARIONIX.append(Xbar) 
    BARIONIY.append(Ybar)
    BARIONIZ.append(Zbar)
    
    rcc,xcc,ycc,zcc=cm(Xd,Yd,Zd,Md)
    razd.append(rcc)
    rcc,xcc,ycc,zcc=cm(Xb,Yb,Zb,Mb)
    razb.append(rcc)
    rcc,xcc,ycc,zcc=cm(Xh,Yh,Zh,Mh)
    razh.append(rcc)
    rcc,xcc,ycc,zcc=cm(Xbar,Ybar,Zbar,Mbar)
    razbar.append(rcc)
    ind.append(t)    
    t+=dt

plt.scatter(DISKX[0],DISKY[0])
plt.scatter(DISKX[101],DISKY[101],c='yellow')
plt.title("drift diska")
plt.xlabel("X[kpc]")
plt.ylabel("Y[kpc]")
plt.savefig('C:/Users/matij/Desktop/Galaksije/M31_txt/driftovanje/drift_M31 diska')
plt.show()

plt.scatter(HALOX[0],HALOY[0])
plt.scatter(HALOX[101],HALOY[101],c='yellow')
plt.title("drift halo")
plt.xlabel("X[kpc]")
plt.ylabel("Y[kpc]")
plt.savefig('C:/Users/matij/Desktop/Galaksije/M31_txt/driftovanje/drift_M31 halo')
plt.show()

plt.scatter(BULGEX[0],BULGEY[0])
plt.scatter(BULGEX[101],BULGEY[101],c='yellow')
plt.title("drift bulge")
plt.xlabel("X[kpc]")
plt.ylabel("Y[kpc]")
plt.savefig('C:/Users/matij/Desktop/Galaksije/M31_txt/driftovanje/drift_M31 bulge')
plt.show()

plt.scatter(BARIONIX[0],BARIONIY[0])
plt.scatter(BARIONIX[101],BARIONIY[101],c='yellow')
plt.title("drift barionske materije")
plt.xlabel("X[kpc]")
plt.ylabel("Y[kpc]")
plt.savefig('C:/Users/matij/Desktop/Galaksije/M31_txt/driftovanje/drift_M31 barionska materija')
plt.show()


plt.plot(ind,razd)
plt.title("drift diska (u vremenu)")
plt.xlabel("T[Gyr]")
plt.ylabel("R[kpc]")
plt.savefig('C:/Users/matij/Desktop/Galaksije/M31_txt/driftovanje/drift_M31 disk (vreme)')
plt.show()

plt.plot(ind,razh)
plt.title("drift halo (u vremenu)")
plt.xlabel("T[Gyr]")
plt.ylabel("R[kpc]")
plt.savefig('C:/Users/matij/Desktop/Galaksije/M31_txt/driftovanje/drift_M31 halo (vreme)')
plt.show()

plt.plot(ind,razb)
plt.title("drift bulge (u vremenu)")
plt.xlabel("T[Gyr]")
plt.ylabel("R[kpc]")
plt.savefig('C:/Users/matij/Desktop/Galaksije/M31_txt/driftovanje/drift_M31 bulge (vreme)')
plt.show()

plt.plot(ind,razbar)
plt.title("drift barionske materije(u vremenu)")
plt.xlabel("T[Gyr]")
plt.ylabel("R[kpc]")
plt.savefig('C:/Users/matij/Desktop/Galaksije/M31_txt/driftovanje/drift_M31 barionska (vreme)')
plt.show()

plt.plot(ind,razd, c='b')
plt.plot(ind,razb, c='r')
plt.plot(ind,razbar, c='g')
plt.title("odnos drifta diska/bulgea i barionske")
plt.xlabel("T[Gyr]")
plt.ylabel("R[kpc]")
plt.savefig('C:/Users/matij/Desktop/Galaksije/M31_txt/driftovanje/odnos drifta barionske sa pojedinacnim driftom (vreme)')
plt.show()

plt.plot(ind,razd, c='b')
plt.plot(ind,razb, c='r')
plt.plot(ind,razh, c='g')
plt.title("drift sve 3, b-d, r-b, g-h")
plt.xlabel("T[Gyr]")
plt.ylabel("R[kpc]")
plt.savefig('C:/Users/matij/Desktop/Galaksije/M31_txt/driftovanje/drift d(b)b(r)h(g)_M31 (vreme)')
plt.show()
    
print("END")

