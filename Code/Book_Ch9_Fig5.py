from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['Times New Roman']
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'

import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.optimize import fsolve

#############################################
## Define functions
#############################################

def pop(phi,cmin,gamma,y): # steady state value of K/AL
	return (1-gamma)*y/(np.exp(phi*y)*cmin)


#############################################
## Set up problem
#############################################
phi = 1 # effect of GDP pc on price of kids
cmin = 5 # minimum consumption
gamma = .5 # utility weight for children
beta = 1.5 # land's role in production (unrealistic, but useful for making a good-looking figure)
axl = np.linspace(0,3,num=100) # AX/L values to graph
y = axl**beta # convert those AX/L values to GDP p.c. values to graph
gA = .05 # growth rate of productivity

#############################################
## Calculate solutions
#############################################
gL = (1-gamma)*y/(np.exp(phi*y)*cmin) # growth rate of productivity and labor force

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# This figure "cheats" a little. I created the Figure by graphing the relationship of the 
# growth rates to the level of AX/L. But it is labelled that the x-axis is "y", or GDP pc. 
# This is solely to keep the Figure legible. If you graph against y itself, the peak
# of the population growth function gets very narrow and the s.s. are hard to see

# Main elements
ax.plot([0,3], [gA,gA], lw=3, color='gray',linestyle='dashed') # growth rate of productivity
ax.plot(axl, gL, lw=3, color='black') # growth rate of population

# Add arrows showing dynamics
ax.plot(np.linspace(.1,2.8,num=10),[0,0,0,0,0,0,0,0,0,0],'k>')

# Add text
ax.annotate(r'$g_A$', xy=(3-.1,gA+.002), size=16)
ax.annotate(r'$\beta g_L$', xy=(1,max(gL)+.002),size=16)

# Options
ax.set_xlim(0,3)
ax.set_ylim(-.01,.08)
ax.set_xlabel(r'$y_t$', fontsize=16, loc='right')
ax.set_ylabel(r'Growth rates', fontsize=16, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(labelleft=False, left=False, bottom=False, labelbottom=False)
ax.spines['bottom'].set_position(('data', 0))

#ax.set_xticks()
#ax.set_xticklabels([r'$\left(\frac{AX}{L}\right)^{ss}_T$'],size=16)

#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch9-fig5.eps")
plt.savefig(path, bbox_inches='tight')
