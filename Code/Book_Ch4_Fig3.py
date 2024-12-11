import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

# override parameters for this plot
from matplotlib import rcParams
rcParams['axes.prop_cycle'] = plt.cycler(color=["black", "gray", "black", "gray", "black", "gray"],
    linestyle=['-', '-', '-.','-.','--','--'])

##################################################################
# Import data and do calculations
##################################################################
# read OECD R&D stats
df = f.oecd()

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

for label, grp in df.groupby('COUNTRY'):
    grp.plot(x = 'obsTime', y = 'RDpercent',ax = ax, label = label,lw=2)

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('R&D workers as percent of employment', fontsize=14)
ax.set_yticks([0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0,1.1])
ax.set_yticklabels([0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0,1.1],rotation=0)

ax.annotate('China',xy=(2005,.21),size=12)
ax.annotate('Germany',xy=(2005,.67),size=12)
ax.annotate('Japan',xy=(2000,1.01),size=12)
ax.annotate('United\nStates',xy=(1995,.7),size=12)
ax.annotate('United\nKingdom',xy=(1995,.48),size=12)

ax.legend().set_visible(False)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch4-fig3.eps")
plt.savefig(path, bbox_inches='tight')
