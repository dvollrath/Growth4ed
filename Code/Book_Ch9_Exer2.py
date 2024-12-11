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

tpost = np.arange(Tstar,Tmax,1)

partA = 1*(1-np.exp(-1*.03*(tpost-30))) + 2*np.exp(-1*.03*(tpost-30))
partB = 2*(1-np.exp(-1*.03*(tpost-30))) + 1*np.exp(-1*.03*(tpost-30))

tcpre = np.arange(Tstar,90,1)
tcpost = np.arange(90,150,1)

partCpre =  2*(1-np.exp(-1*.03*(tcpre-30))) + 1*np.exp(-1*.03*(tcpre-30))
partCpost = 1*(1-np.exp(-1*.03*(tcpost-90))) + partCpre[59]*np.exp(-1*.03*(tcpost-90))

#############################################
## Create figures
#############################################

location = os.path.abspath(os.path.dirname(__file__))

fig, (ax1, ax2, ax3) = plt.subplots(3,sharex=True,figsize=(8,8))

# Main elements
ax1.plot([1,30],[1,1], lw=3,color='black',linestyle='-') # actual GDP pc before change
ax1.plot(tpost,partA, lw=3,color='black',linestyle='-') # actual GDP pc after change

ax2.plot([1,30],[1,1], lw=3,color='black',linestyle='-') # actual GDP pc before change
ax2.plot(tpost,partB, lw=3,color='black',linestyle='-') # actual GDP pc after change

ax3.plot([1,30],[1,1], lw=3,color='black',linestyle='-') # actual GDP pc before change
ax3.plot(tcpre,partCpre, lw=3,color='black',linestyle='-') # actual GDP pc after change
ax3.plot(tcpost,partCpost, lw=3,color='black',linestyle='-') # actual GDP pc after change

ax1.set_ylabel(r'$y$', fontsize=10, rotation=0, loc='top')
ax2.set_ylabel(r'$y$', fontsize=10, rotation=0, loc='top')
ax3.set_ylabel(r'$y$', fontsize=10, rotation=0, loc='top')

ax1.set_title("Problem 9.2 (a)", fontsize=16)
ax2.set_title("Problem 9.2 (b)", fontsize=16)
ax3.set_title("Problem 9.2 (c)", fontsize=16)

ax3.set_xticks([Tstar])
ax3.set_xticklabels([r'$T^{\ast}$'],size=14)

path = os.path.join(location, "../Figures/fig-ch9-exer2.eps")
plt.savefig(path, bbox_inches='tight')

#plt.show()

