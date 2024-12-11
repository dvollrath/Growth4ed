import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Import data and do calculations
##################################################################
# read Maddison world data
md = f.world()

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.scatter(md['pop'],md['gdppc'])
ax.set_xlabel('World population (billions)', fontsize=14)
ax.set_ylabel('World GDP per capita (ratio scale)', fontsize=14)
ax.semilogy()
ax.set_yticks([1000,2000,4000,8000,16000])
ax.set_yticklabels(['1,000','2,000','4,000','8,000','16,000'],rotation=0)
ax.set_xticks([1,2,3,4,5,6,7,8])
ax.set_xticklabels([1,2,3,4,5,6,7,8],rotation=0)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch4-fig6.eps")
plt.savefig(path, bbox_inches='tight')
