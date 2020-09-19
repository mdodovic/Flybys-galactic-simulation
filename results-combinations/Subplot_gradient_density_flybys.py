import numpy as np
import matplotlib.pyplot as plt
import math as math

putanja_sacuvaj = "C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/Gradijenti_gustine/"

#I slucaj
putanja_load_Ia = "C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/Patuljak_M31_direktna/gradijent/1FI_RO_"
putanja_load_Ib = "C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/M31_M31_direktna/gradijent/1FI_RO_"



ugao_0Ia, gradijent_0Ia = np.loadtxt(putanja_load_Ia + str(0).zfill(3) + ".txt", unpack = True)
ugao_48, gradijent_48 = np.loadtxt(putanja_load_Ia + str(50).zfill(3) + ".txt", unpack = True)
ugao_95, gradijent_95 = np.loadtxt(putanja_load_Ia + str(100).zfill(3) + ".txt", unpack = True)

ugao_0Ib, gradijent_0Ib = np.loadtxt(putanja_load_Ib + str(0).zfill(3) + ".txt", unpack = True)
ugao_9, gradijent_9 = np.loadtxt(putanja_load_Ib + str(50).zfill(3) + ".txt", unpack = True)
ugao_11, gradijent_11 = np.loadtxt(putanja_load_Ib + str(100).zfill(3) + ".txt", unpack = True)


# 3 in row
#f, axarr = plt.subplots(2, 3, figsize=(20, 4))

f, axarr = plt.subplots(2, 3, figsize=(16,8))
f.subplots_adjust(hspace=0.5, wspace = 0.2, left = 0.05, right=0.95, bottom = 0.15 , top = 0.9)

axarr[0,0].plot(ugao_0Ia,gradijent_0Ia,c='black')
#axarr[0,0].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
axarr[0,0].set_ylabel(r'$\Delta\rho [ 10^7 Msol/kpc^2]$',fontsize=16)
axarr[0,0].set_xlim(0,360)


axarr[0,1].plot(ugao_48,gradijent_48,c='black')
#axarr[0,1].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
#axarr[0,1].set_ylabel(r'$\Delta\rho [ 10^7 Msol/kpc^2]$',fontsize=16)
axarr[0,1].set_xlim(0,360)

axarr[0,2].plot(ugao_95,gradijent_95,c='black')
#axarr[0,2].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
#axarr[0,2].set_ylabel(r'$\Delta\rho [ 10^7 Msol/kpc^2]$',fontsize=16)
axarr[0,2].set_xlim(0,360)


axarr[1,0].plot(ugao_0Ib,gradijent_0Ib,c='black')
axarr[1,0].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
axarr[1,0].set_ylabel(r'$\Delta\rho [ 10^7 Msol/kpc^2]$',fontsize=16)
axarr[1,0].set_xlim(0,360)


axarr[1,1].plot(ugao_9,gradijent_9,c='black')
axarr[1,1].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
#axarr[1,1].set_ylabel(r'$\Delta\rho [ 10^7 Msol/kpc^2]$',fontsize=16)
axarr[1,1].set_xlim(0,360)

axarr[1,2].plot(ugao_11,gradijent_11,c='black')
axarr[1,2].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
#axarr[1,2].set_ylabel(r'$\Delta\rho [ 10^7 Msol/kpc^2]$',fontsize=16)
axarr[1,2].set_xlim(0,360)

# Fine-tune figure; hide x ticks for top plots and y ticks for right plots

#plt.setp([a.get_xticklabels() for a in axarr[:]], visible=False)
#plt.setp([a.get_yticklabels() for a in axarr[:,1]], visible=False)
#plt.setp([a.get_yticklabels() for a in axarr[:,2]], visible=False)

plt.savefig(putanja_sacuvaj + "Ia_Ib_sub6",dpi=90)
plt.savefig(putanja_sacuvaj + "Ia_Ib_sub6.eps",dpi=90)

plt.show()


#II slucaj

putanja_load_IIa = "C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/Patuljak_M31_direktna_daleki_bp/gradijent/1FI_RO_"
putanja_load_IIb = "C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/M31_M31_direktna_daleki_bp/gradijent/1FI_RO_"



ugao_1IIa, gradijent_1IIa = np.loadtxt(putanja_load_IIa + str(0).zfill(3) + ".txt", unpack = True)
ugao_42, gradijent_42 = np.loadtxt(putanja_load_IIa + str(50).zfill(3) + ".txt", unpack = True)
ugao_61, gradijent_61 = np.loadtxt(putanja_load_IIa + str(100).zfill(3) + ".txt", unpack = True)

ugao_1IIb, gradijent_1IIb = np.loadtxt(putanja_load_IIb + str(0).zfill(3) + ".txt", unpack = True)
ugao_41, gradijent_41 = np.loadtxt(putanja_load_IIb + str(50).zfill(3) + ".txt", unpack = True)
ugao_96, gradijent_96 = np.loadtxt(putanja_load_IIb + str(100).zfill(3) + ".txt", unpack = True)


# 3 in row
#f, axarr = plt.subplots(2, 3, figsize=(20, 4))

f, axarr = plt.subplots(2, 3, figsize=(16,8))
f.subplots_adjust(hspace=0.5, wspace = 0.2, left = 0.05, right=0.95, bottom = 0.15 , top = 0.9)

axarr[0,0].plot(ugao_1IIa,gradijent_1IIa,c='black')
#axarr[0,0].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
axarr[0,0].set_ylabel(r'$\Delta\rho [ 10^7 Msol/kpc^2]$',fontsize=16)
axarr[0,0].set_xlim(0,360)


axarr[0,1].plot(ugao_42,gradijent_42,c='black')
#axarr[0,1].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
#axarr[0,1].set_ylabel(r'$\Delta\rho [ 10^7 Msol/kpc^2]$',fontsize=16)
axarr[0,1].set_xlim(0,360)

axarr[0,2].plot(ugao_61,gradijent_61,c='black')
#axarr[0,2].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
#axarr[0,2].set_ylabel(r'$\Delta\rho [ 10^7 Msol/kpc^2]$',fontsize=16)
axarr[0,2].set_xlim(0,360)


axarr[1,0].plot(ugao_1IIb,gradijent_1IIb,c='black')
axarr[1,0].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
axarr[1,0].set_ylabel(r'$\Delta\rho [ 10^7 Msol/kpc^2]$',fontsize=16)
axarr[1,0].set_xlim(0,360)


axarr[1,1].plot(ugao_41,gradijent_41,c='black')
axarr[1,1].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
#axarr[1,1].set_ylabel(r'$\Delta\rho [ 10^7 Msol/kpc^2]$',fontsize=16)
axarr[1,1].set_xlim(0,360)

axarr[1,2].plot(ugao_96,gradijent_96,c='black')
axarr[1,2].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
#axarr[1,2].set_ylabel(r'$\Delta\rho [ 10^7 Msol/kpc^2]$',fontsize=16)
axarr[1,2].set_xlim(0,360)

# Fine-tune figure; hide x ticks for top plots and y ticks for right plots

#plt.setp([a.get_xticklabels() for a in axarr[:]], visible=False)
#plt.setp([a.get_yticklabels() for a in axarr[:,1]], visible=False)
#plt.setp([a.get_yticklabels() for a in axarr[:,2]], visible=False)

plt.savefig(putanja_sacuvaj + "IIa_IIb_sub6",dpi=90)
plt.savefig(putanja_sacuvaj + "IIa_IIb_sub6.eps",dpi=90)

plt.show()
