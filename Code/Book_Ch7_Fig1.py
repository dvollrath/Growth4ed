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
pw = pw.set_index(['countrycode'])
pw['relA'] = pw['relA']/100 # recale for this figure
pw['relGDPpc'] = pw['relGDPpc']/100 # rescale fort this figure

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.scatter(pw['relA'],pw['relGDPpc'],c = 'white') # invisible dots for data

for code, dat in pw.iterrows(): # label each dot with country code
    ax.annotate(code, (dat['relA'],dat['relGDPpc']))

ax.plot([0,1.75],[0,1.75],lw=2,linestyle='dashed',color='gray')

ax.set_xlabel(r'Productivity relative to the U.S. ($A_i/A_{US}$)', fontsize=14)
ax.set_ylabel(r'GDP per capita relative to the U.S. ($y_i/y_{US}$)', fontsize=14)


#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch7-fig1.eps")
plt.savefig(path, bbox_inches='tight')
