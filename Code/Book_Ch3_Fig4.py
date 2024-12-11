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

pwplot = pw[pw['countrycode'].isin(['CHN','KOR'])].copy() # just Korea and China

pwplot['lnpop'] = np.log(pwplot['pop']) # log of population
pwplot['gpop'] = pwplot.groupby(['countrycode'])['lnpop'].diff(periods=5)/5 # annualized growth over 5 year period

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

for label, grp in pwplot.groupby('country'): # for each country
    grp.plot(x = 'year', y = 'gpop',ax = ax, label = label,lw=2) # plot growth rate of population

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('5-year average population growth rate', fontsize=14)
ax.set_yticks([0,.01,.02,.03,.04])
ax.set_yticklabels([0,.01,.02,.03,.04],rotation=0)
ax.legend(loc="upper right",fontsize=14)

ax.annotate('China',xy=(1990,.019),size=14)
ax.annotate('South Korea',xy=(1960,.032),size=14)

ax.legend().set_visible(False)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch3-fig4.eps")
plt.savefig(path, bbox_inches='tight')
