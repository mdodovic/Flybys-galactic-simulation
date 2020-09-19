import numpy as np
import scipy as scipy
import math as math
import matplotlib.pyplot as plt
rmax=8.699999999999987
#rmax=13.499999999999968 #radijus do kog se posmatra disk (prividna velicina diska) - dobija se iz rotacione krive
def r_3(a,b,c): #fja za intenzitet vektora
    return (a*a + b*b + c*c)**0.5
#definisanje matrice
Mu,Xu,Yu,Zu,VXu,VYu,VZu=np.loadtxt("C:/Users/matij/Desktop/Bliksi_prolaz/txt/DBHS2/disk_000.txt", unpack=True) #ucitavanje fajla sa podacima
#Mu,Xu,Yu,Zu,VXu,VYu,VZu=np.loadtxt("C:/Users/matij/Desktop/Bliksi_prolaz/txt/DBHS2/disk_025.txt", unpack=True) #ucitavanje fajla sa podacima

M=[];X=[];Y=[];Z=[];VX=[];VY=[];VZ=[];
for i in range(len(Mu)):
    if r_3(Xu[i],Yu[i],Zu[i]) <= rmax: # and r_3(Xu[i],Yu[i],Zu[i])>=5 :
        M.append(Mu[i])
        X.append(Xu[i])
        Y.append(Yu[i])
        Z.append(Zu[i])
        VX.append(VXu[i])
        VY.append(VYu[i])
        VZ.append(VZu[i])
#Msol kpc km/s
def r_3(a,b,c): #fja za intenzitet vektora
    return (a*a + b*b + c*c)**0.5
def sort(a,b,c): #fja za uredjivanje 3 broja u rastuci poredak
    x=[a,b,c]
    x.sort()
    return x[0],x[1],x[2]        
N=len(M) #broj cestica
I=[[0 for i in range(3)] for i in range (3)]#matrica nula(3x3) potrebna za momente inercije
tmp=0
I11=I12=I13=I21=I22=I23=I31=I32=I33=0
#izracunavanje momenta inercije diska
for i in range(N):
    if rmax>r_3(X[i],Y[i],Z[i]):
        I11 += X[i]*X[i]*M[i]
        I12 += X[i]*Y[i]*M[i]
        I13 += X[i]*Z[i]*M[i]
        I21 += Y[i]*X[i]*M[i]
        I22 += Y[i]*Y[i]*M[i]
        I23 += Y[i]*Z[i]*M[i]
        I31 += Z[i]*X[i]*M[i]
        I32 += Z[i]*Y[i]*M[i]
        I33 += Z[i]*Z[i]*M[i]
I[0][0]=I11; I[0][1]=I12; I[0][2]=I13; 
I[1][0]=I21; I[1][1]=I22; I[1][2]=I23;
I[2][0]=I31; I[2][1]=I32; I[2][2]=I33;
#matrica I je matrica momenata inercije 

w,v = np.linalg.eig(I)#izracunavanje svojstvenih vrednosti i vektora
I3,I2,I1=sort(w[0],w[1],w[2]) #svojstvene vrednosti sortirani tako da je I1 najvece a I3 najmanje
#print(I3,I2,I1)
#parametri elipse
#print('b/a = ' + str((I2/I1)**0.5))
#print('c/a = ' + str((I3/I1)**0.5))
#print('b/c = ' + str((I2/I1)**0.5/(I3/I1)**0.5))
v=v.T #transponovanje matrice svojstvenih vektora tako da v[0] bude prvi vektor v[1] drugi ...
#print(v)

v1=v[0] #prvi svojstveni vektor
v2=v[1] #drugi svojstveni vektor
v3=v[2] #treci svojstveni vektor
e1=ex=[1,0,0] #vektori normalnog koordinatnog sistema x-osa
e2=ey=[0,1,0] #vektori normalnog koordinatnog sistema y-osa
e3=ez=[0,0,1] #vektori normalnog koordinatnog sistema z-osa
e=[[0 for i in range(3)] for i in range(3)] #matrica normalnog koordinatnog sisitema
for i in range(3):
    e[0][i]=ex[i]  
    e[1][i]=ey[i]
    e[2][i]=ez[i]
#napravljena matrica normalnog koordinatnog sistema
def Qij(v1,v2):#ugao izmedju 2 vektora
    return (v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2])/((v1[0]**2 + v1[1]**2 + v1[2]**2)**0.5 * (v2[0]**2 + v2[1]**2 + v2[2]**2)**0.5) 

#svojstveni vektori
#print(v1)
#print(v2)
#print(v3)

#print( math.degrees(math.acos((v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2])/((v1[0]**2 + v1[1]**2 + v1[2]**2)**0.5 * (v2[0]**2 + v2[1]**2 + v2[2]**2)**0.5))))

#print( math.degrees(math.acos((v3[0]*v2[0] + v3[1]*v2[1] + v3[2]*v2[2])/((v3[0]**2 + v3[1]**2 + v3[2]**2)**0.5 * (v2[0]**2 + v2[1]**2 + v2[2]**2)**0.5))))

#print( math.degrees(math.acos((v3[0]*v1[0] + v3[1]*v1[1] + v3[2]*v1[2])/((v3[0]**2 + v3[1]**2 + v3[2]**2)**0.5 * (v1[0]**2 + v1[1]**2 + v1[2]**2)**0.5))))

Q=[[0 for i in range(3)] for i in range(3)] #matrica za rotaciju iz xyz u x'y'z'
Q=np.zeros((3,3))
#print(ugao)

#pravljenje matrice za rotaciju
for i in range(3):
    for j in range(3):
        Q[i][j]=Qij(v[i],e[j]) #konverzija x to x' (n nenormalan)
        #print(str(i) +' - ' + str(j) + ' ' + str(math.degrees(ugao[i][j])))

Q=np.linalg.inv(Q)

R=[]
TETA=[]
FI=[]
#ROTACIJA KOORDINATNOG SISTEMA - prebacivanje vektora iz xyz u (I1,I2,I3)
for i in range(N):
    #konverzija brzina i koordinata u koordinatni sistem momenata inercija
    VX[i] = VX[i]*Q[0][0] + VY[i]*Q[0][1] + VZ[i]*Q[0][2]  
    VY[i] = VX[i]*Q[0][0] + VY[i]*Q[0][1] + VZ[i]*Q[0][2]  
    VZ[i] = VX[i]*Q[0][0] + VY[i]*Q[0][1] + VZ[i]*Q[0][2]  
    X[i]  =  X[i]*Q[0][0]  +  Y[i]*Q[0][1]  +  Z[i]*Q[0][2] 
    Y[i]  =  X[i]*Q[1][0]  +  Y[i]*Q[1][1]  +  Z[i]*Q[1][2]
    Z[i]  =  X[i]*Q[2][1]  +  Y[i]*Q[2][1]  +  Z[i]*Q[2][2]
    #konverzina xyz(u sistemu momenata inercija) u R,TETA i FI - polarne koordinate
    R.append((X[i]**2 + Y[i]**2 + Z[i]**2)**0.5)
    TETA.append(math.acos(Z[i]/R[i]))
    FI.append(math.atan2(Y[i],X[i]))
#FI je polarni ugao, koji uvek ide od x ka y (u xy ravni)   
#preko formule se odredi A2
suma_cos=0
suma_sin=0
for i in range(N):
    suma_cos += math.cos(2*FI[i])
    suma_sin += math.sin(2*FI[i])
A2=1/len(M) * (suma_cos**2 + suma_sin**2)**0.5
print(A2)
    
    

#xyz -> r,teta,fi
#r=(x*x+y*y+z*z)**0.5
#teta = math.acos(z/r)
#fi = math.atan2(y,x)