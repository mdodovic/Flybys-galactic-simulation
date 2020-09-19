import numpy as np
import matplotlib.pyplot as plt

M, X, Y, Z, VX, VY, VZ = np.loadtxt('galaxy.txt', unpack = True)


Md=[]
vxd=[]
vyd=[]
vzd=[]
xd=[]
yd=[]
zd=[]
Mb=[]
vxb=[]
vyb=[]
vzb=[]
xb=[]
yb=[]
zb=[]
Mh=[]
vxh=[]
vyh=[]
vzh=[]
xh=[]
yh=[]
zh=[]
i=1
j=0

while (i<len(M)):
    if M[i-1]==M[i]:
        Md.append(M[i-1])
        vxd.append(VX[i-1])
        vyd.append(VY[i-1])
        vzd.append(VZ[i-1])
        xd.append(X[i-1])
        yd.append(Y[i-1])
        zd.append(Z[i-1])
        j=i
    else:
        Md.append(M[i-1])
        vxd.append(VX[i-1])
        vyd.append(VY[i-1])
        vzd.append(VZ[i-1])
        xd.append(X[i-1])
        yd.append(Y[i-1])
        zd.append(Z[i-1])
        
        break

    i+=1
i = j+2
j=i

while (i<len(M)):
    if M[i-1]==M[i]:
        Mb.append(M[i-1])
        vxb.append(VX[i-1])
        vyb.append(VY[i-1])
        vzb.append(VZ[i-1])
        xb.append(X[i-1])
        yb.append(Y[i-1])
        zb.append(Z[i-1])
        j=i
    else:
        Mb.append(M[i-1])
        vxb.append(VX[i-1])
        vyb.append(VY[i-1])
        vzb.append(VZ[i-1])
        xb.append(X[i-1])
        yb.append(Y[i-1])
        zb.append(Z[i-1])
   
        break
    i+=1

i = j+2
j=i

while (i<len(M)):
    if M[i-1]==M[i]:
        Mh.append(M[i-1])
        vxh.append(VX[i-1])
        vyh.append(VY[i-1])
        vzh.append(VZ[i-1])
        xh.append(X[i-1])
        yh.append(Y[i-1])
        zh.append(Z[i-1])
        j=i
    else:
        Mh.append(M[i-1])
        vxh.append(VX[i-1])
        vyh.append(VY[i-1])
        vzh.append(VZ[i-1])
        xh.append(X[i-1])
        yh.append(Y[i-1])
        zh.append(Z[i-1])
   
        break
    i+=1
Mh.append(M[i-1])
vxh.append(VX[i-1])
vyh.append(VY[i-1])
vzh.append(VZ[i-1])
xh.append(X[i-1])
yh.append(Y[i-1])
zh.append(Z[i-1])




###Postoje svi nizovi
plt.scatter(xb,zb, c='r')
plt.scatter(xd,zd)
