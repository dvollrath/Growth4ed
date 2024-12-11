import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Import data and do calculations
##################################################################
# read Kremer data (with additions to data file by me)
md = pd.read_csv('../Data/kremer.csv')
md['pop'] = md['pop']/1000

an = md[md['year']>1940] # copy dataset only for 1950+ for annotation
an = an.set_index(['year'])

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.scatter(md['pop'],md['gL'],color='black',lw=3,label='') # plot ALL the data

for code, dat in an.iterrows(): # annotate only the 1950+ years
    ax.annotate(code, (dat['pop'],dat['gL']+.0005))

ax.set_xlabel('Population (billions)', fontsize=14)
ax.set_ylabel('Growth rate of population (%)', fontsize=14)

ax.set_yticks([0,0.005,0.010,0.015,0.02])
ax.set_yticklabels(['0','0.5','1','1.5','2'],rotation=0)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch9-fig3.eps")
plt.savefig(path, bbox_inches='tight')
