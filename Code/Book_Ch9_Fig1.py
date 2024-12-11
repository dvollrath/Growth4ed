import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Import data and do calculations
##################################################################
# read older Maddison 2010 dataset - this has estimates back to year 0 (newer versions drop this)
md = pd.read_csv('../Data/md2010raw.csv')
md['pop'] = md['pop']/1000000

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax2 = ax.twinx()

ax.plot(md['year'],md['gdppc'],color='black',lw=3,label='')
ax2.plot(md['year'],md['pop'],color='gray',lw=3,)

ax.annotate('GDP per capita',xy=(1500,500),size=12)
ax.annotate('Population',xy=(1000,750),size=12)

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('GDP per capita (intl $, log scale)', fontsize=14)
ax2.set_ylabel('Population (billions, log scale)', fontsize=14)
ax.semilogy()
ax2.semilogy()

ax.set_yticks([450,1000,2000,4000,6000,12000])
ax.set_yticklabels(['450','1,000','2,000','4,000','6,000','12,000'],rotation=0)
ax2.set_yticks([.25,.5,1,2,4,6,8])
ax2.set_yticklabels(['0.25','0.5','1','2','4','6','8'],rotation=0)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch9-fig1.eps")
plt.savefig(path, bbox_inches='tight')
