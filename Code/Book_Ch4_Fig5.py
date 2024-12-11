import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

#############################################
## Set up values
#############################################
Y = np.linspace(1,10,num=100) # output
P = 1 # marginal cost
F = 9 # fixed cost

Acost = P + F/Y # average costs
Mcost = P*(Y/Y) # marginal cost

#############################################
## Plot figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot(Y, Acost, lw=3, color='black') # plot growth rate of K
ax.plot(Y, Mcost, lw=3, color='black') # plot growth rate of K

# Add text
ax.annotate('Average cost', xy=(4,4),size=16)
ax.annotate('Marginal cost', xy=(2,1.5),size=16)

# Options
ax.set_xlim(0,10)
ax.set_ylim(0,11)
ax.set_xlabel('Units produced', fontsize=16, loc='right')
ax.set_ylabel('Costs', fontsize=16, loc='top',rotation=0)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xticks([1])
ax.set_xticklabels([1],size=16)
ax.set_yticks([F+1])
ax.set_yticklabels(['F'],size=16)

#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch4-fig5.eps")
plt.savefig(path, bbox_inches='tight')
