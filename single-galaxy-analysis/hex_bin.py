import numpy as np
import matplotlib.pyplot as plt

N=100
poc=0
kr=N+1
#############

ime_in= "C:/Users/matij/Desktop/M31_direktna_blizu/txt/DBHSB2/"
sn_out= 'C:/Users/matij/Desktop/M31_direktna_blizu/txt/rezultati/bin/hex/'

kartd="disk_"    
#sn_dbxz="dbxz_"
sn_xy="xy_"
snmin_xy="xy_rez_"

#sn_xz="xz_"
#sn_yz="yz_"
my_dpi=300

for k in range(0,1):
    
    if k<=9:
        deo = "00"
    if k<=99 and k>=10:
        deo = "0"
    if k>=100:
        deo = ""
        
    diskkart = ime_in + kartd + deo + str(k) + ".txt"        
    Md,Xd,Yd,Zd,VXd,VYd,VZd= np.loadtxt(diskkart, unpack=True)#ovde ubacujes disk
    
    xmin = -20
    xmax =  20
    ymin = -20
    ymax =  20
    plt.subplot(111)
    plt.hexbin(Xd,Yd,bins='log')
    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    cb = plt.colorbar()
    cb.set_label('log(N)')
    plt.title("T = " + str(k/10*0.5) + ' Gyr')    
    plt.savefig(sn_out + '_20_' + 'disk_' + deo + str(k) + '.jpg',dpi=my_dpi)
    plt.show()    
    """
    xmin = -10 #-20
    xmax =  10 #20
    ymin = -10 #-20
    ymax =  10 #20
    plt.subplot(111)
    plt.hexbin(Xd,Yd,bins='log', cmap=plt.cm.inferno)
    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    cb = plt.colorbar()
    cb.set_label('log(N)')
    plt.title("T = " + str(k/10*0.5) + ' Gyr')
    plt.savefig(sn_out + '_10_' + 'disk_' + deo + str(k) + '.jpg',dpi=my_dpi)
    plt.show()    
    
    xmin = -34 #-20
    xmax =  34 #20
    ymin = -34 #-20
    ymax =  34 #20
    plt.subplot(111)
    plt.hexbin(Xd,Yd,bins='log', cmap=plt.cm.inferno)
    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    cb = plt.colorbar()
    cb.set_label('log(N)')
    plt.title("T = " + str(k/10*0.5) + ' Gyr')
    plt.text(-33,29,"T = " + str(k/10*0.5) + ' Gyr',fontsize=15,color='red')    
    plt.savefig(sn_out + 'disk_' + deo + str(k) + '.jpg',dpi=my_dpi)
    plt.show()
    
    xmin = -50 #-20
    xmax =  50 #20
    ymin = -50 #-20
    ymax =  50 #20
    plt.subplot(111)
    plt.hexbin(Xd,Yd,bins='log', cmap=plt.cm.inferno)
    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    cb = plt.colorbar()
    cb.set_label('log(N)')
    plt.title("T = " + str(k/10*0.5) + ' Gyr')
    plt.text(-45,40,"T = " + str(k/10*0.5) + ' Gyr',fontsize=15,color='red')    
    plt.savefig(sn_out + '50_' +'disk_' + deo + str(k) + '.jpg',dpi=my_dpi)
    plt.show() 
    """