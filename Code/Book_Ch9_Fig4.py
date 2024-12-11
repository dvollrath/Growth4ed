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
## Set up problem
#############################################
phi = 1 # effect of GDP pc on price of kids
cmin = 5 # minimum consumption
gamma = .5 # utility weight for children
beta = 1.5 # land's role in production (unrealistic, but useful for making a good-looking figure)
axl = np.linspace(0,3,num=100) # AX/L values to graph
y = axl**beta # convert those AX/L values to GDP p.c. values to graph
gA = .02 # growth rate of productivity

#############################################
## Calculate solutions
#############################################
gL = (1-gamma)*y/(np.exp(phi*y)*cmin) # population growth with income and price effects

# Solve for steady state values of y - these are not analytically obvious - done numerically
func = lambda y : gA - (1-gamma)*y*np.exp(-1*phi*y)/cmin # create function gA - gL
sslow = fsolve(func,0) # solve for smaller ss (gA - gL = 0), start with 0 and solve "up"
sshigh = fsolve(func,3) # solve for larger ss (gA - gL = 0), start with max and solve "down"
axllow = sslow**(1/beta) # convert ss y to AX/L
axlhigh = sshigh**(1/beta) # convert ss y to AX/L

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
ax.plot([axllow,axllow],[0,gA],color='black',linestyle='dotted',lw=2) # low s.s.
ax.plot([axlhigh,axlhigh],[0,gA],color='black',linestyle='dotted',lw=2) # high s.s.
ax.plot(axl, gL, lw=3, color='black') # growth rate of population

# Add arrows showing dynamics around s.s.
ax.plot(np.linspace(.1,axllow-.1,num=2),[0,0],'k>')
ax.plot(np.linspace(axllow+.1,axlhigh-.1,num=5),[0,0,0,0,0],'<k')
ax.plot(np.linspace(.1+axlhigh,3,num=5),[0,0,0,0,0],'k>')

# Add text
ax.annotate(r'$g_A$', xy=(3-.1,gA+.002), size=16)
ax.annotate(r'$g_L$', xy=(1,max(gL)+.002),size=16)

# Options
ax.set_xlim(0,3)
ax.set_ylim(-.01,.08)
ax.set_xlabel(r'$y_t$', fontsize=16, loc='right')
ax.set_ylabel(r'Growth rates', fontsize=16, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(labelleft=False, left=False)
ax.spines['bottom'].set_position(('data', 0))

ax.set_xticks([axllow[0],axlhigh[0]])
ax.set_xticklabels([r'$y^{ss}_M$',r'$y^{ss}_T$'],size=16)

#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch9-fig4.eps")
plt.savefig(path, bbox_inches='tight')
