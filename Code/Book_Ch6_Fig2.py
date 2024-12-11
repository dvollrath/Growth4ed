import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

# override parameters for this plot
#from matplotlib import rcParams
#rcParams['axes.prop_cycle'] = plt.cycler(color=["black", "gray", "black","gray"],linestyle=['-', '--', 'dotted','-'])

##################################################################
# Import data and do calculations
##################################################################
# read business statistics dataset
bd = pd.read_csv('../Data/bds2018.csv')

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.plot(bd['year'],bd['estabs_entry_rate'],label='Establishment entry')
ax.plot(bd['year'],bd['estabs_exit_rate'],color='gray',label='Establishment exit')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Percent of existing establishments', fontsize=14)
ax.set_xticks(np.arange(1975,2025,5))
ax.set_xticklabels(np.arange(1975,2025,5),rotation=0)
ax.set_yticks(np.arange(8,17,1))
ax.set_yticklabels(np.arange(8,17,1),rotation=0)

ax.annotate('Establishment entry',xy=(1995,12.5),size=12)
ax.annotate('Establishment exit',xy=(1990,9.1),size=12)

ax.legend().set_visible(False)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch6-fig2.eps")
plt.savefig(path, bbox_inches='tight')