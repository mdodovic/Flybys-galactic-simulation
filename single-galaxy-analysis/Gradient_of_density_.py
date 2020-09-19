import numpy as np
import math
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
import matplotlib.pyplot as plt
def r_3(a,b,c): #fja za intenzitet vektora
    return (a*a + b*b + c*c)**0.5

N=100
poc=0
kr=N+1
#############
ime_in= "C:/Users/matij/Desktop/Patuljak_direktna/txt/DBHSB2/"
kartd="disk_"    
#kartb="bulge_"
#karth="halo_"
#karts="stars_"
#barionska="bar_"
    
for k in range(poc,kr):
    print(k/kr*100)
    if k<=9:
        deo = "00"
    if k<=99 and k>=10:
        deo = "0"
    if k>=100:
        deo = ""
    #x z y vx vz vy        
    diskkart = ime_in + kartd + deo + str(k) + ".txt"        
#    bulgekart = ime_in + kartb + deo + str(k) + ".txt"
    #halokart = ime_in + karth + deo + str(k) + ".txt"
    #starskart = ime_in + karts + deo + str(k) + ".txt"
    #citanje    
    #Msol kpc km/s
    Md,Xd,Yd,Zd,VXd,VYd,VZd= np.loadtxt(diskkart, unpack=True)#ovde ubacujes disk
#    Mb,Xb,Yb,Zb,VXb,VYb,VZb= np.loadtxt(bulgekart, unpack=True)#ovde ubacujes bulge
    #Mh,Xh,Yh,Zh,VXh,VYh,VZh= np.loadtxt(halokart, unpack=True)#ovde ubacujes halo
    #Xs,Ys,Zs,VXs,VYs,VZs= np.loadtxt(starskart, unpack=True)#ovde ubacujes stars        
    #definisanje matrice
    M=[];X=[];Y=[];Z=[];VX=[];VY=[];VZ=[];
    for i in range(len(Md)):
        M.append(Md[i])
        X.append(Xd[i])
        Y.append(Yd[i])
        Z.append(Zd[i])
        VX.append(VXd[i])
        VY.append(VYd[i])
        VZ.append(VZd[i])
#    for i in range(len(Mb)):
#        M.append(Mb[i])
#        X.append(Xb[i])
#        Y.append(Yb[i])
#        Z.append(Zb[i])
#        VX.append(VXb[i])
#        VY.append(VYb[i])
#        VZ.append(VZb[i])
    
    
    XL=0  #leva granica pravougaonika
    XD=10 #8.699999999999989 #desna granica pravougaonika #rotaciona kriva
    r=1  #sirinapravougaonika
    alfa=0
    dalfa=1   
    Xdl=XL
    Ydl=-r
    Xgd=XD
    Ygd=r

    
    x=[] #niz cestica koje pripadaju ravougaoniku x, y osa i njihove mase
    y=[]
    m=[]
    Mass=[]
    Radius=[]
    Razlika=[]
    Razlika_rho=[]
    Ugao=[]
    RHO=[]
    while alfa <= 360:
        N=len(X)
        #pakovanje cetica koje su u okviru (leva granica , desna granica)
        for i in range(N):
            if Xdl <= X[i] and X[i] <= Xgd and Ydl <= Y[i] and Y[i] <= Ygd:
                x.append(X[i])
                y.append(Y[i])
                m.append(M[i])
            
        n=len(x)
    
        rez=1 #velicina bina - velicina podeoka u pravougaoniku u kom se racuna gustina

        xl=XL
        xd=XL+rez
        xmax=XD
        while xd <= xmax:
            m_temp=0#privremena masa na koju se upsiuju svi u datim pravougaonicima
            for i in range(n):
                if xl <= x[i] and x[i] <= xd:
                    m_temp+=m[i]
            Mass.append(m_temp) #ako hoces gustinu podeli m_temp sa povrsinom jednog podeoka, 2*rez*r
            RHO.append(m_temp/2*rez*r)    

            Radius.append(xd)
            xl=xl+rez
            xd=xl+rez
        #plt.plot(Radius,Mass)
        #plt.show()
        Razlika.append((max(Mass)-min(Mass)))
        Razlika_rho.append(max(RHO) - min(RHO))    
        Ugao.append(alfa)
    
    
    
        for i in range(N):
            a=X[i]
            b=Y[i]        
            X[i]=a*math.cos( math.radians(dalfa*1.0) )-b*math.sin(math.radians(dalfa*1.0))
            Y[i]=a*math.sin( math.radians(dalfa*1.0) )+b*math.cos(math.radians(dalfa*1.0))
        
        x[:]=[]
        y[:]=[]
        m[:]=[]
        Radius[:]=[]
        Mass[:]=[]
        RHO[:]=[]
        alfa+=dalfa

    plt.plot(Ugao,Razlika_rho)    
    #plt.plot(Ugao,Razlika)
    plt.title('sn' + deo + str(k))
    plt.xlabel('UGAO [deg]')
    plt.ylabel('dRHO [Msol/kpc^2]')
    plt.title("T = " + str(k/10*0.5) + ' Gyr')
    plt.savefig('C:/Users/matij/Desktop/Patuljak_direktna/txt/rezultati/Gradijent_gustine/razlika_gustina' + deo + str(k) + '.jpg')    
    plt.show()