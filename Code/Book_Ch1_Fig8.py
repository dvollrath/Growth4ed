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

pwplot = pw[pw['countrycode'].isin(['USA'])].copy() # just the US data
cshmean = pwplot['csh_i'].mean() # mean capital formation share
print(cshmean) # print for use in book

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.plot(pwplot['year'],pwplot['csh_i'],lw=2) # capital formation share over time
ax.plot([1950,2020],[cshmean,cshmean],lw=2,color='gray') # mean share
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Gross capital formation / GDP', fontsize=14)
ax.set_yticks([0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0])
ax.set_yticklabels([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],rotation=0)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch1-fig8.eps")
plt.savefig(path, bbox_inches='tight')
