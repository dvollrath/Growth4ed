from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['Times New Roman']
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'

import numpy as np
import matplotlib.pyplot as plt
import os

rng = np.random.default_rng(12345) #set seed to replicate figure

lnGDPpc = [1] # initialize list for actual GDP pc
trendpc = [.98] # initialize trend GDP pc

for x in range(0,200): # for each of 200 periods
	trendpc.append(trendpc[x]*(1+.1*.02)) # advance trend GDP pc by 0.2% (dN = .1 and gamma = .02)
	if rng.random()<.1: # if an innovation occurs
		lnGDPpc.append(lnGDPpc[x]*(1+.02)) # advance actual GDP pc by 2%
	else: # no innovation occurs
		lnGDPpc.append(lnGDPpc[x]) # keep actual GDP pc the same

time = np.arange(1,202,1)

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot(time, lnGDPpc, lw=3, color='black') # plot growth rate of K
ax.plot(time, trendpc, lw=3, color='gray',linestyle='dashed') # plot growth rate of K

# Options
ax.set_ylim(min(lnGDPpc)-.2,max(lnGDPpc)+.3)
ax.set_xlabel(r'Time', fontsize=16, loc='right')
ax.set_ylabel(r'$\log A_t$', fontsize=16, loc='top',rotation=0)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch6-fig1.eps")
plt.savefig(path, bbox_inches='tight')
