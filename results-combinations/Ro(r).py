import numpy as np
import scipy as scipy
import pylab 
import math as math
import numpy as np
import matplotlib.pyplot as plt
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
import matplotlib.lines as mlines


n100 = mlines.Line2D([], [], color='black', markersize=15, label='T=5 Gyr',linestyle = ':')
n000 = mlines.Line2D([], [], color='black', markersize=15, label='T=0 Gyr',linestyle = '-')


NIZM,NIZX,NIZY,NIZZ,NIZVX,NIZVY,NIZVZ= np.loadtxt("C:/Users/matij/Desktop/Patuljak_izolacija/txt/DBH2/bulge_000.txt", unpack=True)
#povrsinska gustina
N=len(NIZM)
Rad2=[]
Rad3=[]
for i in range(N):
    Rad2.append((NIZX[i]**2 + NIZY[i]**2)**0.5)
#max2=int(max(Rad2))
#print(max2)
rez=0.1
rl=0
rd=rl+rez
rmax=5
Rho=[]
R = []

while rl <= rmax:
    m = 0
    for i in range(N):
        r2 = Rad2[i]
        if rl <= r2 and r2 < rd:
            m += NIZM[i]
    S = 4/3 * 3.14159 * (rd**3 - rl**3)
    Rho.append(m / S)  # povrsinska gustina!!!
    R.append(rl)
    rl += rez
    rd += rez

NIZM1,NIZX1,NIZY1,NIZZ1,NIZVX1,NIZVY1,NIZVZ1= np.loadtxt("C:/Users/matij/Desktop/Patuljak_izolacija/txt/DBH2/bulge_100.txt", unpack=True)
# povrsinska gustina
N1 = len(NIZM1)
Rad21 = []
Rad31 = []
for i in range(N1):
    Rad21.append((NIZX1[i]**2 + NIZY1[i]**2)**0.5)
# max2=int(max(Rad2))
# print(max2)
rez1 = 0.1
rl1 = 0
rd1 = rl1 + rez1
rmax1 = 5
Rho1 = []
R1 = []

while rl1 <= rmax1:
    m1 = 0
    for i in range(N1):
        r21 = Rad21[i]
        if rl1 <= r21 and r21 < rd1:
            m1 += NIZM1[i]
    S1 = 4 / 3 * 3.14159 * (rd1**3 - rl1**3)
    Rho1.append(m1 / S1)  # povrsinska gustina!!!
    R1.append(rl1)
    rl1 += rez1
    rd1 += rez1

for i in range(len(Rho)):
    Rho[i] = Rho[i] / 1e8
    Rho1[i] = Rho1[i] / 1e8

plt.plot(R, Rho, c='black', linestyle='-')
plt.plot(R1, Rho1, c='black', linestyle=':')
plt.xlim(0, 2)  # ukoliko je patuljak racunat onda se otkomentarise
plt.xlabel('$R  [kpc]$')
plt.ylabel(r'$\rho [ 10^8 Msol/kpc^3]$')
plt.legend(handles=[n000, n100], loc=7)
plt.legend()
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/Profili_gustine/Gustina_patuljak.png',dpi=90)
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/Profili_gustine/Gustina_patuljak.eps',dpi=90)
plt.show()
