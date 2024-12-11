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

pw = pw[(pw['year']>1969)].copy() # only post 1970

pw['lnpop'] = np.log(pw['pop']) # log population
pw['gpop'] = pw.groupby(['countrycode'])['lnpop'].diff(periods=49)/49 # 49-year annualized rate

# limit by year, extreme values of pop growth, and GDP per capita
pwplot = pw[(pw['year']==2019) & (pw['gpop']<.04) & (pw['gpop']>-.01) & (pw['GDPpc']>1000)].copy()
pwplot = pwplot.set_index(['countrycode'])

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.scatter(pwplot['gpop'],pwplot['GDPpc'],c = 'white') # scatter with invisible dots

for code, dat in pwplot.iterrows(): # label each dot with country code
    ax.annotate(code, (dat['gpop'],dat['GDPpc']))

ax.set_xlabel('Average annual population growth rate, 1970-2019', fontsize=14)
ax.set_ylabel('GDP per capita (Intl $, ratio scale)', fontsize=14)
ax.semilogy()
ax.set_xticks(np.arange(-.01,.05,.005))
ax.set_yticks([1000,2000,4000,8000,16000,32000,64000,128000])
ax.set_yticklabels(['1,000','2,000','4,000','8,000','16,000','32,000','64,000','128,000'],rotation=0)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch3-fig6.eps")
plt.savefig(path, bbox_inches='tight')
