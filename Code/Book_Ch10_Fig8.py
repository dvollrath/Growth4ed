import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Import data and do calculations
##################################################################
ei = pd.read_csv('../Data/nei.csv') # read emissions data

# rebase to initial year
ei['co'] = 100*ei['co']/ei.loc[(ei['year']==1970),'co'].values
ei['nox'] = 100*ei['nox']/ei.loc[(ei['year']==1970),'nox'].values
ei['so2'] = 100*ei['so2']/ei.loc[(ei['year']==1970),'so2'].values
ei['voc'] = 100*ei['voc']/ei.loc[(ei['year']==1970),'voc'].values
ei['pm25'] = 100*ei['pm25']/ei.loc[(ei['year']==1990),'pm25'].values
ei['nh3'] = 100*ei['nh3']/ei.loc[(ei['year']==1990),'nh3'].values

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.plot(ei['year'],ei['co'],c='black',lw=2,label='Carbon monoxide')
#ax.plot(ei['year'],ei['nox'],c='gray',lw=2,label='Nitrogen oxides')
ax.plot(ei['year'],ei['so2'],c='black',lw=2,linestyle='dashed',label='Sulfur dioxide')
ax.plot(ei['year'],ei['voc'],c='black',lw=2,linestyle='dotted',label='Volatile organics')
ax.plot(ei['year'],ei['pm25'],c='gray',lw=2,linestyle='dashed',label='Particulate matter')
#ax.plot(ei['year'],ei['nh3'],c='gray',lw=2,linestyle='dotted',label='Ammonia')

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Index of total emissions (1970=100)', fontsize=14)
ax.set_yticks(np.arange(0,120,10))
ax.set_xticks(np.arange(1970,2025,5))

ax.annotate('Particulate\nmatter',xy=(2016,78),size=12)
ax.annotate('Volatile\norganics',xy=(2016,52),size=12)
ax.annotate('Carbon\nmonoxide',xy=(2016,23),size=12)
ax.annotate('Sulfer\ndioxide',xy=(2016,11),size=12)

ax.legend().set_visible(False)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch10-fig8.eps")
plt.savefig(path, bbox_inches='tight')
