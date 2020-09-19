import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

############################################################################################################
################# MIRUJUCA GALAKSIJA
############################################################################################################
###ovo su bliski bliski prolazi
T_izol   ,A2_izol   =np.loadtxt('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/M31_izolacija/A2/A2-parametar.txt', unpack=True)

T_M31_ret,A2_M31_ret=np.loadtxt('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/M31_M31_retrogradna/A2/A2-parametar.txt', unpack=True)


T_M31_dir,A2_M31_dir=np.loadtxt('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/M31_M31_direktna/A2/A2-parametar.txt', unpack=True)

T_p_dir  ,A2_p_dir  =np.loadtxt('C:/Users/matij/Desktop/kodovi_za_analizu/rezultati/Patuljak_M31_direktna/A2/A2-parametar.txt', unpack=True)

###daleki bliski prolazi

T_p_dir_daleko  ,A2_p_dir_daleko  =np.loadtxt('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/Patuljak_M31_direktna_daleki_bp/A2/A2-parametar.txt', unpack=True)

#T_p_ret_daleko  ,A2_p_ret_daleko  =np.loadtxt('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/Patuljak_M31_retrogradna_daleki_bp/A2/A2-parametar.txt', unpack=True)

T_M31_ret_daleko  ,A2_M31_ret_daleko  =np.loadtxt('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/M31_M31_retrogradna_daleki_bp/A2/A2-parametar.txt', unpack=True)

T_M31_dir_daleko  ,A2_M31_dir_daleko  =np.loadtxt('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/M31_M31_direktna_daleki_bp/A2/A2-parametar.txt', unpack=True)

T=[]
T[:]=T_izol[:]

c = 'black'

izol    = mlines.Line2D([], [], color=c, markersize=15, label='izolacija', linestyle = '-')
pat_dir = mlines.Line2D([], [], color=c, markersize=15, label='direktna_sferoidna_patuljasta',linestyle = '-.')
M31_dir = mlines.Line2D([], [], color=c, markersize=15, label='direktna_spiralna', linestyle = '-.')

M31_ret = mlines.Line2D([], [], color=c, markersize=15, label='retrogradna_spiralna', linestyle = '-.')

pat_dir_dalek = mlines.Line2D([], [], color=c, markersize=15, label='direktna_sferoidna_patuljasta',linestyle = '-.')
pat_ret_dalek = mlines.Line2D([], [], color=c, markersize=15, label='retrogradna_sferoidna_patuljasta')
M31_dir_dalek = mlines.Line2D([], [], color=c, markersize=15, label='direktna_spiralna', linestyle = '-.')
M31_ret_dalek = mlines.Line2D([], [], color=c, markersize=15, label='retrogradna_spiralna_II',linestyle = '-.')

###IZOLACIJA
plt.plot(T,A2_izol, c=c,linestyle = '-')
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')
plt.ylim(0,1)
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/izol.png',dpi=90)
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/izol.eps',dpi=90)

plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/Slika7.png',dpi=90)
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/Slika7.eps',dpi=90)


plt.show()


###Ic IIc
M31_ret1 = mlines.Line2D([], [], color=c, markersize=15, label='Ic',linestyle = '-')
M31_ret2 = mlines.Line2D([], [], color=c, markersize=15, label='IIc',linestyle = '--')


#plt.plot(T,A2_izol, c=c,linestyle = '-')
plt.plot(T,A2_M31_ret, c=c,linestyle = '-')
plt.plot(T,A2_M31_ret_daleko, c=c,linestyle = '--')
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')

plt.legend(handles=[M31_ret1,M31_ret2], loc=4)
plt.legend()
plt.ylim(0,1)
#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/izol_Ic_IIc.png',dpi=90)
#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/izol_Ic_IIc.eps',dpi=90)

#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/Slika12.png',dpi=90)
#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/Slika12.eps',dpi=90)

plt.show()




###Ib IIb

M311_dir1 = mlines.Line2D([], [], color=c, markersize=15, label='Ib',linestyle = '-')
M311_dir2= mlines.Line2D([], [], color=c, markersize=15, label='IIb',linestyle = '--')
pat1_dir1 = mlines.Line2D([], [], color=c, markersize=15, label='Ia',linestyle = '-')
pat1_dir2 = mlines.Line2D([], [], color=c, markersize=15, label='IIa',linestyle = '--')


#plt.plot(T,A2_izol, c=c,linestyle = '-')
plt.plot(T,A2_M31_dir, c=c,linestyle = '-')
plt.plot(T,A2_M31_dir_daleko, c=c,linestyle = '--')
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')
plt.ylim(0, 1)

plt.legend(handles=[M311_dir1,M311_dir2], loc=4)
plt.legend()
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/testSlikeVidiSe/bezIzolacije/izol_Ib_IIb.png',dpi=90)
#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/izol_Ib_IIb.eps',dpi=90)

#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/Slika11.png',dpi=90)
#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/Slika11.eps',dpi=90)

plt.show()


###Ia IIa

#plt.plot(T,A2_izol, c=c,linestyle = '-')
plt.plot(T,A2_p_dir_daleko, c=c,linestyle = '--')
plt.plot(T,A2_p_dir, c=c,linestyle = '-')
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')
plt.ylim(0,1)

plt.legend(handles=[pat1_dir1,pat1_dir2], loc=4)
plt.legend()
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/testSlikeVidiSe/bezIzolacije/izol_Ia_IIa.png',dpi=90)
#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/izol_Ia_IIa.eps',dpi=90)

#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/Slika10.png',dpi=90)
#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/Slika10.eps',dpi=90)

plt.show()

###Ia Ib Ic
Ia = mlines.Line2D([], [], color=c, markersize=15, label='Ia',linestyle = '--')
Ib = mlines.Line2D([], [], color=c, markersize=15, label='Ib',linestyle = '-')
Ic = mlines.Line2D([], [], color=c, markersize=15, label='Ic',linestyle = '-.')
#plt.plot(T,A2_izol, c=c,linestyle = '-')
plt.plot(T,A2_M31_dir, c=c,linestyle = '-')
plt.plot(T,A2_p_dir, c=c,linestyle = '--')
plt.plot(T,A2_M31_ret, c=c,linestyle = '-.')

plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')
plt.ylim(0,1)
plt.legend(handles=[Ia,Ib,Ic], loc=4)
plt.legend()
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/testSlikeVidiSe/bezIzolacije/izol_Ia_Ib_Ic.png',dpi=90)
#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/izol_Ia_Ib_Ic.eps',dpi=90)

#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/Slika8.png',dpi=90)
#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/Slika8.eps',dpi=90)
plt.show()


#IIa IIb IIc
IIa = mlines.Line2D([], [], color=c, markersize=15, label='IIa',linestyle = '-')
IIb = mlines.Line2D([], [], color=c, markersize=15, label='IIb',linestyle = '--')
IIc = mlines.Line2D([], [], color=c, markersize=15, label='IIc',linestyle = '-.')

plt.plot(T, A2_p_dir_daleko, c=c, linestyle = '-')
plt.plot(T, A2_M31_dir_daleko, c=c, linestyle = '--')
plt.plot(T, A2_M31_ret_daleko, c=c, linestyle = '-.')
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')
plt.ylim(0, 1)

plt.legend(handles=[IIa,IIb,IIc], loc=4)
plt.legend()
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/testSlikeVidiSe/bezIzolacije/izol_IIa_IIb_IIc.png',dpi=90)
#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/izol_IIa_IIb_IIc.eps',dpi=90)

#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/Slika9.png',dpi=90)
#plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/Slika9.eps',dpi=90)
plt.show()


"""
plt.plot(T,A2_izol, c=c,linestyle = '-')
plt.plot(T,A2_M31_dir_daleko, c=c,linestyle = '-.')
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')
plt.ylim(0,1)

plt.legend(handles=[izol,pat_dir], loc=4)
plt.legend()
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/M31_dir_vs_izol_daleko.png',dpi=300)
plt.show()

plt.plot(T,A2_izol, c=c,linestyle = '-')
plt.plot(T,A2_M31_ret_daleko, c=c,linestyle = '-.')
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')

plt.legend(handles=[izol,pat_dir], loc=4)
plt.legend()
plt.ylim(0,1)
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/M31_ret_vs_izol_daleko.png',dpi=300)
plt.show()

plt.plot(T,A2_izol, c=c,linestyle = '-')
plt.plot(T,A2_p_dir_daleko, c=c,linestyle = '-.')
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')
plt.ylim(0,1)

plt.legend(handles=[izol,pat_dir], loc=4)
plt.legend()
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/P_dir_vs_izol_daleko.png',dpi=300)
plt.show()




plt.plot(T,A2_M31_dir_daleko, c=c)
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')
plt.ylim(0,1)

plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/M31_dir_daleko.png',dpi=300)
plt.show()


plt.plot(T,A2_M31_ret_daleko, c=c)
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')
plt.ylim(0,1)

plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/M31_ret_daleko.png',dpi=300)
plt.show()

plt.plot(T,A2_p_dir_daleko, c=c)
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')
plt.ylim(0,1)

plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/p_dir_daleko.png',dpi=300)
plt.show()

plt.plot(T,A2_izol, c=c)
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')
plt.ylim(0,1)

plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/izol.png',dpi=300)
plt.show()
 
plt.plot(T,A2_M31_ret, c=c)
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')
plt.ylim(0,1)

plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/M31_ret.png',dpi=300)
plt.show()


plt.plot(T,A2_M31_dir, c=c)
plt.xlabel('$T[Gyr]$')
plt.ylim(0,1)
plt.ylabel('$A_2$')

plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/M31_dir.png',dpi=300)
plt.show()


plt.plot(T,A2_p_dir, c=c)
plt.xlabel('$T[Gyr]$')
plt.ylim(0,1)
plt.ylabel('$A_2$')

plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/pat_dir.png',dpi=300)
plt.show()


plt.plot(T,A2_izol, c=c,linestyle = '-')
plt.plot(T,A2_p_dir, c=c,linestyle = '-.')
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')
plt.ylim(0,1)

plt.legend(handles=[izol,pat_dir], loc=4)
plt.legend()
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/P_dir_vs_izol.png',dpi=300)
plt.show()


plt.plot(T,A2_izol, c=c,linestyle = '-')
plt.plot(T,A2_M31_ret, c=c,linestyle = '-.')
plt.xlabel('$T[Gyr]$')
plt.ylim(0,1)
plt.ylabel('$A_2$')

plt.legend(handles=[izol,M31_ret], loc=4)
plt.legend()
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/M31_ret_vs_izol.png',dpi=300)
plt.show()


plt.plot(T,A2_izol, c=c,linestyle = '-')
plt.plot(T,A2_M31_dir, c=c,linestyle = '-.')
plt.ylim(0,1)
plt.xlabel('$T[Gyr]$')
plt.ylabel('$A_2$')

plt.legend(handles=[izol,M31_dir], loc=4)
plt.legend()
plt.savefig('C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/A2/M31_dir_vs_izol.png',dpi=300)
plt.show()
"""



"""
'best'         : 0, (only implemented for axes legends)
'upper right'  : 1,
'upper left'   : 2,
'lower left'   : 3,
'lower right'  : 4,
'right'        : 5,
'center left'  : 6,
'center right' : 7,
'lower center' : 8,
'upper center' : 9,
'center'       : 10,
"""
