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
pwUSA = pw[pw['countrycode'].isin(['USA'])].copy() 
lm = np.polyfit(pwUSA['year'],pwUSA['lnGDPpc'],1) # estimate simple trend line
lmfit = np.poly1d(lm) # create function to fit trend
pwUSA['fitGDPpc'] = np.exp(lmfit(pwUSA['year'])) # get fitted values by year

# Estimate trend lines for South Korea
pwKOR = pw[pw['countrycode'].isin(['KOR'])].copy()

# -- Early period
preKOR =pwKOR[(pwKOR['year']<1966) & (pwKOR['year']>1952)].copy() # only early period
lm = np.polyfit(preKOR['year'],preKOR['lnGDPpc'],1) # estimate simple trend line
lmfit = np.poly1d(lm) # create function to fit trend
pwKOR['prefitGDPpc'] = np.exp(lmfit(pwKOR['year'])) # get fitted values for ALL years

# -- Late period
postKOR =pwKOR[(pwKOR['year']>2000)].copy() # only later period
lm = np.polyfit(postKOR['year'],postKOR['lnGDPpc'],1) # estimate simple trend line
lmfit = np.poly1d(lm) # create function to fit trend
pwKOR['postfitGDPpc'] = np.exp(lmfit(pwKOR['year'])) # get fitted values for ALL years

# Pull in Chinese data for plotting
pwCHN = pw[pw['countrycode'].isin(['CHN'])].copy()

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.plot(pwUSA['year'], pwUSA['GDPpc'], lw=2, label='United States')
ax.plot(pwUSA['year'], pwUSA['fitGDPpc'], lw=2, color='gray',linestyle='dotted')
ax.plot(pwKOR['year'], pwKOR['GDPpc'], lw=2, label='South Korea')
ax.plot(pwKOR['year'], pwKOR['prefitGDPpc'], lw=2, color='gray',linestyle='dotted')
ax.plot(pwKOR['year'], pwKOR['postfitGDPpc'], lw=2, color='gray',linestyle='dotted')
ax.plot(pwCHN['year'], pwCHN['GDPpc'], lw=2, label='China')

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('GDP per capita (Intl $, ratio scale)', fontsize=14)
ax.semilogy()
ax.set_yticks([1000,2000,4000,8000,16000,32000,64000])
ax.set_yticklabels(['1,000','2,000','4,000','8,000','16,000','32,000','64,000'],rotation=0)

ax.annotate('South\nKorea',xy=(1990,8000),size=14)
ax.annotate('China',xy=(2010,7000),size=14)
ax.annotate('United States',xy=(1960,30000),size=14)

ax.legend().set_visible(False)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch3-fig2.eps")
plt.savefig(path, bbox_inches='tight')
