import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Import data and do calculations
##################################################################
pw = f.pwt() # call function to load PWT data,
pw = pw[(pw['relGDPpc']<=120)] # eliminates several outliers

first = 1960 # initial year of analysis
last = 2019 # final year of analysis

# subset first and last years and drop outliers
pwlast = pw[(pw['year']==last) & (pw['lnGDPpc']>=6.5)].copy() 
pwfirst = pw[(pw['year']==first) & (pw['lnGDPpc']>=6.5)].copy()

xticks = np.log([500,1000,2000,4000,8000,16000,32000,64000,128000]) # for dividing histogram
xlabels = ['500','1,000','2,000','4,000','8,000','16,000','32,000','64,000','128,000'] # associated labels

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

# histogram for both years, using total population to weight size of bars, x divided on log GDP pc
ax.hist([pwfirst['lnGDPpc'],pwlast['lnGDPpc']],weights=[pwfirst['pop'],pwlast['pop']],
	color=['black','gray'],bins=xticks,
	label=[first,last]) 

ax.set_xlabel('GDP per capita (Intl $, ratio scale)', fontsize=14)
ax.set_ylabel('Population (ratio scale)', fontsize=14)
ax.legend(loc="upper right",fontsize=14)
ax.semilogy()

ax.set_xticks(xticks)
ax.set_xticklabels(xlabels)
ax.set_yticks([25,50,100,250,500,1000,2000])
ax.set_yticklabels(['25mil','50mil','100mil','250mil','500mil', '1bn', '2bn'])

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch3-fig11.eps")
plt.savefig(path, bbox_inches='tight')
