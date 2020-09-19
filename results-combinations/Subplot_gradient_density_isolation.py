import numpy as np
import matplotlib.pyplot as plt
import math as math


putanja_load = "C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/M31_izolacija/gradijent/1FI_RO_"
putanja_sacuvaj = "C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/Gradijenti_gustine/"


ugao_0, gradijent_0 = np.loadtxt(putanja_load + str(0).zfill(3) + ".txt", unpack = True)
ugao_50, gradijent_50 = np.loadtxt(putanja_load + str(50).zfill(3) + ".txt", unpack = True)
ugao_100, gradijent_100 = np.loadtxt(putanja_load + str(100).zfill(3) + ".txt", unpack = True)



# 3 in row
f, axarr = plt.subplots(1, 3, figsize=(20, 4))
f.subplots_adjust(hspace=0.2, wspace = 0.2, left = 0.05, right=0.95, bottom = 0.15 , top = 0.9)


axarr[0].plot(ugao_0,gradijent_0,c='black')
axarr[0].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
axarr[0].set_ylabel(r'$\Delta\rho [ 10^7 M_dot/kpc^2]$',fontsize=16)
axarr[0].set_xlim(0,360)

#axarr[0, 0].set_xlabel("dd")
#axarr[0, 0].set_title('Axis [0,0]')
axarr[1].plot(ugao_50,gradijent_50,c='black')
axarr[1].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
axarr[1].set_xlim(0,360)

#axarr[0, 1].set_title('Axis [0,1]')
axarr[2].plot(ugao_50,gradijent_50,c='black')
axarr[2].set_xlabel(r'$\alpha$ [ $^\circ$ ]',fontsize=16)
axarr[2].set_xlim(0,360)

#axarr[1, 0].set_title('Axis [1,0]')
#axarr[1, 1].scatter(x, y ** 2)
#axarr[1, 1].set_title('Axis [1,1]')
# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
#plt.setp([a.get_xticklabels() for a in axarr[:]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[1:3]], visible=False)
plt.savefig(putanja_sacuvaj + "izolacija_graijent_sub3",dpi=90)
plt.savefig(putanja_sacuvaj + "izolacija_graijent_sub3.eps",dpi=90)
plt.show()