import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Import data and do calculations
##################################################################
ei = f.energy() # call function to load EIA data

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.plot(ei['year'],ei['renew_perc'],c='black',lw=2)

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Renewables as percent of all energy', fontsize=14)
ax.set_yticks(np.arange(0,12,1))
ax.set_xticks(np.arange(1950,2025,5))

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch10-fig7.eps")
plt.savefig(path, bbox_inches='tight')
