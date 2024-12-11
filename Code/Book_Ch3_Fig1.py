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

# Estimate trend line for US
pwUSA = pw[pw['countrycode'].isin(['USA'])].copy() # US only data
lm = np.polyfit(pwUSA['year'],pwUSA['lnGDPpc'],1) # estimate simple trend line
lmfit = np.poly1d(lm) # create function to fit trend
pwUSA['fitGDPpc'] = np.exp(lmfit(pwUSA['year'])) # get fitted values by year

# Estimate trend line for Germany
pwDEU = pw[pw['countrycode'].isin(['DEU'])].copy() # DEU only data
estDEU =pwDEU[(pwDEU['year']>1990)] # estimate will be based only on post-1990 data
lm = np.polyfit(estDEU['year'],estDEU['lnGDPpc'],1) # estimate simple trend line
lmfit = np.poly1d(lm) # create function to fit trend
pwDEU['fitGDPpc'] = np.exp(lmfit(pwDEU['year'])) # get fitted values by year for ALL years

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.plot(pwUSA['year'], pwUSA['GDPpc'], lw=2, label='United States')
ax.plot(pwUSA['year'], pwUSA['fitGDPpc'], lw=2, color='gray',linestyle='dotted')
ax.plot(pwDEU['year'], pwDEU['GDPpc'], lw=2, label='Germany')
ax.plot(pwDEU['year'], pwDEU['fitGDPpc'], lw=2, color='gray',linestyle='dotted')

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('GDP per capita (Intl $, ratio scale)', fontsize=14)
ax.semilogy()
ax.set_yticks([2000,4000,8000,16000,32000,64000])
ax.set_yticklabels(['2,000','4,000','8,000','16,000','32,000','64,000'],rotation=0)

ax.annotate('Germany',xy=(1960,9000),size=14)
ax.annotate('United States',xy=(1960,30000),size=14)

ax.legend().set_visible(False)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch3-fig1.eps")
plt.savefig(path, bbox_inches='tight')
