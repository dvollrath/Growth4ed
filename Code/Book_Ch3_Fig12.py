import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Import data and do calculations
##################################################################
# read business statistics dataset
ow = pd.read_csv('../Data/owid-extreme-poverty.csv')

ow['out_poverty'] = ow['out_poverty']/1000000000
ow['in_poverty'] = ow['in_poverty']/1000000000

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

pal = ["silver", "dimgray"]
ax.stackplot(ow['Year'],ow['in_poverty'],ow['out_poverty'], colors=pal)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of people (billions)', fontsize=14)
ax.annotate('Number of people \n out of extreme \n poverty', xy=(1932,4), size=14)
ax.annotate('Number of people \n in extreme poverty', xy=(1940,.5), size=14)


ax.set_xticks(np.arange(1820,2040,20))
ax.set_xticklabels(np.arange(1820,2040,20),rotation=0)
ax.set_yticks(np.arange(1,8,1))
ax.set_yticklabels(np.arange(1,8,1),rotation=0)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position(('data', 1820))

plt.xlim(1820,2020)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch3-fig12.eps")
plt.savefig(path, bbox_inches='tight')