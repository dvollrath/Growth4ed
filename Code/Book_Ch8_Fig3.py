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
pw['relA'] = pw['relA']/100 # scale for figure
pw = pw[(pw['relA']<1.5) & (pw['relA']>.01)] # eliminate outliers
pw = pw.set_index(['countrycode']) # set index for figure

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.scatter(pw['gov'],pw['relA'],c = 'white') # invisible dots for data

for code, dat in pw.iterrows(): # label dots with country codes
    ax.annotate(code, (dat['gov'],dat['relA']))

ax.set_xlabel('Social Infrastructure, 2019', fontsize=14)
ax.set_ylabel('Productivity relative to U.S., 2019 (log scale)', fontsize=14)
ax.semilogy()
ax.set_yticks([0.1,.2,.4,.8,1,1.4])
ax.set_yticklabels(['0.1','0.2','0.4','0.8','1.0','1.4'],rotation=0)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch8-fig3.eps")
plt.savefig(path, bbox_inches='tight')
