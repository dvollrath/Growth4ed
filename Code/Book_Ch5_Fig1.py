from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['Times New Roman']
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'

import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as pr # pull in common productivity functions

#############################################
## Set up problem
#############################################
phi = 0
lam = 1
theta = .1
gL = .02
sR = 1
L0 = 1
A0 = 1

#############################################
## Calculate solutions
#############################################
r = pr.romer(phi,lam,theta,sR,gL,A0,L0,1) # call to find s.s. ratio of L/A
L = np.arange(.5*r["LA_ss"],1.5*r["LA_ss"],.01) # range of L to create variation in A/L ratio

r = pr.romer(phi,lam,theta,sR,gL,A0,L,1) # call for all the values of L

#############################################
## Create figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot(r["LA"], r["gA"], lw=3, color='black') # plot growth rate of A
ax.plot([min(L),max(L)],[r["gA_ss"],r["gA_ss"]],lw=3,color='black',linestyle='--')
ax.plot([r["LA_ss"],r["LA_ss"]],[0,r["gA_ss"]],lw=2,color='gray',linestyle='dotted')

# Annotate
ax.annotate(r'$\lambda g_L$', xy=(.9*max(L),r["gA_ss"]-.001), size=16)
ax.annotate(r'$(1-\phi)g_A = (1-\phi)\theta s_R^{\lambda}\frac{L_t^{\lambda}}{A_t^{1-\phi}}$', xy=(.65*max(L),max(r["gA"])-.001), size=16)
ax.annotate(r'$\frac{L_t^{\lambda}}{A_t^{1-\phi}}$ is falling', xy=(.8*max(L),r["gA_ss"]+.002), size=16)
ax.annotate(r'$\frac{L_t^{\lambda}}{A_t^{1-\phi}}$ is rising', xy=(1.2*min(L),r["gA_ss"]-.002), size=16)

# Options
ax.set_xlim(min(L),max(L))
ax.set_ylim(min(r["gA"]),max(r["gA"]))
ax.set_xlabel(r'$L_t^{\lambda}/A_t^{1-\phi}$', fontsize=14, loc='right', labelpad = -20)
ax.set_ylabel('Growth rate', fontsize=14, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Format ticks
ax.set_yticks([])
ax.set_xticks([r["LA_ss"]])
ax.set_xticklabels([r'$\left(\frac{L^{\lambda}}{A^{1-\phi}}\right)^{ss}$'],size=14)

#plt.show()

# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch5-fig1.eps")
plt.savefig(path, bbox_inches='tight')
