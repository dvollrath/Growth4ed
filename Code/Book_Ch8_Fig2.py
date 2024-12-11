import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Import data and do calculations
##################################################################
pw = f.govern() # call function to load world governance indicators (includes PWT)

pw = pw[(pw['year']==2019)] # limit to 2019

pw = pw.set_index(['countrycode']) # set index for figure

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.scatter(pw['gov'],pw['yr_sch'],c = 'white') # invisible dots for data

for code, dat in pw.iterrows(): # label dots with country codes
    ax.annotate(code, (dat['gov'],dat['yr_sch']))

ax.set_xlabel('Social Infrastructure, 2019', fontsize=14)
ax.set_ylabel('Average years of schooling, 2019', fontsize=14)

plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch8-fig1.eps")
plt.savefig(path, bbox_inches='tight')
