import numpy as np
import matplotlib.pyplot as plt
import math as math
import matplotlib.patches as patches

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
ime_in= "C:/Users/matij/Desktop/M31_direktna_blizu/txt/DBHSB2/"
#sn_out='C:/Users/matij/Desktop/Patuljak_direktna/txt/rezultati/vizual/disk/'
kartd="disk_"    
sn_xy="xy_"
snzum_xy="xy_rez_"
snuzum_xy="xy_rez2_"

#sn_xz="xz_"
#sn_yz="yz_"    
    
nizx=[]
nizy=[]
for k in range(10,11):
    
    if k<=9:
        deo = "00"
    if k<=99 and k>=10:
        deo = "0"
    if k>=100:
        deo = ""

    diskkart = ime_in + kartd + deo + str(k) + ".txt"        

    #m x z y vx vy vz citanje       
    
    Md,Xd,Yd,Zd,VXd,VYd,VZd= np.loadtxt(diskkart, unpack=True)#ovde ubacujes disk
    """
        #disk    
        plt.scatter(Xd,Yd,s=0.005)
        plt.xlim(-35,35)
        plt.ylim(-35,35)
        plt.xlabel('X [kpc]')
        plt.ylabel('Y [kpc]')
        plt.savefig(sn_out + sn_xy + deo + str(k) + '.jpg')
        plt.show()
    """
#    plt.scatter(Xd,Yd,s=0.001)
#    plt.xlim(-20,20)
#    plt.ylim(-20,20)
#    plt.xlabel('X [kpc]')
#    plt.ylabel('Y [kpc]')
#    plt.savefig(sn_out + snzum_xy + deo + str(k) + '.jpg')
#    plt.show()
    a=30
    plt.scatter(Xd,Yd,s=0.005)
    plt.xlim(-a,a)
    plt.ylim(-a,a)
    #plt.xlabel('X [kpc]')
    #plt.ylabel('Y [kpc]')
    #plt.text(-19,17, 'T = ' + str(k/10*0.5) +' Gyr' , color = 'red', fontsize =14, style = 'oblique') #, fontsize=13 )
    plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='off')
        

    left,right = -a,a
    low,high = -a,a
    plt.arrow(left, 0, right -left, 0, length_includes_head = True, head_width = 1, color = 'black')
    plt.arrow( 0, low, 0, high-low , length_includes_head = True, head_width = 1, color = 'black') 
    
    l=0
    d = 10
    s=2.5
    debljina = 2
    alfa = 30.0
    X=[l,d,d,l,l]
    Y=[-s,-s,s,s,-s]
    plt.plot(X,Y,c= 'red', linewidth=debljina) 
    for spine in plt.gca().spines.values():
        spine.set_visible(False)
    for i in range(len(X)):
        a=X[i]
        b=Y[i]        
        X[i]=a*math.cos(math.radians(-alfa))-b*math.sin(math.radians(-alfa))
        Y[i]=a*math.sin(math.radians(-alfa))+b*math.cos(math.radians(-alfa))
            
        
    plt.plot(X,Y,c='r',linewidth=debljina)

    style="Simple,tail_width=3,head_width=8,head_length=12"
    kw = dict(arrowstyle=style, color="red")
    
    a3 = patches.FancyArrowPatch((13,0), (10,-10) ,connectionstyle="arc3,rad=-0.3" , **kw)
    
    plt.gca().add_patch(a3)
    
    plt.text(28,-3,"X")        
    plt.text(-2.5,27,"Y")        
    
    plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/Skica/disk.jpg', dpi = 90)
    plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/Skica/disk.eps', dpi = 90)

    plt.show()


#    plt.scatter(Xd,Yd,s=0.002)
#    plt.xlim(-10,10)
#    plt.ylim(-10,10)
#    plt.xlabel('X [kpc]')
#    plt.ylabel('Y [kpc]')
#    plt.savefig(sn_out + snuzum_xy + deo + str(k) + '.jpg')
#    plt.show()


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

