import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerTuple

fin = "BH_NS_GWaves.csv"
gwData = pd.read_csv(fin, header=0)

fin = "BH_NS_XRB.csv"
xrbData = pd.read_csv(fin, header=0)

fin = "BH_NS_ulens.csv"
ulensData = pd.read_csv(fin, header=0, comment="#")

fin = "NS_Antoniadis.csv"
nsData = pd.read_csv(fin, header=0, comment="#")

fin = "non_interacting.csv"
noniData = pd.read_csv(fin, header=0, comment="#")

fin = "BH_NS_dark_DR3.csv"
# fin = "BH_NS_KKThesis_DR3_xshooter.csv"
kkThDR3Data = pd.read_csv(fin, header=0)

fin = "2021_gentille-fusillo_wd_cat_masses.csv"
wdMass = pd.read_csv(fin, header=0)

fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(111)
plt.grid(False)
ax.set_xscale('log', base=10)
ax.set_yscale('log', base=10)

plt.xlabel(r'Mass [$M_\odot$]', fontsize=16)
plt.ylabel(r'Number', fontsize=16)

plt.xlim(5.*10**(-1),2.*10.**2)
# plt.xlim(-5, 465)

ax.tick_params(axis='both', which='major', labelsize=16)
# ax.xaxis.set_ticklabels([])
plt.xticks([10**0, 10**1, 10**2], [1,10,100])
bins = np.logspace(np.log10(5*10**(-1)), np.log10(2*10.**2), num=50)

mH = wdMass["MassH"].values[:]
mHe = wdMass["MassHe"].values[:]
mall = np.hstack((mH, mHe))

massWD = plt.hist(mall, bins=bins, alpha=0.6, histtype='stepfilled', color='plum', edgecolor='mediumvioletred', zorder=0, label="WD")

m1 = gwData["mass_1_source"].values[:]
m2 = gwData["mass_2_source"].values[:]
m_fin = gwData["final_mass_source"].values[:]
m_prim = np.hstack((m1, m2))


m1 = nsData["Mass"].values[:]
massNS = plt.hist(m1, bins=bins, alpha=0.6, histtype='stepfilled', edgecolor='brown', color='lightcoral', label="NS")

massGWs_prim = plt.hist(m_prim, bins=bins, alpha=0.6, histtype='stepfilled', edgecolor='goldenrod', color='gold', label="GW binary")
massGWs_fin = plt.hist(m_fin, bins=bins, alpha=0.6, histtype='stepfilled', edgecolor='darkslategrey', color='grey', label="GW final")

m1 = xrbData["mass"].values[:]
massXRBs = plt.hist(m1, bins=bins, alpha=0.6, histtype='stepfilled', edgecolor='maroon',  color='firebrick', label="HMXRB")

m1 = ulensData["mass"].values[:]
massUlens = plt.hist(m1, bins=bins, alpha=0.6, histtype='stepfilled', edgecolor='navy', color='cornflowerblue', label="Microlensing")

# colors = ["lightcoral", "sandybrown", "darkkhaki", "mediumaquamarine", "darkcyan", "slateblue"]

# m1 = kkThDR3Data["M_L"].values[:]
# kkDR3mass = plt.hist(m1, bins=bins, alpha=0.6, histtype='stepfilled', color='black', label="This work")

m1 = noniData["Mass"].values[:]
massNoni = plt.hist(m1, bins=bins, alpha=0.6, histtype='stepfilled', color='darkgreen', edgecolor='black', label="Non-interacting")

for i in range(len(kkThDR3Data["ML"])):
    shift = 1.5 + i*1.22
    if(kkThDR3Data["#GaiaDR3-ULENS"].values[i][-1] == "+"):
        marker = "o"
    else:
        marker = "d"
    m1 = kkThDR3Data["ML"].values[i]
    m1_err = [[kkThDR3Data["err_ML_mn"].values[i]], [kkThDR3Data["err_ML_pl"].values[i]]]

    kkDR3 = ax.errorbar(m1, shift, xerr=m1_err, c='black', marker=marker, markersize=8, zorder=14)
#
m1 = -1
m1_err = [[kkThDR3Data["err_ML_mn"].values[0]], [kkThDR3Data["err_ML_pl"].values[0]]]
kkDR31 = ax.errorbar(m1, -1, xerr=m1_err, c='black', marker='o', markersize=8, zorder=14)
kkDR32 = ax.errorbar(m1, -1, xerr=m1_err, c='black', marker='d', markersize=8, zorder=14)

# for i in range(len(kkThDR3Data["mass"])):
#     shift = 1. + i*0.22
#     m1 = kkThDR3Data["mass"].values[i]
#     m1_err = [[kkThDR3Data["error_mn"].values[i]], [kkThDR3Data["error_pl"].values[i]]]
#
#     kkDR3 = ax.errorbar(m1, shift, xerr=m1_err, c='black', marker='o', markersize=5, zorder=14)
#     # ax.annotate(kkThDR3Data["event"].values[i], (m1, shift+0.4), fontsize=14)
#
# m1 = kkThDR3Data["mass"].values[0]
# m1_err = [[kkThDR3Data["error_mn"].values[0]], [kkThDR3Data["error_pl"].values[0]]]
# kkDR3 = ax.errorbar(m1, 1, xerr=m1_err, c='black', marker='o', markersize=5, zorder=14, label = "Dark lens candidates")

plt.axvline(x=1.4, ls = '--', color='black')
plt.axvline(x=2.1, ls = '--', color='black')
plt.axvline(x=5., ls = '-', color='grey')
plt.axvline(x=40., ls = '--', color='black')
plt.axvline(x=90., ls = '--', color='black')

plt.text(3.5, 1.5*10.**2,'1st mass-gap', fontsize=16, rotation=90, rotation_mode='anchor')
plt.text(64, 1.5*10.**2,'2nd mass-gap', fontsize=16, rotation=90, rotation_mode='anchor')

ax.tick_params(axis='both', which='major', labelsize=20)
# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# plt.legend([(primary,final), xrb, ulens, noni, ns1, ns2, ns3, ns4, ns5, ns6],["GW", "HMXB", "Microlensing", "Non-interacting", "LMXB", "Eclipsing MSP", "NS-NS binaries", "NS-WD binaries", "MSP-MS binaries", "MSP in a triple system"], fontsize=16, handler_map={tuple: HandlerTuple(ndivide=None)}, bbox_to_anchor=(1, 0.5), loc='center left')
#PL
# plt.legend([(primary,final), xrb, ulens, noni, ns1, ns2, ns3, ns4, ns5, ns6],["GW", "HMXB", "Mikrosoczewkowanie", "Układy z\nnieoddziałującymi\nobiektami", "LMXB", "Układy zaćmieniowe PM", "Układy podwójne NS-NS", "Układy podwójne NS-WD", "Układy podwójne PM-MS", "PM w układzie potrójnym"], fontsize=16, handler_map={tuple: HandlerTuple(ndivide=None)}, bbox_to_anchor=(1, 0.5), loc='center left')

# plt.legend([massGWs, massXRBs, massNS, massNoni, massUlens],
#            ["GW", "HMXB", "NS (different methods)", "Non-interacting", "Microlensing"],
#            fontsize=16, handler_map={tuple: HandlerTuple(ndivide=None)}, bbox_to_anchor=(1, 0.5), loc='center left')

# plt.legend(fontsize=18, bbox_to_anchor=(1, 0.5), loc='center left')
handles, labels = ax.get_legend_handles_labels()
handles.append((kkDR31, kkDR32))
labels.append("This work")
plt.legend(handles=handles, labels=labels, fontsize=18, bbox_to_anchor=(1, 0.5), loc='center left',
           handler_map={tuple: HandlerTuple(ndivide=None)})

#PL
#plt.legend([kkDR3, (primary,final), xrb, ulens, noni, ns1, ns2, ns3, ns4, ns5, ns6],["Ta praca", "GW", "HMXB", "Mikrosoczewkowanie", "Układy z\nnieoddziałującymi\nobiektami", "LMXB", "Układy zaćmieniowe PM", "Układy podwójne NS-NS", "Układy podwójne NS-WD", "Układy podwójne PM-MS", "PM w układzie potrójnym"], fontsize=16, handler_map={tuple: HandlerTuple(ndivide=None)}, bbox_to_anchor=(1, 0.5), loc='center left')

# plt.legend([(primary,final)],["GW"], fontsize=16, handler_map={tuple: HandlerTuple(ndivide=None)}, bbox_to_anchor=(1, 0.5), loc='center left')
# plt.legend([xrb, ns1 ],["HMXB", "LMXB"], fontsize=16, handler_map={tuple: HandlerTuple(ndivide=None)}, bbox_to_anchor=(1, 0.5), loc='center left')
# plt.legend([ns2, ns3, ns4, ns5, ns6, ],["Eclipsing MSP", "NS-NS binaries", "NS-WD binaries", "MSP-MS binaries", "MSP in a triple system"], fontsize=16, handler_map={tuple: HandlerTuple(ndivide=None)}, bbox_to_anchor=(1, 0.5), loc='center left')
# plt.legend([ulens],["Microlensing"], fontsize=16, handler_map={tuple: HandlerTuple(ndivide=None)}, bbox_to_anchor=(1, 0.5), loc='center left')
# plt.legend([noni],["Non-interacting"], fontsize=16, handler_map={tuple: HandlerTuple(ndivide=None)}, bbox_to_anchor=(1, 0.5), loc='center left')

plt.ylim(10**0, 10**5)

plt.savefig("masses_hist_dark.pdf", dpi=150, format='pdf')
plt.show()

