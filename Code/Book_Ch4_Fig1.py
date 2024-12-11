import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

# override parameters for this plot
from matplotlib import rcParams
rcParams['axes.prop_cycle'] = plt.cycler(color=["black", "gray", "black", "gray", "black", "gray"],
    linestyle=['-', '-', '-.','-.','--','--'])

##################################################################
# Import data and do calculations
##################################################################
# read IPC dataset on patents
df = pd.read_csv('../Data/oecd_pats_ipc_subset.csv')
df['Value'] = df['Value']/1000 # scale
countries = ['USA','GBR','CHN','KOR','JPN'] # set of countries to plot
df = df[df['LOCATION'].isin(countries)] 

df.loc[(df.LOCATION == 'CHN'), 'Country'] = 'China' # clean up text name
df.loc[(df.LOCATION == 'KOR'), 'Country'] = 'South Korea' # clean up text name

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

for label, grp in df.groupby('Country'): # for each country in dataset
    grp.plot(x = 'Time', y = 'Value',ax = ax, label = label,lw=2)

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Total patents granted (thousands)', fontsize=14)

ax.set_yticks([20,40,60,80,100,120,140,160])
ax.set_yticklabels([20,40,60,80,100,120,140,160],rotation=0)

ax.annotate('United\nStates',xy=(2015,130),size=12)
ax.annotate('Japan',xy=(2015,55),size=12)
ax.annotate('South\nKorea',xy=(2015,22),size=12)
ax.annotate('China',xy=(2015,13),size=12)
ax.annotate('U.K.',xy=(2015,0),size=12)

ax.legend().set_visible(False)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch4-fig1.eps")
plt.savefig(path, bbox_inches='tight')
