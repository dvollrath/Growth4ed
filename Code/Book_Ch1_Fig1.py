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
pw = pw[(pw['year']==2019)] # limit to 2019
pw.sort_values(by=['relGDPpc'],inplace=True) # sort by relative GDP pc
pw['cumpop'] = 100*pw['pop'].cumsum()/pw['pop'].sum() # calculate cumulative population by rel GDP pc

# save information on three countries to label in figure
labelCHNx = pw.loc[(pw['countrycode']=='CHN'),'relGDPpc'].values
labelCHNy = pw.loc[(pw['countrycode']=='CHN'),'cumpop'].values
labelINDx = pw.loc[(pw['countrycode']=='IND'),'relGDPpc'].values
labelINDy = pw.loc[(pw['countrycode']=='IND'),'cumpop'].values
labelUSAx = pw.loc[(pw['countrycode']=='USA'),'relGDPpc'].values
labelUSAy = pw.loc[(pw['countrycode']=='USA'),'cumpop'].values

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.plot(pw['relGDPpc'], pw['cumpop'], lw=3, color='black') # Cum pop (y) versus GDPpc (x)

ax.set_xlabel('GDP per capita relative to the United States', fontsize=14)
ax.set_ylabel('Percent of world population', fontsize=14)
ax.set_xticks([0,10,20,30,40,50,60,70,80,90,100,110,120])
ax.set_xticklabels([0,10,20,30,40,50,60,70,80,90,100,110,120])
ax.set_yticks([0,10,20,30,40,50,60,70,80,90,100])
ax.set_yticklabels([0,10,20,30,40,50,60,70,80,90,100],rotation=0)

# Annotate the three example
ax.annotate('China',xy=(labelCHNx,labelCHNy-5), xytext=(labelCHNx+5,labelCHNy-10),
	arrowprops=dict(arrowstyle= '->',
                             color='black',
                             lw=1.5),
	size=12)
ax.annotate('India',xy=(labelINDx,labelINDy-5), xytext=(labelINDx+5,labelINDy-10),
	arrowprops=dict(arrowstyle= '->',
                             color='black',
                             lw=1.5),
	size=12)
ax.annotate('U.S.',xy=(labelUSAx,labelUSAy-1), xytext=(labelUSAx+5,labelUSAy-10),
	arrowprops=dict(arrowstyle= '->',
                             color='black',
                             lw=1.5),
	size=12)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch1-fig1.eps")
plt.savefig(path, bbox_inches='tight')
