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

# subset first and last years
pwlast = pw[(pw['year']==2019)].copy() 
pwfirst = pw[(pw['year']==1960)].copy()

worldpop = pwlast['pop'].sum() # world population
pwlast['percpop'] = 100*pwlast['pop']/worldpop # percent of world population

worldpop = pwfirst['pop'].sum() # world population
pwfirst['percpop'] = 100*pwfirst['pop']/worldpop # percent of world population

# These print statements are for information used in the book
print('Number of countries in 1960: ',len(pwfirst))
print('Singapore relative GDPpc in 1960: ', pwfirst.loc[(pwfirst['countrycode']=='SGP'),'relGDPpc'].values)
print('Singapore relative GDPpc in 2019: ', pwlast.loc[(pwlast['countrycode']=='SGP'),'relGDPpc'].values)

print('China relative GDPpc in 1960: ', pwfirst.loc[(pwfirst['countrycode']=='CHN'),'relGDPpc'].values)
print('China relative GDPpc in 2019: ', pwlast.loc[(pwlast['countrycode']=='CHN'),'relGDPpc'].values)
print('India relative GDPpc in 1960: ', pwfirst.loc[(pwfirst['countrycode']=='IND'),'relGDPpc'].values)
print('India relative GDPpc in 2019: ', pwlast.loc[(pwlast['countrycode']=='IND'),'relGDPpc'].values)

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.hist([pwfirst['relGDPpc'],pwlast['relGDPpc']],range(0,110,10),weights=[pwfirst['percpop'],pwlast['percpop']],
	color=['black','gray'],label=['1960','2019']) # plot both histograms of weighted shares of world pop
ax.set_xlabel('GDP per capita relative to the United States', fontsize=14)
ax.set_ylabel('Percent of world population', fontsize=14)
ax.legend(loc="upper right",fontsize=14)
ax.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
ax.set_xticklabels([0,10,20,30,40,50,60,70,80,90,100])

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch1-fig2.eps")
plt.savefig(path, bbox_inches='tight')
