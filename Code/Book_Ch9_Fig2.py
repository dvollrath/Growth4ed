from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['Times New Roman']
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'

import numpy as np
import matplotlib.pyplot as plt
import os

#############################################
## Define functions
#############################################
def pop(axl,beta,theta,cmin):
	return theta*(axl**beta - cmin)

#############################################
## Set up problem
#############################################
nu = .01 # scaling parameter for population growth
cmin = .5 # minimum consumption
beta = .5 # role of land in production (high, but useful for making a good-looking figure)
axl = np.linspace(0,5,num=100) # range of AX/L values to graph
gA = 0.0075 # growth rate of productivity

#############################################
## Calculate solutions
#############################################
gL = nu*(axl**beta - cmin) # growth rate of population
axlss = (gA/nu + cmin)**(1/beta) # steady state value of AX/L

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot([0,3], [gA,gA], lw=3, color='gray',linestyle='dashed') # growth rate of productivity
ax.plot([axlss,axlss],[0,gA],color='black',linestyle='dotted',lw=2) # steady state
ax.plot(axl, gL, lw=3, color='black') # growth rate of population

# Add text
ax.annotate(r'$g_A$', xy=(3-.1,gA+.0005), size=16)
ax.annotate(r'$g_L = \nu \left(\frac{A_tX}{L_t}\right)^{\beta} - \nu \overline{c}$', xy=(2-.1,nu*(2**beta - cmin)+.003), size=16)
ax.annotate(r'$A_tX/L_t$ is falling', xy=(axlss+.25,.005),size =16)
ax.annotate(r'$A_tX/L_t$ is rising', xy=(axlss-1.3,.005),size =16)

# Options
ax.set_xlim(0,3)
ax.set_xlabel(r'$A_tX/L_t$', fontsize=16, loc='right')
ax.set_ylabel(r'Growth rates', fontsize=16, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(labelleft=False, left=False)
ax.spines['bottom'].set_position(('data', 0))

ax.set_xticks([axlss])
ax.set_xticklabels([r'$\left(\frac{AX}{L}\right)^{ss}$'],size=16)

#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch9-fig2.eps")
plt.savefig(path, bbox_inches='tight')
