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
gamma = .6 # weight on A (versus D with 1-gamma) in diffusion equation
psi = .1 # scaling parameter in diffusion equation
gA = .02 # growth rate of world frontier
h = 1 # level of human capital

#############################################
## Calculate solutions
#############################################
AD = np.arange(0,.2,.01) # range of A/D values to graph

gD = psi*h*AD**gamma # diffusion equation
ADss = (gA/(psi*h))**(1/gamma) # steady state A/D ratio

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot(AD, gD, lw=3, color='black') # plot growth rate of D
ax.plot([min(AD),max(AD)],[gA,gA],lw=3,color='gray',linestyle='--')
ax.plot([ADss,ADss],[0,gA],lw=2,color='black',linestyle='dotted')

# Annotate
ax.annotate(r'$g_A$', xy=(.9*max(AD),gA-.001), size=16)
ax.annotate(r'$g_D = \psi h \left(\frac{A_t}{D_t} \right)^{\gamma}$', xy=(.65*max(AD),psi*h*(.65*max(AD))**gamma+.005), size=16)
ax.annotate(r'$\frac{A_t}{D_t}$ is falling', xy=(.8*max(AD),gA+.004), size=16)
ax.annotate(r'$\frac{A_t}{D_t}$ is rising', xy=(min(AD)+.01,gA-.004), size=16)

# Options
ax.set_xlim(min(AD),max(AD))
ax.set_ylim(min(gD),max(gD))
ax.set_xlabel(r'$A_t/D_t$', fontsize=14, loc='right', labelpad = -20)
ax.set_ylabel('Growth rate', fontsize=14, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Format ticks
ax.set_yticks([])
ax.set_xticks([ADss])
ax.set_xticklabels([r'$\left(\frac{A}{D}\right)^{ss}$'],size=14)

#plt.show()

# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch7-fig2.eps")
plt.savefig(path, bbox_inches='tight')
