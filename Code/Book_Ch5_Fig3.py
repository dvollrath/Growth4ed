from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['Times New Roman']
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'

import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as pr # pull in common Solow functions

#############################################
## Set up problem
#############################################
phi = 0
lam = 1
theta = .1
gL = .02
L0 = 1
A0 = 1

sRold = .15
sRnew = .3

Tstar=30 # time period when shock occurs
Tmax=150 # time periods to graph

told = np.arange(0,Tstar,1) # time periods for old model
tnew = np.arange(Tstar,Tmax,1) # time periods new model

#############################################
## Calculate solutions
#############################################
old = pr.romer(phi,lam,theta,sRold,gL,A0,L0,told) # call for all the values of L at old sR
Astar = old["AL_ss"]**(1/(1-phi)) # recover actual A level from ss (assuming L = 1)
new = pr.romer(phi,lam,theta,sRnew,gL,Astar,1,tnew) # call for all the values of L at new sR

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot([Tstar-1,Tstar-1], [0,max(new["gA"])], lw=3, color='gray',linestyle='dotted') # show when change happens
ax.plot([0,Tstar-1],[old["gA_ss"],old["gA_ss"]], lw=3, color='black') # old growth rate prior to change
ax.plot(new["time"], new["gA"], lw=3, color='black') # growth rate after change

# Options
ax.set_xlim(0,Tmax)
ax.set_ylim(0,max(new["gA"])+.002)
ax.set_xlabel('Time', fontsize=14, loc='right')
ax.set_ylabel(r'$g_A$', fontsize=14, rotation=0, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Format ticks
ax.set_yticks([old["gA_ss"]])
ax.set_xticks([Tstar-1])
ax.set_xticklabels([r'$T^{\ast}$'],size=14)
ax.set_yticklabels([r'$\frac{\lambda}{1-\phi}g_L$'],size=14)

#plt.show()

# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch5-fig3.eps")
plt.savefig(path, bbox_inches='tight')
