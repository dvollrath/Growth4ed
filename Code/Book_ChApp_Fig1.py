from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['Times New Roman']
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'

import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Solow as sw # pull in common Solow functions

#############################################
## Set up problem
#############################################
# Set range of KY values to graph over
MinKY = 1
MaxKY = 5

PreGA = .02
PreGL = .01
PreDelta = .045
PreSK = .2
alpha = 0

#############################################
## Calculate solutions
#############################################
ky = np.arange(MinKY,MaxKY,.01) # get range of KY values to use
kal = sw.KAL(ky,alpha) # get K/AL values for each individual KY used
PreGK = sw.GrowthK(ky,PreSK,alpha,PreDelta) # get growth rate of K for each ky value
PreKALss = sw.KAL(sw.SteadyKY(PreGA,PreGL,PreDelta,PreSK),alpha) # get KAL steady state from KY steady state
KALzero = .5*PreKALss
GKzero = sw.GrowthK(KALzero**(1-alpha),PreSK,alpha,PreDelta)

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot(kal, PreGK, lw=3, color='black') # plot growth rate of K
ax.plot([min(kal),max(kal)],[PreGA+PreGL,PreGA+PreGL], lw=3, color='black', linestyle='--') # plot growth rate of A and L
ax.plot([PreKALss,PreKALss],[0,PreGA+PreGL],lw=2,color='black',linestyle='dotted')
ax.plot(np.linspace(min(kal),PreKALss-.1,num=5),[0,0,0,0,0],'k>')
ax.plot(np.linspace(PreKALss+.1,max(kal)-.1,num=5),[0,0,0,0,0],'k<')

# Add text
ax.annotate(r'$g_X = \phi\frac{Z}{X} - \delta$', xy=(1.4*min(kal)+.1,sw.GrowthK(1.4*min(kal)**(1-alpha),PreSK,alpha,PreDelta)), size=16)
ax.annotate(r'$g_Z = \beta$', xy=(.8*max(kal),PreGA+PreGL+.003), size=16)
ax.annotate(r'$\frac{X}{Z}$ is falling',xy=(.8*max(kal),PreGA+PreGL-.02), size=16)
ax.annotate(r'$\frac{X}{Z}$ is rising',xy=(1.1*min(kal),PreGA+PreGL+.01), size=16)

# Options
ax.set_xlim(min(kal)-.1,max(kal))
ax.set_ylim(min(PreGK)-.005,max(PreGK)+.005)
ax.set_xlabel(r'$X/Z$', fontsize=16, loc='right')
ax.set_ylabel('Growth rate', fontsize=16, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))

# Format ticks
ax.set_yticks([0])
ax.set_yticklabels(['0'],size=16)
ax.set_xticks([PreKALss])
ax.set_xticklabels([r'$\left(\frac{X}{Z}\right)^{ss}$'],size=16)

#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-chapp-fig1.eps")
plt.savefig(path, bbox_inches='tight')
