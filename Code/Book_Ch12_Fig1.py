import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

# override params for this figure
from matplotlib import rcParams
rcParams['axes.prop_cycle'] = plt.cycler(color=["black", "gray", "black","gray"],linestyle=['-', '--', 'dotted','-'])

##################################################################
# Import data and do calculations
##################################################################
un = f.fert() # call function to load PWT data,

countries = ['USA','JPN','CHN','DEU'] # set of countries to plot
unplot = un[(un['Code'].isin(countries))] 

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

for label, grp in unplot.groupby('Entity'): # for each country
    grp.plot(x = 'Year', y = 'tfr_plot',ax = ax, label = label, lw=2)

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Total fertility rate', fontsize=14)
ax.set_xticks(np.arange(1950,2060,10))
ax.set_xticklabels(np.arange(1950,2060,10),rotation=0)
ax.set_yticks(np.arange(1,8,1))
ax.set_yticklabels(np.arange(1,8,1),rotation=0)

ax.annotate('Germany',xy=(1980,1.2),size=12)
ax.annotate('China',xy=(1975,5),size=12)
ax.annotate('United\nStates',xy=(1960,3.6),size=12)
ax.annotate('Japan',xy=(2040,1.3),size=12)

ax.legend().set_visible(False)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch12-fig1.eps")
plt.savefig(path, bbox_inches='tight')