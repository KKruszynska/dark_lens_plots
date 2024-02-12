import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fin = "/home/kasia/Documents/PhD/Thesis/Summary/gdr3_darkmass_transverse_vels.csv"
kkThDR3Data = pd.read_csv(fin, header=0, comment="#")

fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(111)
plt.grid(False)
ax.set_xscale('log', base=10)
# ax.set_yscale('linear')

plt.xlim(4.4*10**(-1),1.2*10.**1)
# plt.ylim(-5, 400)

ax.add_patch(Rectangle((2.8*10**(-1), 269.-25.), (2.5*10.**2-2.8*10**(-1)), 2*25,
             facecolor = 'cornflowerblue',
             fill=True,
             alpha = 0.6,
             label="Hobbs et al. (2005)"))
             
plt.axhline(y=269., lw=3, color='navy', zorder=5)

ax.add_patch(Rectangle(((6.03-1.04)*10**0, 37.61-5.13), ((1.04+1.19)*10**0), 5.13+5.12,
             facecolor = 'red',
             fill=True,
             alpha = 0.6,
             label="Lam et al. (2023)"))
# plt.axhline(y=43.4, lw=3, color='firebrick', zorder=5)

ax.tick_params(axis='both', which='major', labelsize=16)
# plt.yticks([10**0, 10**1, 10**2], [1,10,100])

for i in range(len(kkThDR3Data["mass"])):
# #
    mass = kkThDR3Data["mass"].values[i]
    mass_err = [[kkThDR3Data["error_mn"].values[i]], [kkThDR3Data["error_pl"].values[i]]]
# #
    vt = kkThDR3Data["vt"].values[i]
    vt_err = [[kkThDR3Data["err_mn"].values[i]], [kkThDR3Data["err_pl"].values[i]]]
# #
    print(kkThDR3Data["event"].values[i], mass, mass_err, vt, vt_err)
# #
    thwork = ax.errorbar(mass, vt, xerr=mass_err, yerr=vt_err,
                     c='black',  marker='o', markersize=10, zorder=10, ls='-')

plt.xlabel(r'$M_L$ [$M_\odot$]', fontsize=26)
plt.ylabel(r'$v_{t,L}$ [km/s]', fontsize=26)
ax.tick_params(axis='both', which='major', labelsize=20)
plt.legend(loc='best', fontsize=20)
plt.savefig("masses_transvels_gdr3_dark_fin.pdf", dpi=150, format='pdf')
plt.show()
