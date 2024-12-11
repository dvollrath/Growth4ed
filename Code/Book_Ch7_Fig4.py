import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

# override parameters for this figure
from matplotlib import rcParams
rcParams['axes.prop_cycle'] = plt.cycler(color=["black", "black", "black"],linestyle=['-', '--', 'dotted'])

##################################################################
# Import data and do calculations
##################################################################
mad = f.maddison() # call function to load PWT data,

countries = ['USA','JPN'] # set of countries to plot
madplot = mad[(mad['countrycode'].isin(countries)) & (mad['year']>1884)] 

# estimate trend for USA over whole period
est = madplot[madplot['countrycode']=='USA']
lm = np.polyfit(est['year'],est['lnGDPpc'],1) # estimate simple trend line
print('Estimated growth rate for US:') # print for reference in book
print(lm)

# estimate trend line for JPN over whole period
est = madplot[madplot['countrycode']=='JPN']
lm = np.polyfit(est['year'],est['lnGDPpc'],1) # estimate simple trend line
print('Estimated growth rate for JPN:') # print for reference in book
print(lm)

# estimate trend for USA prior to 1920
est = madplot[(madplot['countrycode']=='USA') & (madplot['year']<1920)]
lm = np.polyfit(est['year'],est['lnGDPpc'],1) # estimate simple trend line
print('Estimated growth rate for USA pre-1920:') # print for reference in book
print(lm)

# estimate trend for JPN prior to 1920
est = madplot[(madplot['countrycode']=='JPN') & (madplot['year']<1920)]
lm = np.polyfit(est['year'],est['lnGDPpc'],1) # estimate simple trend line
print('Estimated growth rate for JPN pre-1920:') # print for reference in book
print(lm)

# estimate trend for USA after 1975
est = madplot[(madplot['countrycode']=='USA') & (madplot['year']>1975)]
lm = np.polyfit(est['year'],est['lnGDPpc'],1) # estimate simple trend line
print('Estimated growth rate for USA post-1975:') # print for reference in book
print(lm)

# estimate trend for JPN after 1975
est = madplot[(madplot['countrycode']=='JPN') & (madplot['year']>1975)]
lm = np.polyfit(est['year'],est['lnGDPpc'],1) # estimate simple trend line
print('Estimated growth rate for JPN post-1975:') # print for reference in book
print(lm)

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

for label, grp in madplot.groupby('country'):
    grp.plot(x = 'year', y = 'gdppc',ax = ax, label = label, lw=2)

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('GDP per capita (Intl $, ratio scale)', fontsize=14)
ax.semilogy()
ax.set_yticks([1000,2000,4000,8000,16000,32000,64000])
ax.set_yticklabels(['1,000','2,000','4,000','8,000','16,000','32,000','64,000'],rotation=0)

ax.annotate('United States',xy=(1960,32000),size=12)
ax.annotate('Japan',xy=(1980,16000),size=12)

ax.legend().set_visible(False)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch7-fig4.eps")
plt.savefig(path, bbox_inches='tight')
