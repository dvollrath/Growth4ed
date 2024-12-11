import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

def updatesolow(passed): # function takes solow dictionary as argument
	updated = passed # copy passed dictionary of values to new dictionary to start
	hold = passed["y"] # hold GDP pc value for use in calculation

	# calculate values of stocks and various ratios based on them
	updated["K"] = passed["sI"]*passed["Y"] + (1 - passed["delta"])*passed["K"] # accum capital
	updated["L"] = (1+passed["gL"])*passed["L"] # labor growth
	updated["A"] = (1+passed["gA"])*passed["A"] # productivity growth
	updated["KAL"] = updated["K"]/(updated["A"]*updated["L"]) # K/AL ratio
	updated["Y"] = updated["K"]**updated["alpha"]*(updated["L"]*updated["A"])**(1-updated["alpha"]) # GDP
	updated["y"] = updated["Y"]/updated["L"] # GDP per capita
	updated["gy"] = updated["y"]/hold - 1 # growth rate of GDP per capita

	# calculate hypothetical steady state and BGP given passed values
	updated["KALss"] = (updated["sI"]/(updated["gA"]+updated["gL"]+updated["delta"]))**(1/(1-updated["alpha"]))
	updated["ybgp"] = updated["KALss"]**updated["alpha"]*updated["A"]

	return updated # pass updated dictionary back to calling program

#############################################
## Set up time periods
#############################################
Tstar=30 # time period when shock occurs
Tmax=150 # time periods to graph

#############################################
## Set up baseline solow dictionary
#############################################
# This is a dictionary of lists. The lists will be of values over time periods
solow = {"t": [], "sI": [], "gA": [], "gL": [], "delta": [], "alpha": [], "A": [], "L": [], 
	"K": [], "Y": [], "KALss": [], "y": [], "ybgp": [], "gy": [], "KAL": []}

# This is a dictionary of initial values of different parameters
old = {"sI": .2, "gA": .02, "gL": .01, "delta": .05, "alpha": .4, "A": 1, "L": 1}
# Calculate capital assuming at steady state, and GDP using A, K, L and alpha values
old["KALss"] = (old["sI"]/(old["gA"]+old["gL"]+old["delta"]))**(1/(1-old["alpha"])) # set to SS value
old["K"] = old["A"]*old["L"]*old["KALss"] # set to SS value
old["KAL"] = old["K"]/(old["A"]*old["L"]) # calculate, but trivially equal to SS value
old["Y"] = old["K"]**old["alpha"]*(old["A"]*old["L"])**(1-old["alpha"]) # calculate GDP
old["y"] = old["Y"]/old["L"] # calcutate GDP per capita
old["ybgp"] = old["KALss"]**old["alpha"]*old["A"] # calculate BGP GDP per capita
old["gy"] = old["gA"] # initialize growth rate

#############################################
## Loop through periods
#############################################

for t in range(0,Tmax): # do this for the specified number of period
	for key, value in old.items(): # populate solow lists with values in "old"
		solow[key].append(value)
	solow["t"].append(t) # population time period in solow list
	old = updatesolow(old) # update values to next period
	if t >= Tstar: # check for shock
		old["sI"] = .1 # apply shock

#############################################
## Create figures
#############################################

#location = os.path.abspath(os.path.dirname(__file__))

fig, (ax1, ax2, ax3) = plt.subplots(3,sharex=True,figsize=(8,8))

ax1.plot(solow["t"],np.log(solow["ybgp"]), lw=3, color='gray',linestyle='--') # BGP GDP pc
ax1.plot(solow["t"],np.log(solow["y"]), lw=3, color='black',linestyle='-') # Actual GDP pc

ax2.plot(solow["t"],solow["gA"], lw=3, color='gray',linestyle='--') # BGP growth rate
ax2.plot(solow["t"],solow["gy"], lw=3, color='black',linestyle='-') # Actual growth rate

ax3.plot(solow["t"],solow["KALss"], lw=3, color='gray',linestyle='--') # BGP KAL
ax3.plot(solow["t"],solow["KAL"], lw=3, color='black',linestyle='-') # Actual KAL

ax1.set_ylabel(r'Log $y$', fontsize=10, rotation=0, loc='top')
ax2.set_ylabel(r'$g_y$', fontsize=10, rotation=0, loc='top')
ax3.set_ylabel(r'$K/AL$', fontsize=10, rotation=0, loc='top')

ax1.set_title("Exercise 2.2.a", fontsize=16)

plt.show()
