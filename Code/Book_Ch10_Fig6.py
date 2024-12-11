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

ax.plot(ei['year'],ei['co2'],c='black',lw=2)

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Total CO2 emissions (million metric tonnes)', fontsize=14)
ax.set_xticks(np.arange(1950,2025,5))

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch10-fig6.eps")
plt.savefig(path, bbox_inches='tight')
