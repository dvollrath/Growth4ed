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

first = 1950
last = 2019
## read PWT dataset into pw
#na = pd.read_csv('../Data/pwt100.csv')
#ed = pd.read_csv('../Data/pwt100-labor-detail.csv')
#ed = ed[['countrycode','year','yr_sch']]
#pw = pd.merge(na,ed,on = ['countrycode','year'],how='inner')

# Recalculate growth accounting. This is done with national acounts figures, as the table
# only deals with the US over time (there is no cross-country comparison)
#
# This also uses a lower 7% return to education, to match Jones/Fernald
#
pw = pw[(pw['countrycode']=='USA')]
pw['GDPpc'] = pw['rgdpna']/pw['pop'] # create GDP per capita
pw['lfp'] = pw['emp']/pw['pop'] # labor force participation
pw['ky'] = (pw['rnna']/pw['rgdpo'])**(.3/.7) # capital/output to alpha/1-alpha
pw['hc'] = np.exp(.07*pw['yr_sch']) # HC with 7% return
pw['A'] = pw['GDPpc']/(pw['ky']*pw['hc']*pw['lfp']) # residual productivity

# These commands calculate the annualized growth rate of all terms and print them for reference
gGDPpc = (np.log(pw.loc[(pw['year']==last),'GDPpc'].values) - np.log(pw.loc[(pw['year']==first),'GDPpc'].values))/(last-first)
print('GDP per capita: ' + str(gGDPpc))

gky = (np.log(pw.loc[(pw['year']==last),'ky'].values) - np.log(pw.loc[(pw['year']==first),'ky'].values))/(last-first)
print('Capital/output ratio: ' + str(gky))

ghc = (np.log(pw.loc[(pw['year']==last),'hc'].values) - np.log(pw.loc[(pw['year']==first),'hc'].values))/(last-first)
print('Human capital: ' + str(ghc))

glfp = (np.log(pw.loc[(pw['year']==last),'lfp'].values) - np.log(pw.loc[(pw['year']==first),'lfp'].values))/(last-first)
print('Labor force participation: ' + str(glfp))

gA = (np.log(pw.loc[(pw['year']==last),'A'].values) - np.log(pw.loc[(pw['year']==first),'A'].values))/(last-first)
print('Productivity: ' + str(gA))

gpop = (np.log(pw.loc[(pw['year']==last),'pop'].values) - np.log(pw.loc[(pw['year']==first),'pop'].values))/(last-first)
print('Population: ' + str(gpop))