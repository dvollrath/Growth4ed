import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Import data and do calculations
##################################################################
pw = f.pwt() # call function to load PWT data,
pw = pw[(pw['relGDPpc']<=120)] # eliminates several outliers

first = 1970 # initial year of convergence plot
last = 2019 # final year of convergence plot
diff = last - first

# calculate growth rate; the negative signs calculate growth "forward"
# so 1970 will get the annualized growth rate from 1970 to 2019
pw['gGDPpc'] = -100*pw.groupby(['countrycode'])['lnGDPpc'].diff(periods=-1*diff)/diff

pw = pw.set_index(['countrycode']) # set index to country code

# only the initial year, and drop extremes on growth rates and GDP pc.
pwplot = pw[(pw['year']==first) & (pw['gGDPpc']>-4) & (pw['GDPpc']<100000)].copy()

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.scatter(pwplot['GDPpc'],pwplot['gGDPpc'],c = 'white') # invisible dots for data

for code, dat in pwplot.iterrows(): # label each dot with country code
    ax.annotate(code, (dat['GDPpc'],dat['gGDPpc']))

ax.set_xlabel('GDP per capita 1970 (Intl $, log scale)', fontsize=14)
ax.set_ylabel('Annual growth rate of GDP per capita (%), 1970-2019', fontsize=14)
ax.semilogx()
ax.set_yticks(np.arange(-2,7,1))
ax.set_xticks([1000,2000,4000,8000,16000,32000,64000])
ax.set_xticklabels(['1,000','2,000','4,000','8,000','16,000','32,000','64,000'],rotation=0)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch3-fig8.eps")
plt.savefig(path, bbox_inches='tight')
