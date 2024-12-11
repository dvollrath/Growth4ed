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

ax.plot(md['gpop'],md['ggdppc'],marker='o',color='gray',lw=1)

for i, txt in enumerate(md['year']):
    plt.annotate(txt, (md['gpop'][i]+.0005, md['ggdppc'][i]),fontsize=12)

ax.set_xlabel('Growth rate of world population (%)', fontsize=14)
ax.set_ylabel('Growth rate of world GDP per capita (%)', fontsize=14)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch4-fig7.eps")
plt.savefig(path, bbox_inches='tight')
