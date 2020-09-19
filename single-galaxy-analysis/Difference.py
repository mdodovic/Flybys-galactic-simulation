import numpy as np
import matplotlib.pyplot as plt

N=100
poc=0
kr=N+1
#############
def r_3(a,b,c):
    return (a*a + b*b + c*c)**0.5
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

    return xc,yc,zc

ime_in= "C:/Users/matij/Desktop/M31_direktna_blizu/txt/DBHSB1/"
sn_out='C:/Users/matij/Desktop/M31_direktna_blizu/txt/rezultati/vizual/Rastojanje/'
kartd="disk_"    
kartb="bulge_"
karth="halo_"
karts="stars_"
kartbn="bndry_"
#sn_dbxz="dbxz_"
sn_ddxy="ddxy_"
sn_svexy="xy_"
#sn_dbxz="dbxz_"
#sn_dbyz="dbyz_"
#barionska="bar_"
    
Rast=[]
T=[]
Disk1=[]
Disk2=[]
for k in range(poc,kr):
    
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
    bndrykart = ime_in + kartbn + deo + str(k) + ".txt"

    #m x z y vx vy vz citanje       
    
    Md,Xd,Yd,Zd,VXd,VYd,VZd= np.loadtxt(diskkart, unpack=True)#ovde ubacujes disk
    Mh,Xh,Yh,Zh,VXh,VYh,VZh= np.loadtxt(halokart, unpack=True)#ovde ubacujes halo
    Mb,Xb,Yb,Zb,VXb,VYb,VZb= np.loadtxt(bulgekart, unpack=True)#ovde ubacujes bulge
    Ms,Xs,Ys,Zs,VXs,VYs,VZs= np.loadtxt(starskart, unpack=True)#ovde ubacujes stars
    Mbn,Xbn,Ybn,Zbn,VXbn,VYbn,VZbn= np.loadtxt(bndrykart, unpack=True)#ovde ubacujes stars
    #prve sve
    
    #druge sve    
    
    Rad_disk_1=[((Xd[i]**2 + Yd[i]**2 + Zd[i]**2)**0.5) for i in range(N)]
    Rad_disk_2=[((Xs[i]**2 + Ys[i]**2 + Zs[i]**2)**0.5) for i in range(N)]
    X1,Y1,Z1=cm(Xd,Yd,Zd,Md)
    X2,Y2,Z2=cm(Xs,Ys,Zs,Ms)
    Disk1.append(max(Rad_disk_1))
    Disk2.append(max(Rad_disk_2))
    Rast.append(((X2-X1)**2 + (Y2-Y1)**2 + (Z2-Z1)**2)**0.5)



    T.append(k/20)
    print((k+1))
    
    
    
print(min(Rast))    
d1=Disk1[Rast.index(min(Rast))] 
d2=Disk2[Rast.index(min(Rast))] 
T1=T[Rast.index(min(Rast))] 
print(d1)
print(d2)
print(T1)

file=open(sn_out + 'Rcm(T).txt','w')
for i in range(len(T)):
    file.write(str(T[i]) + ' ' + str(Rast[i]) + '\n')
file.close()

plt.plot(T,Rast)
plt.xlabel('T [Gyr]')
plt.ylabel('R [kpc]')
plt.savefig('C:/Users/matij/Desktop/rastojanje.jpg',dpi=300)
plt.show()