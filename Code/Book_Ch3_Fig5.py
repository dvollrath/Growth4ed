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

pw = pw[(pw['year']>1969)].copy() # just 1970 and after

mean_csh_i = pw.groupby(['countrycode'])[['csh_i']].mean() # average capital formation share by country
pw = pw.set_index(['countrycode']) # ensure pw has countrycode as an index
pw['mean_csh_i'] = mean_csh_i # assign the mean csh data back to the pw dataframe

# limit datafram by year, bounds on csh, and level of GDPpc
pwplot = pw[(pw['year']==2019) & (pw['mean_csh_i']>0) & (pw['mean_csh_i']<.5) & (pw['GDPpc']>1000)].copy()

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.scatter(pwplot['mean_csh_i'],pwplot['GDPpc'],c = 'white') # scatter plot with invisible dots

for code, dat in pwplot.iterrows(): # annotate each dot with the country code
    ax.annotate(code, (dat['mean_csh_i'],dat['GDPpc']))

ax.set_xlabel('Average capital formation share of GDP, 1970-2019', fontsize=14)
ax.set_ylabel('GDP per capita 2019 (Intl $, log scale)', fontsize=14)
ax.semilogy()
ax.set_xticks(np.arange(0,.55,.05))
ax.set_yticks([1000,2000,4000,8000,16000,32000,64000,128000])
ax.set_yticklabels(['1,000','2,000','4,000','8,000','16,000','32,000','64,000','128,000'],rotation=0)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch3-fig5.eps")
plt.savefig(path, bbox_inches='tight')
