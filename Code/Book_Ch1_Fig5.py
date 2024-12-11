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

madplot = md[(md['countrycode'].isin(['USA'])) & (md['year']>1869)].copy()

# estimate trend line to plot
lm = np.polyfit(madplot['year'],madplot['lnGDPpc'],1) # estimate simple trend line
lmfit = np.poly1d(lm) # create function to fit trend
madplot['fitGDPpc'] = np.exp(lmfit(madplot['year'])) # get fitted values by year

print(lm) # print results of estimation for reference in book

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.plot(madplot['year'], madplot['gdppc'], lw=2)
ax.plot(madplot['year'], madplot['fitGDPpc'], lw=2)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('GDP per capita (Intl $, log scale)', fontsize=14)
ax.semilogy()
xticks = np.arange(1870,2030,10)
ax.set_xticks(xticks)
ax.set_xticklabels(xticks)
ax.set_yticks([2000,4000,8000,16000,32000,64000])
ax.set_yticklabels(['2,000','4,000','8,000','16,000','32,000','64,000'],rotation=0)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch1-fig5.eps")
plt.savefig(path, bbox_inches='tight')
