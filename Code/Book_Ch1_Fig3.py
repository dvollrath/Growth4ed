import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

# override parameters for this figure
from matplotlib import rcParams
rcParams['axes.prop_cycle'] = plt.cycler(color=["black", "gray", "black"],linestyle=['-', '--', 'dotted'])

##################################################################
# Import data and do calculations
##################################################################
md = f.maddison() # call function to load PWT data,

countries = ['GBR','ITA','NLD'] # set of countries to plot
madplot = md[(md['countrycode'].isin(countries)) & (md['year']>1499)] 

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

for label, grp in madplot.groupby('country'):
    grp.plot(x = 'year', y = 'gdppc',ax = ax, label = label, lw=2)

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('GDP per capita (Intl $, log scale)', fontsize=14)
ax.semilogy()
ax.set_yticks([1000,2000,4000,8000,16000,32000,64000])
ax.set_yticklabels(['1,000','2,000','4,000','8,000','16,000','32,000','64,000'],rotation=0)

ax.annotate('Italy',xy=(1850,2000),size=14)
ax.annotate('Netherlands',xy=(1650,5000),size=14)
ax.annotate('United Kingdom',xy=(1675,1500),size=14)

ax.legend().set_visible(False)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch1-fig3.eps")
plt.savefig(path, bbox_inches='tight')
