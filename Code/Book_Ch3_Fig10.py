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

first = 1960 # initial year of analysis
last = 2019 # final year of analysis

pw = pw[(pw['year']>=first) & (pw['year']<=last)].copy() # limit to these years inclusive

# get 90/10 ratio within a year
pw['p90'] = pw.groupby(['year'])['GDPpc'].transform(lambda x: x.quantile(.9)) # 90th percentile
pw['p10'] = pw.groupby(['year'])['GDPpc'].transform(lambda x: x.quantile(.1)) # 10th percentile
pw['p9010'] = pw['p90']/pw['p10'] # generate ratio

pw.sort_values(by=['year'],inplace=True) # sort by year to ensure figure comes out looking okay

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.plot(pw['year'],pw['p9010'],c='black')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Ratio of GDP per capita, 90th to 10th percentile', fontsize=14)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch3-fig10.eps")
plt.savefig(path, bbox_inches='tight')
