import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import statsmodels.api as sm

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Import data and do calculations
##################################################################
pw = f.pwt() # call function to load PWT data,
pw = pw[(pw['relGDPpc']<=120)] # eliminates several outliers

first = 1965 # initial year of analysis
last = 2019 # final year of analysis
diff = last - first

# get "forward" annualized growth rate of GDP per capita
pw['gGDPpc'] = -100*pw.groupby(['countrycode'])['lnGDPpc'].diff(periods=-1*diff)/diff
pw['lnpop'] = np.log(pw['pop']) # log for growth rate
# get "forward" annualized growth rate of population
pw['gpop'] = -1*pw.groupby(['countrycode'])['lnpop'].diff(periods=-1*diff)/diff

mean_csh_i = pw.groupby(['countrycode'])[['csh_i']].mean() # average capital formation share for each country
pw = pw.set_index(['countrycode']) # set index on PWT
pw['mean_csh_i'] = mean_csh_i # merge country averages back to full PWT

# limit dataset to initial year, drop extreme growth values
pwplot = pw[(pw['year']==first) & (pw['gGDPpc']>-2) & (pw['gGDPpc']<=15)].copy()
#pw = pw.set_index(['countrycode']) 

# The following performs a 'partial regression' of the growth rate on initial GDP pc.
#  controlling for capital formation share and population growth
#
# estimate relationship of initial level of GDP per capita to average cap share and population growth
X = pwplot[['mean_csh_i','gpop']]
Y = pwplot['lnGDPpc']
X = sm.add_constant(X)
initial = sm.OLS(Y, X).fit() # OLS of log GDP pc on cap share and pop growth

residuals = initial.resid.rename("residual") # save for using later
residuals = pd.DataFrame(residuals) # make these a data frame for merging
pwplot = pd.merge(pwplot,residuals,on = ['countrycode'],how='inner') # merge residuals back to main data frame

Z = initial.resid # pull the residuals of the above OLS into Z
Y = pwplot['gGDPpc']
Z = sm.add_constant(Z) 
second = sm.OLS(Y, Z).fit() # OLS of growth rate of GDP pc on residuals from first regression

##################################################################
# Plot figure
##################################################################
fig, ax = plt.subplots(figsize=(8,8))

ax.scatter(pwplot['residual'],pwplot['gGDPpc'],c = 'white') # plot growth rate against the residual of initial GDP pc.

for code, dat in pwplot.iterrows(): # label each dot with country code
    ax.annotate(code, (dat['residual'],dat['gGDPpc']))

ax.plot(initial.resid,second.fittedvalues,c='gray') # plot the fitted values from the second regression

ax.set_xlabel(r'Log GDP per capita relative to steady state, ' + str(first), fontsize=14)
ax.set_ylabel('Annual growth rate of GDP per capita (%), ' + str(first) + '-' + str(last), fontsize=14)

#plt.show()
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch3-fig9.eps")
plt.savefig(path, bbox_inches='tight')
