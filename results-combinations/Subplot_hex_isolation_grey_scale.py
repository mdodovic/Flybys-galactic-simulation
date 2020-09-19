"""
hexbin is an axes method or pyplot function that is essentially
a pcolor of a 2-D histogram with hexagonal cells.  It can be
much more informative than a scatter plot; in the first subplot
below, try substituting 'scatter' for 'hexbin'.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20) 

putanja_disk_i = "C:/Users/matij/Desktop/M31_izolacija/txt/DBH2/disk_"
putanja_sacuvaj = "C:/Users/matij/Desktop/Kodovi_za_analizu/rezultati/Mape_xy/"
M0,X0,Y0,Z0,VX0,VY0,VZ0 = np.loadtxt(putanja_disk_i + str(0).zfill(3) + ".txt", unpack = True)
M50,X50,Y50,Z50,VX50,VY50,VZ50 = np.loadtxt(putanja_disk_i + str(50).zfill(3) + ".txt", unpack = True)
M100,X100,Y100,Z100,VX100,VY100,VZ100 = np.loadtxt(putanja_disk_i + str(100).zfill(3) + ".txt", unpack = True)

"""
left  = 0.125  # the left side of the subplots of the figure
right = 0.9    # the right side of the subplots of the figure
bottom = 0.1   # the bottom of the subplots of the figure
top = 0.9      # the top of the subplots of the figure
wspace = 0.2   # the amount of width reserved for space between subplots,
               # expressed as a fraction of the average axis width
hspace = 0.2   # the amount of height reserved for space between subplots,
               # expressed as a fraction of the average axis height
"""
lim = 34
grid=100
labelPad = 30 #ose X[kpc] ... i to koliko je odmaknuto
ticksPad = 15 #koliko su same brojke -30 -20 ... odmaknute
labelAxesSize = 30 #velicina brojki -30 -20 ...
fig, axs = plt.subplots(ncols=3, sharey=True, figsize=(40, 10))
fig.subplots_adjust(left=0.045, right=0.985, bottom = 0.175, wspace = 0.0)
#fig.subplots_adjust(left=0.040, right=0.93)
ax = axs[0]
hb = ax.hexbin(X0, Y0, gridsize=grid, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])

ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)

ax.set_xlabel('$X$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
ax.set_ylabel('$Y$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
cb = fig.colorbar(hb, ax=ax)

ax = axs[1]
hb = ax.hexbin(X50, Y50, gridsize=grid, bins='log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
ax.set_xlabel('$X$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
cb = fig.colorbar(hb, ax=ax)

ax = axs[2]
hb = ax.hexbin(X100, Y100, gridsize=grid, bins = 'log', cmap='gray')
ax.axis([-lim, lim, -lim, lim])
ax.tick_params(axis = 'x', pad = ticksPad)
ax.tick_params(axis = 'y', pad = ticksPad)
ax.set_xlabel('$X$' + ' [kpc]',size = labelAxesSize, labelpad = labelPad)
cb = fig.colorbar(hb, ax=ax)
cb.set_label('log $N$', size = labelAxesSize, labelpad = labelPad)






plt.savefig(putanja_sacuvaj + "izolacija_3.png", dpi = 90 )
plt.savefig(putanja_sacuvaj + "izolacija_3.eps", dpi = 90 )
plt.savefig("C:/Users/matij/Desktop/Kodovi_za_analizu/SlikeRad/slika13.eps", dpi = 90 )
plt.show()