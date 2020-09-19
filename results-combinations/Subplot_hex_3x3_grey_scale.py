"""
hexbin is an axes method or pyplot function that is essentially
a pcolor of a 2-D histogram with hexagonal cells.  It can be
much more informative than a scatter plot; in the first subplot
below, try substituting 'scatter' for 'hexbin'.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


putanja_sacuvaj = "C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/Mape_xy/"

putanja_disk_Ia = "C:/Users/matij/Desktop/Patuljak_direktna_blizu/txt/DBHSB2/disk_"
putanja_disk_Ib = "C:/Users/matij/Desktop/M31_direktna_blizu/txt/DBHSB2/disk_"
putanja_disk_Ic = "C:/Users/matij/Desktop/M31_retrogradna_blizu/txt/DBHSB2/disk_"


M0Ia,X0Ia,Y0Ia,Z0Ia,VX0Ia,VY0Ia,VZ0Ia = np.loadtxt(putanja_disk_Ia + str(0).zfill(3) + ".txt", unpack = True)
M50Ia,X50Ia,Y50Ia,Z50Ia,VX50Ia,VY50Ia,VZ50Ia = np.loadtxt(putanja_disk_Ia + str(26).zfill(3) + ".txt", unpack = True)
M100Ia,X100Ia,Y100Ia,Z100Ia,VX100Ia,VY100Ia,VZ100Ia = np.loadtxt(putanja_disk_Ia + str(36).zfill(3) + ".txt", unpack = True)

M0Ib,X0Ib,Y0Ib,Z0Ib,VX0Ib,VY0Ib,VZ0Ib = np.loadtxt(putanja_disk_Ib + str(0).zfill(3) + ".txt", unpack = True)
M50Ib,X50Ib,Y50Ib,Z50Ib,VX50Ib,VY50Ib,VZ50Ib = np.loadtxt(putanja_disk_Ib + str(14).zfill(3) + ".txt", unpack = True)
M100Ib,X100Ib,Y100Ib,Z100Ib,VX100Ib,VY100Ib,VZ100Ib = np.loadtxt(putanja_disk_Ib + str(21).zfill(3) + ".txt", unpack = True)

M0Ic,X0Ic,Y0Ic,Z0Ic,VX0Ic,VY0Ic,VZ0Ic = np.loadtxt(putanja_disk_Ic + str(0).zfill(3) + ".txt", unpack = True)
M50Ic,X50Ic,Y50Ic,Z50Ic,VX50Ic,VY50Ic,VZ50Ic = np.loadtxt(putanja_disk_Ic + str(50).zfill(3) + ".txt", unpack = True)
M100Ic,X100Ic,Y100Ic,Z100Ic,VX100Ic,VY100Ic,VZ100Ic = np.loadtxt(putanja_disk_Ic + str(100).zfill(3) + ".txt", unpack = True)


lim = 34
grid=100

labelPad = 30
labelAxesSize = 50
ticksPad = 15 #koliko su same brojke -30 -20 ... odmaknute

leftAll  = 0.06  # the left side of the subplots of the figure
rightAll = 0.97    # the right side of the subplots of the figure
bottomAll = 0.03   # the bottom of the subplots of the figure
topAll = 0.97      # the top of the subplots of the figure
wspaceAll = 0.1   # the amount of width reserved for space between subplots,
               # expressed as a fraction of the average axis width
hspaceAll = 0.1   # the amount of height reserved for space between subplots,
               # expressed as a fraction of the average axis height


matplotlib.rc('xtick', labelsize = 40) 
matplotlib.rc('ytick', labelsize = 40) 


fig, axs = plt.subplots(ncols=3, nrows = 3, sharey=True, figsize=(50,50))
fig.subplots_adjust( left=leftAll, right=rightAll, wspace = wspaceAll, hspace=hspaceAll)
#fig.subplots_adjust(left=0.045, right=0.985, bottom = 0.175, wspace = 0.0)

ax = axs[0,0]
hb = ax.hexbin(X0Ia, Y0Ia, gridsize=grid, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
ax.set_ylabel('$Y$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
cb = fig.colorbar(hb, ax=ax)

ax = axs[0,1]
hb = ax.hexbin(X50Ia, Y50Ia, gridsize=grid, bins='log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
cb = fig.colorbar(hb, ax=ax)

ax = axs[0,2]
hb = ax.hexbin(X100Ia, Y100Ia, gridsize=grid, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
cb = fig.colorbar(hb, ax=ax)
cb.set_label('log $N$', size = labelAxesSize, labelpad = labelPad)



ax = axs[1,0]
hb = ax.hexbin(X0Ib, Y0Ib, gridsize=grid, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
ax.set_ylabel('$Y$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
cb = fig.colorbar(hb, ax=ax)

ax = axs[1,1]
hb = ax.hexbin(X50Ib, Y50Ib, gridsize=grid, bins='log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
cb = fig.colorbar(hb, ax=ax)

ax = axs[1,2]
hb = ax.hexbin(X100Ib, Y100Ib, gridsize=grid*2, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
cb = fig.colorbar(hb, ax=ax)
cb.set_label('log $N$', size = labelAxesSize, labelpad = labelPad)

ax = axs[2,0]
hb = ax.hexbin(X0Ic, Y0Ic, gridsize=grid, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
ax.set_xlabel('$X$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
ax.set_ylabel('$Y$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
cb = fig.colorbar(hb, ax=ax)

ax = axs[2,1]
hb = ax.hexbin(X50Ic, Y50Ic, gridsize=grid, bins='log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
ax.set_xlabel('$X$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
cb = fig.colorbar(hb, ax=ax)

ax = axs[2,2]
hb = ax.hexbin(X100Ic, Y100Ic, gridsize=grid, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.set_xlabel('$X$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
cb = fig.colorbar(hb, ax=ax)
cb.set_label('log $N$', size = labelAxesSize, labelpad = labelPad)

plt.savefig(putanja_sacuvaj + "I_9.png", dpi = 90 )
plt.savefig(putanja_sacuvaj + "I_9.eps", dpi = 90 )
plt.savefig("C:/Users/matij/Desktop/Kodovi_za_analizu/SlikeRad/slika14.eps", dpi = 90 )
plt.show()

putanja_disk_IIa = "C:/Users/matij/Desktop/Patuljak_direktna/txt/DBHSB2/disk_"
putanja_disk_IIb = "E:/BLISKI_PROLAZ/M31_direktna/txt/DBHSB2/disk_"
putanja_disk_IIc = "E:/BLISKI_PROLAZ/M31_retrogradna/txt/DBHSB2/disk_"

M0IIa,X0IIa,Y0IIa,Z0IIa,VX0IIa,VY0IIa,VZ0IIa = np.loadtxt(putanja_disk_IIa + str(0).zfill(3) + ".txt", unpack = True)
M50IIa,X50IIa,Y50IIa,Z50IIa,VX50IIa,VY50IIa,VZ50IIa = np.loadtxt(putanja_disk_IIa + str(50).zfill(3) + ".txt", unpack = True)
M100IIa,X100IIa,Y100IIa,Z100IIa,VX100IIa,VY100IIa,VZ100IIa = np.loadtxt(putanja_disk_IIa + str(100).zfill(3) + ".txt", unpack = True)

M0IIb,X0IIb,Y0IIb,Z0IIb,VX0IIb,VY0IIb,VZ0IIb = np.loadtxt(putanja_disk_IIb + str(0).zfill(3) + ".txt", unpack = True)
M50IIb,X50IIb,Y50IIb,Z50IIb,VX50IIb,VY50IIb,VZ50IIb = np.loadtxt(putanja_disk_IIb + str(50).zfill(3) + ".txt", unpack = True)
M100IIb,X100IIb,Y100IIb,Z100IIb,VX100IIb,VY100IIb,VZ100IIb = np.loadtxt(putanja_disk_IIb + str(100).zfill(3) + ".txt", unpack = True)

M0IIc,X0IIc,Y0IIc,Z0IIc,VX0IIc,VY0IIc,VZ0IIc = np.loadtxt(putanja_disk_IIc + str(0).zfill(3) + ".txt", unpack = True)
M50IIc,X50IIc,Y50IIc,Z50IIc,VX50IIc,VY50IIc,VZ50IIc = np.loadtxt(putanja_disk_IIc + str(50).zfill(3) + ".txt", unpack = True)
M100IIc,X100IIc,Y100IIc,Z100IIc,VX100IIc,VY100IIc,VZ100IIc = np.loadtxt(putanja_disk_IIc + str(100).zfill(3) + ".txt", unpack = True)


lim = 34
grid=100

fig, axs = plt.subplots(ncols=3, nrows = 3, sharey=True, figsize=(50,50))
fig.subplots_adjust( left=leftAll, right=rightAll, wspace = wspaceAll, hspace=hspaceAll)

ax = axs[0,0]
hb = ax.hexbin(X0IIa, Y0IIa, gridsize=grid, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
ax.set_ylabel('$Y$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
cb = fig.colorbar(hb, ax=ax)

ax = axs[0,1]
hb = ax.hexbin(X50IIa, Y50IIa, gridsize=grid, bins='log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
cb = fig.colorbar(hb, ax=ax)

ax = axs[0,2]
hb = ax.hexbin(X100IIa, Y100IIa, gridsize=grid, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
cb = fig.colorbar(hb, ax=ax)
cb.set_label('log $N$', size = labelAxesSize, labelpad = labelPad)



ax = axs[1,0]
hb = ax.hexbin(X0IIb, Y0IIb, gridsize=grid, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
ax.set_ylabel('$Y$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
cb = fig.colorbar(hb, ax=ax)

ax = axs[1,1]
hb = ax.hexbin(X50IIb, Y50IIb, gridsize=grid, bins='log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
cb = fig.colorbar(hb, ax=ax)


ax = axs[1,2]
hb = ax.hexbin(X100IIb, Y100IIb, gridsize=grid, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
cb = fig.colorbar(hb, ax=ax)
cb.set_label('log $N$', size = labelAxesSize, labelpad = labelPad)

ax = axs[2,0]
hb = ax.hexbin(X0IIc, Y0IIc, gridsize=grid, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
ax.set_xlabel('$X$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
ax.set_ylabel('$Y$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
cb = fig.colorbar(hb, ax=ax)

ax = axs[2,1]
hb = ax.hexbin(X50IIc, Y50IIc, gridsize=grid, bins='log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
ax.set_xlabel('$X$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
cb = fig.colorbar(hb, ax=ax)

ax = axs[2,2]
hb = ax.hexbin(X100IIc, Y100IIc, gridsize=grid, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
ax.set_xlabel('$X$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
cb = fig.colorbar(hb, ax=ax)
cb.set_label('log $N$', size = labelAxesSize, labelpad = labelPad)

plt.savefig(putanja_sacuvaj + "II_9.png", dpi = 90 )
plt.savefig(putanja_sacuvaj + "II_9.eps", dpi = 90 )
plt.savefig("C:/Users/matij/Desktop/Kodovi_za_analizu/SlikeRad/slika15.eps", dpi = 90 )
plt.show()
