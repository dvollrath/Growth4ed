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

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

for label, grp in pwplot.groupby('country'): # for each country
    grp.plot(x = 'year', y = 'csh_i',ax = ax, label = label,lw=2) # plot their cap formation share

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Gross capital formation / GDP', fontsize=14)
ax.set_yticks([0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0])
ax.set_yticklabels([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],rotation=0)

ax.annotate('China',xy=(1990,.2),size=14)
ax.annotate('South Korea',xy=(1975,.45),size=14)

ax.legend().set_visible(False)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch3-fig3.eps")
plt.savefig(path, bbox_inches='tight')
