import numpy as np
import scipy as scipy
import math as math
import matplotlib.pyplot as plt
import pylab 
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
import matplotlib.lines as mlines

def r_3(a,b,c): #fja za intenzitet vektora
    return (a*a + b*b + c*c)**0.5
def Rotaciona(diskkart,bulgekart,halokart,st):
#paramtri rotacione krive

    #citanje    
    #Msol kpc km/s
    Md,Xd,Yd,Zd,VXd,VYd,VZd= np.loadtxt(diskkart, unpack=True)#ovde ubacujes disk
    Mb,Xb,Yb,Zb,VXb,VYb,VZb= np.loadtxt(bulgekart, unpack=True)#ovde ubacujes bulge
    Mh,Xh,Yh,Zh,VXh,VYh,VZh= np.loadtxt(halokart, unpack=True)#ovde ubacujes halo
    #Xs,Ys,Zs,VXs,VYs,VZs= np.loadtxt(starskart, unpack=True)#ovde ubacujes stars    

    r0=0.1 #pocetni radijus
    rez=0.05 #rezolucija
    rmax=25 #maksimalni radijus
    vel_conversion=3.086e+16#konvertovanje kpc/s u km/s
    M=[];X=[];Y=[];Z=[];
    N=len(Md)+len(Mb)+len(Mh)
    Nd=len(Md)
    Nh=len(Mh)
    Nb=len(Mb)
    
    for k in range(Nd):
        M.append(Md[k])
        X.append(Xd[k])
        Y.append(Yd[k])
        Z.append(Zd[k])
    
    for k in range(Nb):
        M.append(Mb[k])
        X.append(Xb[k])
        Y.append(Yb[k])
        Z.append(Zb[k])
    
    for k in range(Nh):
        M.append(Mh[k])
        X.append(Xh[k])
        Y.append(Yh[k])
        Z.append(Zh[k])    
    
    G = 4.515353945657138e-39 #kpc^3/(Msol*s^2)
    Rad3=[((X[i]**2 + Y[i]**2 + Z[i]**2)**0.5) for i in range(N)]
    Rad3h=[((Xh[i]**2 + Yh[i]**2 + Zh[i]**2)**0.5) for i in range(Nh)]
    Rad3d=[((Xd[i]**2 + Yd[i]**2 + Zd[i]**2)**0.5) for i in range(Nd)]
    Rad3b=[((Xb[i]**2 + Yb[i]**2 + Zb[i]**2)**0.5) for i in range(Nb)]
    Vc=[]
    Vcd=[]
    Vcb=[]
    Vch=[]
    R=[]
    #disk
    r=r0
    while r<=rmax:
        m=0
        for i in range(Nd):
            r3 = Rad3d[i]
            if r >= r3:
                m += Md[i] #dodavanje mase koaj je u radijusu r
                
        v=(G*m/r)**0.5        #racunanje rotacione brzine
        Vcd.append(v*vel_conversion) #konvertovanje jedinica u km/s i dodavanje na niz
        r += rez
    #bulge
    r=r0
    while r<=rmax:
        m=0
        for i in range(Nb):
            r3 = Rad3b[i]
            if r >= r3:
                m += Mb[i] #dodavanje mase koaj je u radijusu r
                
        v=(G*m/r)**0.5        #racunanje rotacione brzine
        Vcb.append(v*vel_conversion) #konvertovanje jedinica u km/s i dodavanje na niz
        r += rez
    #halo    
    r=r0
    while r<=rmax:
        m=0
        for i in range(Nh):
            r3 = Rad3h[i]
            if r >= r3:
                m += Mh[i] #dodavanje mase koaj je u radijusu r
                
        v=(G*m/r)**0.5        #racunanje rotacione brzine
        Vch.append(v*vel_conversion) #konvertovanje jedinica u km/s i dodavanje na niz
        r += rez
    
    #objedinjeno
    r=r0
    while r<=rmax:
        m=0
        for i in range(N):
            r3 = Rad3[i]
            if r >= r3:
                m += M[i] #dodavanje mase koaj je u radijusu r
                
        v=(G*m/r)**0.5        #racunanje rotacione brzine
        R.append(r)
        Vc.append(v*vel_conversion) #konvertovanje jedinica u km/s i dodavanje na niz
        r += rez


    plt.plot(R,Vc,c='blue')
    plt.plot(R,Vcb,c='purple')
    plt.plot(R,Vcd,c='green')
    plt.plot(R,Vch,c='red')
    plt.xlabel('r[kpc]')
    plt.ylabel('Vc[km/s]')
    disk = mlines.Line2D([], [], color='green', markersize=15, label='disk')
    bulge = mlines.Line2D([], [], color='purple', markersize=15, label='bulge')
    halo = mlines.Line2D([], [], color='red', markersize=15, label='halo')
    objedinjeno = mlines.Line2D([], [], color='blue', markersize=15, label='sve')
    plt.legend(handles=[disk,bulge,halo,objedinjeno], loc=7)
    
    plt.savefig('C:/Users/matij/Desktop/Patuljak_direktna/txt/rezultati/rotacione_krive/Rotaciona/Rotacione_krive_' + str(st) + '.jpg')
    plt.show()
    
    r=R[Vc.index(max(Vc))] #index maksimalne brzine i radijus za koju se ta brzina postize se printuje
    r=round(r,3)
    print(r)
    
    plt.plot(R,Vc,c='blue')
    plt.plot([r,r],[0,max(Vc)], c='red')
    plt.xlabel('r[kpc]')
    plt.ylabel('Vc[km/s]')
    plt.text(r+1, max(Vc)/2, 'Rmax = ' + str(r), style='italic',fontsize=20)
    
    plt.savefig('C:/Users/matij/Desktop/Patuljak_direktna/txt/rezultati/rotacione_krive/Rmax/Rmax_' + str(st) +  '.jpg')
    plt.show()
        
    return r


BROJAC=0
N=100
poc=0
kr=N+1
#############

ime_in= "C:/Users/matij/Desktop/Patuljak_direktna/txt/DBHSB2/"
kartd="disk_"    
kartb="bulge_"
karth="halo_"
#karts="stars_"
#barionska="bar_"
    
T=[]    
Rmax=[]

for k in range(poc,kr):
    
    if k<=9:
        deo = "00"
    if k<=99 and k>=10:
        deo = "0"
    if k>=100:
        deo = ""
    #x z y vx vz vy        
    diskkart = ime_in + kartd + deo + str(k) + ".txt"        
    bulgekart = ime_in + kartb + deo + str(k) + ".txt"
    halokart = ime_in + karth + deo + str(k) + ".txt"
    #starskart = ime_in + karts + deo + str(k) + ".txt"
    rmax=Rotaciona(diskkart,bulgekart,halokart,deo+str(k))
    Rmax.append(rmax)
    T.append(k/20)

file=open('C:/Users/matij/Desktop/Patuljak_direktna/txt/rezultati/rotacione_krive/Rmax.txt','w')
for i in range(len(T)):
    file.write(str(T[i]) + ' ' + str(Rmax[i]) + '\n')
file.close()
