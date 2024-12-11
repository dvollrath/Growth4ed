import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Import data and do calculations
##################################################################
# read Jorda et al dataset
jst = pd.read_csv('../Data/jstdatasetr4.csv')
jst.sort_values(by=['iso', 'year']) # organize by country/year

# Set rolling return period
lag = 5

jst['pi'] = jst.groupby(['iso'])['cpi'].pct_change() # calculate inflation rate
jst['ln_capital_real'] = np.log((1+jst['capital_tr'])/(1+jst['pi'])) # log real return

# rolling sum of log real returns
jst['capital_roll'] = jst.groupby('iso')['ln_capital_real'].apply(lambda x:x.rolling(center=False,window=lag).sum())
jst['capital_roll'] = (1/lag)*jst['capital_roll'] # scale by number of periods
jst['capital_roll'] = 100*(np.exp(jst['capital_roll']) - 1) # convert to percentage return


countries = ['USA'] # set of countries to plot
jstplot = jst[(jst['iso'].isin(countries)) & (jst['year']>1930)] # limit by country and year
jstmean = jstplot['capital_roll'].mean() # mean return over whole period
print(jstmean) # print for reference in book

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.plot(jstplot['year'],jstplot['capital_roll'],lw=2)
ax.plot([1930,2020],[jstmean,jstmean],lw=2,color='gray')

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Trailing ' + str(lag) + '-year real return on capital (%)', fontsize=14)
ax.set_ylim(-5,20)
xticks = np.arange(1930,2030,10)
ax.set_xticks(xticks)
ax.set_xticklabels(xticks)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch1-fig6.eps")
plt.savefig(path, bbox_inches='tight')
