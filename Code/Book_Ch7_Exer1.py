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
    data.sort_values(by="country", ascending=False, inplace=True)
    data.reset_index(drop=True, inplace=True)
    
    for index, row in data.iterrows(): # go through each member of passed data
        tcountry = row['country']
        tGDP = "{0:,.0f}".format(row['rgdpo'])
        tpop = "{0:.1f}".format(row['pop'])
        temp = "{0:.1f}".format(row['emp'])
        tK = "{0:,.0f}".format(row['cgdpo'])
        tyr = "{0:.1f}".format(row['yr_sch'])

        # write formatted fields to output file
        out.write(tcountry + ' & ' + tGDP + ' & ' + tpop + ' & ' + temp + ' & ' + tK + ' & ' + tyr + ' \\\\' + '\n')

##################################################################
# Housekeeping for output file
##################################################################
# Open file to write table entries
out = open('../Draft/tab_ch7_hw1.txt', 'w')

##################################################################
# Import data and do calculations
##################################################################
pw = f.pwt() # call function to load PWT data,

# subset the data for writing to the table
pw = pw[(pw['year']==2019)] # just for latest year
pw = pw[['countrycode','country','year','rgdpo','pop','emp','cgdpo','yr_sch']].copy()
pw.dropna() # drop any row that doesn't have full information, otherwise no summary stats

##################################################################
# Import data and do calculations
##################################################################

# Go through sets of countries to put into table
report = ['USA','IDN','MYS','PAK','CHL','COL','BWA']
pwprint = pw[pw['countrycode'].isin(report)].copy() # select only those countries

# Write initial header to table
out.write('\\\\' + '\n') # add empty row for spacing

Write(pwprint) # call function to write rows for selected countries

out.close() # close output file
