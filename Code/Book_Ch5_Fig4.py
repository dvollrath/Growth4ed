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

sRold = .1
sRnew = .5

Tstar=30 # time period when shock occurs
Tmax=200 # time periods to graph

tpre = np.arange(0,Tstar,1)
tall = np.arange(0,Tmax,1) # time periods for old model
tpost = np.arange(Tstar,Tmax,1) # time periods new model

#############################################
## Calculate solutions
#############################################
pre = pr.romer(phi,lam,theta,sRold,gL,A0,L0,tpre) # call for all the values of L at old sR
old = pr.romer(phi,lam,theta,sRold,gL,A0,L0,tall) # call for all the values of L at old sR
Astar = old["AL_ss"]**(1/(1-phi)) # recover actual A level from ss (assuming L = 1)
new = pr.romer(phi,lam,theta,sRnew,gL,Astar,L0,tall) # call for all the values of L at new sR
post = pr.romer(phi,lam,theta,sRnew,gL,Astar,L0,tpost) # call for all the values of L at new sR

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot(old["time"],old["lnA_bgp"], lw=3, color='gray',linestyle='--') # old BGP
ax.plot(new["time"],new["lnA_bgp"], lw=3, color='gray',linestyle='--') # new BGP
ax.plot(pre["time"],pre["lnA_bgp"], lw=3,color='black') # actual GDP pc before change
ax.plot(post["time"],post["lnA"], lw=3,color='black') # actual GDP pc after change

# Options
ax.set_xlim(0,Tmax)
ax.set_xlabel('Time', fontsize=14, loc='right')
ax.set_ylabel(r'Log $A_t$', fontsize=14, rotation=0, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Format ticks
ax.set_yticks([])
ax.set_xticks([Tstar])
ax.set_xticklabels([r'$T^{\ast}$'],size=14)

#pplt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch5-fig4.eps")
plt.savefig(path, bbox_inches='tight')
