import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

#############################################
## Set up problem
#############################################
Tmax = 100

alpha = .2 # relatively low to make figure look good
gA = .002
gL = .01
delta = .05
A0 = 1
L0 = 1
K0 = 1
sI = .2

t= np.arange(0,Tmax,1)

#############################################
## Calculate solutions
#############################################
ss = f.solow(alpha,sI,delta,gA,gL,K0,A0,L0,t) # solution with old si prior to change
above = f.solow(alpha,sI,delta,gA,gL,ss["KAL_ss"]+2,A0,L0,t) # full solutions with old si to show BGP
below = f.solow(alpha,sI,delta,gA,gL,ss["KAL_ss"]-2,A0,L0,t) # solutions with new si, starting at old s.s

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot(ss["time"],ss["lny_bgp"], lw=3, color='black',linestyle='-') # BGP
ax.plot(above["time"],above["lny"], lw=3, color='gray',linestyle='--') # starts above BGP
ax.plot(below["time"],below["lny"], lw=3,color='gray',linestyle='--') # starts below BGP

ax.annotate(r'$\ln X(t)^{ss} = \left[\ln Z(0) + \ln \frac{\phi}{\beta+\delta}\right] + \beta t$',xy=(Tmax-50,max(ss["lny_bgp"])),size=16)
# Options
ax.set_xlim(0,Tmax)
ax.set_xlabel('Time (t)', fontsize=14, loc='right')
ax.set_ylabel('Log X(t)', fontsize=14, rotation=0, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Format ticks
ax.set_yticks([])
ax.set_xticks([])


#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-chapp-fig2.eps")
plt.savefig(path, bbox_inches='tight')
