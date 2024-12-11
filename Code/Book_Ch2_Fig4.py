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
Tmax=100 # time periods to graph

alpha = .2 # relatively low to make figure look good
gA = .002
gL = .01
delta = .05
A0 = 1
L0 = 1
K0 = 1

sIold = .2
sInew = .22

told = np.arange(0,Tstar,1) # time periods for old model
tnew = np.arange(Tstar,Tmax,1) # time periods new model

#############################################
## Calculate solutions
#############################################
old = f.solow(alpha,sIold,delta,gA,gL,K0,A0,L0,told) # full solutions with old si
new = f.solow(alpha,sInew,delta,gA,gL,old["KAL_ss"],1,1,tnew) # solutions with new si, starting at old s.s

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot([Tstar-1,Tstar-1], [0,max(new["gy"])], lw=3, color='gray',linestyle='dotted') # show when change happens
ax.plot([0,Tstar-1],[gA,gA], lw=3, color='black') # old growth rate prior to change
ax.plot(new["time"], new["gy"], lw=3, color='black',linestyle='-') # growth rate after change

# Options
ax.set_xlim(0,Tmax)
ax.set_ylim(0,max(new["gy"])+.002)
ax.set_xlabel('Time', fontsize=14, loc='right')
ax.set_ylabel(r'$g_y$', fontsize=14, rotation=0, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Format ticks
ax.set_yticks([gA])
ax.set_xticks([Tstar-1])
ax.set_xticklabels([r'$T^{\ast}$'],size=14)
ax.set_yticklabels([r'$g_A$'],size=14)

#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch2-fig4.eps")
plt.savefig(path, bbox_inches='tight')
