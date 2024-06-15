import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fin = "BH_NS_dark_DR3.csv"
kkThDR3Data = pd.read_csv(fin, header=0)

fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(111)
plt.grid(False)
ax.set_xscale('log', base=10)
# ax.set_yscale('linear')

plt.xlim(4.4*10**(-1),1.2*10.**1)
# plt.ylim(-5, 400)

ax.add_patch(Rectangle((2.8*10**(-1), 269.-25.), (2.5*10.**2-2.8*10**(-1)), 2*25,
             facecolor = 'lightcoral',
             fill=True,
             alpha = 0.6,
             label="Hobbs et al. (2005)"))

ax.add_patch(Rectangle(((6.03-1.04)*10**0, 37.61-5.13), ((1.04+1.19)*10**0), 5.13+5.12,
             facecolor = 'cornflowerblue',
             fill=True,
             alpha = 0.7,
             label="Lam & Lu (2023)",
             zorder=11))
             
plt.axhline(y=269., lw=3, color='brown', zorder=5)


# plt.axhline(y=43.4, lw=3, color='firebrick', zorder=5)

ax.tick_params(axis='both', which='major', labelsize=16)
# plt.yticks([10**0, 10**1, 10**2], [1,10,100])

for i in range(len(kkThDR3Data["ML"])):
    if(kkThDR3Data["transverse_vel"].values[i] != "--"):
        mass = kkThDR3Data["ML"].values[i]
        mass_err = [[kkThDR3Data["err_ML_mn"].values[i]], [kkThDR3Data["err_ML_pl"].values[i]]]
    # #
        vt = float(kkThDR3Data["transverse_vel"].values[i])
        vt_err = [[float(kkThDR3Data["err_vt_mn"].values[i])], [float(kkThDR3Data["err_vt_pl"].values[i])]]
    # #
        #print(kkThDR3Data["event"].values[i], mass, mass_err, vt, vt_err)
    # #
        thwork = ax.errorbar(mass, vt, xerr=mass_err, yerr=vt_err,
                         c='black',  marker='o', markersize=10, zorder=10, ls='-')
#
thwork = ax.errorbar(-1.0, -1.0, xerr=0.0001, yerr=0.0001,
                     c='black',  marker='o', markersize=10, zorder=10, ls='-', label='This work')

plt.xlabel(r'$M_L$ [$M_\odot$]', fontsize=26)
plt.ylabel(r'$v_{t,L}$ [km/s]', fontsize=26)
ax.tick_params(axis='both', which='major', labelsize=20)
plt.legend(loc='best', fontsize=20)
plt.savefig("gdr3_dark_transvels.pdf", dpi=150, format='pdf')
plt.show()
