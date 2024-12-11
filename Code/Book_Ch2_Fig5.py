import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

#############################################
## Set up problem
#############################################
Tstar=30 # time period when shock occurs
Tmax=150 # time periods to graph

alpha = .2 # relatively low to make figure look good
gA = .002
gL = .01
delta = .05
A0 = 1
L0 = 1
K0 = 1

sIold = .2
sInew = .3

tpre = np.arange(0,Tstar,1)
tall = np.arange(0,Tmax,1) # time periods for old model
tpost = np.arange(Tstar,Tmax,1) # time periods new model

#############################################
## Calculate solutions
#############################################
pre = f.solow(alpha,sIold,delta,gA,gL,K0,A0,L0,tpre) # solution with old si prior to change
old = f.solow(alpha,sIold,delta,gA,gL,K0,A0,L0,tall) # full solutions with old si to show BGP
post = f.solow(alpha,sInew,delta,gA,gL,old["KAL_ss"],1,1,tpost) # solutions with new si, starting at old s.s
new = f.solow(alpha,sInew,delta,gA,gL,old["KAL_ss"],1,1,tall) # full solutions with new si to show BGP

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot(old["time"],old["lny_bgp"], lw=3, color='gray',linestyle='--') # old BGP
ax.plot(new["time"],new["lny_bgp"], lw=3, color='gray',linestyle='--') # new BGP
ax.plot(pre["time"],pre["lny_bgp"], lw=3,color='black',linestyle='-') # actual GDP pc before change
ax.plot(post["time"],post["lny"], lw=3,color='black',linestyle='-') # actual GDP pc after change

# Options
ax.set_xlim(0,Tmax)
ax.set_xlabel('Time', fontsize=14, loc='right')
ax.set_ylabel(r'Log $y_t$', fontsize=14, rotation=0, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Format ticks
ax.set_yticks([])
ax.set_xticks([Tstar])
ax.set_xticklabels([r'$T^{\ast}$'],size=14)

#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch2-fig5.eps")
plt.savefig(path, bbox_inches='tight')
