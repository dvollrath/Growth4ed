import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.plot([2,2],[0,9],color='black')
ax.plot([6,6],[0,9],color='black')
ax.plot([10,10],[0,9],color='black')
ax.plot([2,10],[9,9],color='black')
ax.plot([2,10],[0,0],color='black')
ax.arrow(1,5.5,0,3,head_width = 0.25,head_length=0.25,color ='black')
ax.arrow(1,4,0,-3,head_width = 0.25,head_length=0.25,color ='black')

ax.annotate('Rivalrous goods',xy=(4,10),size=14, ha='center')
ax.annotate('Nonrivalrous goods',xy=(8,10),size=14, ha='center')
ax.annotate('Degree of',xy=(1,5),size=14, ha='center')
ax.annotate('Excludability',xy=(1,4.5),size=14, ha='center')
ax.annotate('Low',xy=(1,.3),size=10, ha='center')
ax.annotate('High',xy=(1,9),size=10, ha='center')

ax.annotate('Legal services',xy=(4,8),size=12, ha='center')
ax.annotate('Smartphone',xy=(4,7),size=12, ha='center')
ax.annotate('Fish in the ocean',xy=(4,2),size=12, ha='center')
ax.annotate('Bee pollination',xy=(4,1),size=12, ha='center')

ax.annotate('Encrypted TV show',xy=(8,8),size=12, ha='center')
ax.annotate('Open source software',xy=(8,6),size=12, ha='center')
ax.annotate('Wal-mart operations',xy=(8,4),size=12, ha='center')
ax.annotate('manual',xy=(8,3.5),size=12, ha='center')
ax.annotate('National defense',xy=(8,2),size=12, ha='center')
ax.annotate('Basic R&D',xy=(8,1.5),size=12, ha='center')
ax.annotate('Calculus',xy=(8,1),size=12, ha='center')

ax.set_ylim(0,11)
ax.set_xlim(0,11)
ax.axis('off')

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch4-fig4.eps")
plt.savefig(path, bbox_inches='tight')
