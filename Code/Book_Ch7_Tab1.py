import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions

##################################################################
# Define speciality function to write to output file
##################################################################
def Write(data):
    # sort data passed by GDPpc (descending) for write
    data.sort_values(by="relGDPpc", ascending=False, inplace=True)
    data.reset_index(drop=True, inplace=True)
    
    for index, row in data.iterrows(): # go through each member of passed data
        tcountry = row['country']
        tGDPpc = "{0:.3f}".format(row['relGDPpc'])
        tky = "{0:.3f}".format(row['relky'])
        thc = "{0:.3f}".format(row['relhc'])
        tlfp = "{0:.3f}".format(row['rellfp'])
        tA = "{0:.3f}".format(row['relA'])
        # write formatted fields to output file
        out.write(tcountry + ' & ' + tGDPpc + ' & ' + tky + ' & ' + thc + ' & ' + tlfp + ' & ' + tA + ' \\\\' + '\n')

##################################################################
# Housekeeping for output file
##################################################################
# Open file to write table entries
out = open('../Draft/tab_ch7_tab1.txt', 'w')

##################################################################
# Import data and do calculations
##################################################################
pw = f.pwt() # call function to load PWT data,

# subset the data for writing to the table
pw = pw[(pw['year']==2019)] # just for latest year
pw = pw[['countrycode','country','year','relGDPpc','relky','relhc','rellfp','relA']].copy()
pw.dropna() # drop any row that doesn't have full information, otherwise no summary stats
pw['relGDPpc'] = pw['relGDPpc']/100 # rescale
pw['relky'] = pw['relky']/100 # rescale
pw['relhc'] = pw['relhc']/100 # rescale
pw['rellfp'] = pw['rellfp']/100 # rescale
pw['relA'] = pw['relA']/100 # rescale 

# Calculate and format the means, SD, and coef of variation
meanGDPpc = "{0:.3f}".format(pw['relGDPpc'].mean())
meanky = "{0:.3f}".format(pw['relky'].mean())
meanhc = "{0:.3f}".format(pw['relhc'].mean())
meanlfp = "{0:.3f}".format(pw['rellfp'].mean())
meanA = "{0:.3f}".format(pw['relA'].mean())

sdGDPpc = "{0:.3f}".format(pw['relGDPpc'].std())
sdky = "{0:.3f}".format(pw['relky'].std())
sdhc = "{0:.3f}".format(pw['relhc'].std())
sdlfp = "{0:.3f}".format(pw['rellfp'].std())
sdA = "{0:.3f}".format(pw['relA'].std())

covGDPpc = "{0:.3f}".format(pw['relGDPpc'].std()/pw['relGDPpc'].mean())
covky = "{0:.3f}".format(pw['relky'].std()/pw['relky'].mean())
covhc = "{0:.3f}".format(pw['relhc'].std()/pw['relhc'].mean())
covlfp = "{0:.3f}".format(pw['rellfp'].std()/pw['rellfp'].mean())
covA = "{0:.3f}".format(pw['relA'].std()/pw['relA'].mean())

print(pw['relA'].count()) # for reference in book

##################################################################
# Import data and do calculations
##################################################################

# Go through sets of countries to put into table
report = ['USA','JPN','KOR','DEU','GBR','CAN','MEX','BRA','TUR','CHN','IND','ZAF','NGA','EGY','IDN','KEN','VNM'] # set of countries
pwprint = pw[pw['countrycode'].isin(report)].copy() # select only those countries

# Write initial header to table
out.write('\\\\' + '\n') # add empty row for spacing
out.write('\\multicolumn{6}{l}{Selected countries:} \\\\' + '\n')

Write(pwprint) # call function to write rows for selected countries

out.write('\\\\' + '\n') # add empty row for spacing
out.write('\\multicolumn{6}{l}{Summary statistics over all countries:} \\\\' + '\n')

out.write('Mean & ' + meanGDPpc + ' & ' + meanky + ' & ' + meanhc + ' & ' + meanlfp + ' & ' + meanA + ' \\\\' + '\n')
out.write('Std. Dev. & ' + sdGDPpc + ' & ' + sdky + ' & ' + sdhc + ' & ' + sdlfp + ' & ' + sdA + ' \\\\' + '\n')
out.write('Coef. of Var. & ' + covGDPpc + ' & ' + covky + ' & ' + covhc + ' & ' + covlfp + ' & ' + covA + ' \\\\' + '\n')

out.close() # close output file
