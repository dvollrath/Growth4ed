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
out = open('../Draft/tab_ch7_hw1ans.txt', 'w')

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

##################################################################
# Import data and do calculations
##################################################################

# Go through sets of countries to put into table
report = ['USA','IDN','MYS','PAK','CHL','COL','BWA'] # set of countries
pwprint = pw[pw['countrycode'].isin(report)].copy() # select only those countries

# Write initial header to table
out.write('\\\\' + '\n') # add empty row for spacing
out.write('\\multicolumn{6}{l}{Selected countries:} \\\\' + '\n')

Write(pwprint) # call function to write rows for selected countries


out.close() # close output file
