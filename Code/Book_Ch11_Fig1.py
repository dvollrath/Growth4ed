from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['Times New Roman']
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'

import numpy as np
import matplotlib.pyplot as plt
import os

#############################################
## Create figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# This is purely mechanical to show the dynamics in the AK model

# Main elements
ax.plot([0,8],[0.05,0.05], lw=3, color='black') # plot growth rate of K
ax.plot([0,8],[0.02,.02],lw=2,color='black',linestyle='dashed')
ax.plot(np.linspace(2.1,7.9,num=10),[0,0,0,0,0,0,0,0,0,0],'k>')

# Add text
ax.annotate(r'$g_K = s_I a - \delta$', xy=(7,.055), size=16)
ax.annotate(r'$g_L$', xy=(7,.025), size=16)

# Options
ax.set_xlim(0,8)
ax.set_ylim(-.01,.1)
ax.set_xlabel(r'$K_t/L_t$', fontsize=16, loc='right')
ax.set_ylabel('Growth rate', fontsize=16, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))

# Format ticks
ax.set_yticks([0])
ax.set_yticklabels(['0'],size=16)
ax.set_xticks([2])
ax.set_xticklabels([r'$\frac{K_0}{L_0}$'],size=16)

#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch11-fig1.eps")
plt.savefig(path, bbox_inches='tight')
