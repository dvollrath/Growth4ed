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

pw = pw[(pw['year']==2019)] # limit to 2019
pw = pw[(pw['trade']<2) & (pw['GDPpc']>800)] # cut outliers
pw = pw.set_index(['countrycode'])

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.scatter(pw['trade'],pw['GDPpc'],c = 'white') # invisible dots for data

for code, dat in pw.iterrows(): # label dots with country codes
    ax.annotate(code, (dat['trade'],dat['GDPpc']))

ax.set_xlabel(r'Total trade as a share of GDP', fontsize=14)
ax.set_ylabel(r'GDP per capita (intl \$, ratio scale)', fontsize=14)
ax.semilogy()
ax.set_xticks(np.arange(0,2.25,.25))
ax.set_xticklabels(np.arange(0,2.25,.25))
ax.set_yticks([1000,2000,4000,8000,16000,32000,64000,128000])
ax.set_yticklabels(['1,000','2,000','4,000','8,000','16,000','32,000','64,000','128,000'],rotation=0)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch7-fig3.eps")
plt.savefig(path, bbox_inches='tight')
