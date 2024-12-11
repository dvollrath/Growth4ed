import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Import data and do calculations
##################################################################
mad = f.maddison() # call function to load PWT data,

first = 1870
last = 2018
diff = last - first

# read Maddison dataset into pw
#mad = pd.read_csv('../Data/mpd2020raw.csv')
#mad.sort_values(by=['countrycode', 'year']) # organize by country/year
#mad['lnGDPpc'] = np.log(mad['gdppc'])

# calculate "reverse" growth rate of GDP per capita from first to last period
mad['glnGDPpc'] = -100*mad.groupby(['countrycode'])['lnGDPpc'].diff(periods=-1*diff)/diff

countries = ['USA','GBR','NZL','AUS','BEL','NLD','DNK','FRA','ITA','AUT','DEU','CAN',
	'CHE','IRL','GRC','ESP','PRT','FIN','SWE','JPN','NOR'] # set of countries to plot
madplot = mad[(mad['countrycode'].isin(countries)) & (mad['year']==first)].copy()
madplot = madplot.set_index(['countrycode']) # index for plotting

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.scatter(madplot['gdppc'],madplot['glnGDPpc'],c = 'white') # invisible dots for data

for code, dat in madplot.iterrows(): # label dots with country codes
    ax.annotate(code, (dat['gdppc'],dat['glnGDPpc']))

ax.set_xlabel('GDP per capita, 1870', fontsize=14)
ax.set_ylabel('Average annual growth rate (%), 1870-2019', fontsize=14)
yticks = np.arange(1,3,.25)
ax.set_xlim(1000,6000)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks)
ax.set_xticks([1000,2000,3000,4000,5000,6000])
ax.set_xticklabels(['1,000','2,000','3,000','4,000','5,000','6,000'],rotation=0)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch3-fig7.eps")
plt.savefig(path, bbox_inches='tight')
