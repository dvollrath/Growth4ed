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

for label, grp in df.groupby('COUNTRY'): # for each country
    grp.plot(x = 'obsTime', y = 'obsValue',ax = ax, label = label,lw=2)

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('R&D workers (000s of FTE)', fontsize=14)

ax.annotate('United\nStates',xy=(2015,1200),size=12)
ax.annotate('Japan',xy=(2015,725),size=12)
ax.annotate('Germany',xy=(2015,475),size=12)
ax.annotate('China',xy=(2015,2000),size=12)
ax.annotate('United\nKingdom',xy=(2015,150),size=12)

ax.legend().set_visible(False)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch4-fig2.eps")
plt.savefig(path, bbox_inches='tight')
