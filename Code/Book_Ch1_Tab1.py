import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##################################################################
# Output setup and write function
##################################################################
# Open file to write table entries
out = open('../Draft/tab_ch1_tab1.txt', 'w')

# define functions to write output
def Write(title,data):
    out.write('\\multicolumn{6}{l}{' + title + '} \\\\' + '\n') # write title of section

    # sort data passed by GDPpc (descending) for write
    data.sort_values(by="GDPpc", ascending=False, inplace=True)
    data.reset_index(drop=True, inplace=True)
    
    for index, row in data.iterrows(): # go through each member of passed data
        tcountry = row['country'] # format fields
        tGDPpc = "{0:,}".format(round(row['GDPpc']))
        tGDPpw = "{0:,}".format(round(row['GDPpw']))
        tlfp = "{0:.2f}".format(row['lfp'])
        tgGDPpc = "{0:.1f}".format(100*row['glnGDPpc'])
        tdblGDPpc = "{0:}".format(round(row['dblGDPpc']))
        # write formatted fields to output file
        out.write(tcountry + ' & ' + tGDPpc + ' & ' + tGDPpw + ' & ' + tlfp + ' & ' + tgGDPpc + ' & ' + tdblGDPpc + ' \\\\' + '\n')

##################################################################
# Import data and do calculations
##################################################################
pw = f.pwt() # call function to load PWT data

# Set cutoffs for periods to look at
first = 1960
last = 2019
diff = last - first # time span

pw.sort_values(by=['countrycode', 'year']) # organize by country/year

# calculate growth rates and doubling time
# groups by country, growth rates via log differences
pw['glnGDPpc'] = pw.groupby(['countrycode'])['lnGDPpc'].diff(periods=diff)/diff 
pw['glnGDPpw'] = pw.groupby(['countrycode'])['lnGDPpw'].diff(periods=diff)/diff
pw['dblGDPpc'] = np.log(2)/np.log(1+pw['glnGDPpc'])

##################################################################
# Write table file
##################################################################
out.write('\\\\' + '\n') # add empty row for spacing

# Go through sets of countries to put into table
rich = ['USA','JPN','FRA'] # set of rich countries
pwprint = pw[(pw['year']==2019) & pw['countrycode'].isin(rich)] # select only those countries
Write("Relatively rich countries:",pwprint) # call function to write rows
out.write('&&&&& \\\\' + '\n') # add empty row for spacing

middle = ['MEX','CHL','TUR']
pwprint = pw[(pw['year']==2019) & pw['countrycode'].isin(middle)]
Write("Middle income countries:",pwprint) # call function to write rows
out.write('&&&&& \\\\' + '\n') # add empty row for spacing

poor = ['CHN','IND','MWI']
pwprint = pw[(pw['year']==2019) & pw['countrycode'].isin(poor)]
Write("Relatively poor countries:",pwprint) # call function to write rows
out.write('&&&&& \\\\' + '\n') # add empty row for spacing

miracle = ['TWN','KOR','SGP']
pwprint = pw[(pw['year']==2019) & pw['countrycode'].isin(miracle)]
Write("Growth miracles:",pwprint) # call function to write rows
out.write('&&&&& \\\\' + '\n') # add empty row for spacing

disaster = ['VEN','NER','MDG']
pwprint = pw[(pw['year']==2019) & pw['countrycode'].isin(disaster)]
Write("Growth disasters:",pwprint) # call function to write rows

out.close()
