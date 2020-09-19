import numpy as np
import matplotlib.pyplot as plt

N=100
poc=0
kr=N+1
#############
def centar(x):
    n=10
    while 1:
        if x>n:
            n+=10
        else:
            break
    return n
ime_in= "C:/Users/matij/Desktop/M31_direktna_blizu/txt/DBHSB1/"
sn_out= 'C:/Users/matij/Desktop/M31_direktna_blizu/txt/rezultati/vizual/bliski_prolaz/'
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
    
    
nizx=[]
nizy=[]
my_dpi=300
for k in range(100,101):
    
    if k<=9:
        deo = "00"
    if k<=99 and k>=10:
        deo = "0"
    if k>=100:
        deo = ""

    diskkart = ime_in + kartd + deo + str(k) + ".txt"        
    #bulgekart = ime_in + kartb + deo + str(k) + ".txt"
    #halokart = ime_in + karth + deo + str(k) + ".txt"
    starskart = ime_in + karts + deo + str(k) + ".txt"
    #bndrykart = ime_in + kartbn + deo + str(k) + ".txt"

    #m x z y vx vy vz citanje       
    
    Md,Xd,Yd,Zd,VXd,VYd,VZd= np.loadtxt(diskkart, unpack=True)#ovde ubacujes disk
    #Mh,Xh,Yh,Zh,VXh,VYh,VZh= np.loadtxt(halokart, unpack=True)#ovde ubacujes halo
    #Mb,Xb,Yb,Zb,VXb,VYb,VZb= np.loadtxt(bulgekart, unpack=True)#ovde ubacujes bulge
    Ms,Xs,Ys,Zs,VXs,VYs,VZs= np.loadtxt(starskart, unpack=True)#ovde ubacujes stars
    #Mbn,Xbn,Ybn,Zbn,VXbn,VYbn,VZbn= np.loadtxt(bndrykart, unpack=True)#ovde ubacujes stars
    
    #diskovi + blulge-ovi  
    """
    if k < 20:
        plt.scatter(Xd,Yd,s=0.005)
        plt.scatter(Xs,Ys,s=0.005)
        plt.xlim(-300,300)
        plt.ylim(-300,300)
        plt.xlabel('X [kpc]')
        plt.ylabel('Y [kpc]')
        plt.text(-290,250,'T = ' + str(k/10*0.5) +' Gyr', fontsize = 13)
        plt.savefig(sn_out + sn_ddxy + deo + str(k) + '.jpg',dpi=my_dpi)

        plt.show()

    if k >= 20:
        plt.scatter(Xd,Yd,s=0.005)
        plt.scatter(Xs,Ys,s=0.005)
        plt.xlim(-300,300)
        plt.ylim(-150,450)
        plt.xlabel('X [kpc]')
        plt.ylabel('Y [kpc]')
        plt.text(-290,350,'T = ' + str(k/10*0.5) +' Gyr', fontsize = 13)
        plt.savefig(sn_out + sn_ddxy + deo + str(k) + '.jpg',dpi=my_dpi)

        plt.show()
    """
    plt.scatter(Xd,Yd,s=0.005)
    plt.scatter(Xs,Ys,s=0.005)
    plt.xlim(-800,800)
    plt.ylim(-350,1250)

    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.text(-750,0,'T = ' + str(k/10*0.5) +' Gyr', fontsize = 13)
    plt.savefig(sn_out + sn_ddxy + deo + str(k) + '_800x800_.jpg',dpi=my_dpi)

    plt.show()


    """
    plt.scatter(Xd,Yd,s=0.005)
    plt.scatter(Xb,Yb,s=0.005)
    plt.scatter(Xh,Yh,s=0.005)
    plt.scatter(Xs,Ys,s=0.005)
    plt.scatter(Xbn,Ybn,s=0.005)    
    plt.xlim(-650,650)
    plt.ylim(-650,650)
    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.text(-600,500,'T = ' + str(k/10*0.5) +' Gyr', fontsize = 13)
    plt.savefig(sn_out + sn_svexy + deo + str(k) + '.jpg')
    plt.show()
    """
#    plt.scatter([Xd[0], Xd[100], Xd[580]],Zd,s=30)
#    plt.scatter(Xh,Zh,s=0.01)
#    plt.xlim(-7,7)
#    plt.ylim(-15,15)
    
#    plt.xlim(-centar(max(Rasxy)),centar(max(Rasxy)))
#    plt.ylim(-centar(max(Zd)),centar(max(Zd)))    
    #plt.savefig(sn_out + sn_dbxz + deo + str(k) + '.jpg')
    #plt.show()        

#    plt.scatter(Xd,Zd,s=0.01)
#    plt.scatter(Xh,Zh,s=0.01)
#    plt.xlim(-centar(max(Rasxy)),centar(max(Rasxy)))
#    plt.ylim(-centar(max(Rasxy)),centar(max(Rasxy)))    
#    plt.savefig(sn_out + sn_dbxz + deo + str(k) + '.jpg')
#    plt.show()        

#    plt.scatter(Yd,Zd,s=0.01)
#    plt.scatter(Yh,Zh,s=0.01)
#    plt.xlim(-centar(max(Rasxy)),centar(max(Rasxy)))
#    plt.ylim(-centar(max(Rasxy)),centar(max(Rasxy)))    
#    plt.savefig(sn_out + sn_dbyz + deo + str(k) + '.jpg')
#    plt.show()        

    #print('vizualizovana grupa: ' + str(k))

