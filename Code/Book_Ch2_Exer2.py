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

tpost = np.arange(Tstar,Tmax,1) # time periods after change
tall = np.arange(0,Tmax,1) # all time periods
tshift = np.arange(0,Tmax - Tstar,1)

#############################################
## Create figures
#############################################

location = os.path.abspath(os.path.dirname(__file__))

# A: drop in cap investment rate
pre = f.solow(alpha = .4, si = .4, t = tall) # high inv rate
post = f.solow(alpha = .4, si = .2, k0 = pre["KAL_ss"], t = tpost) # low inv rate
f.trifigure(pre,post,Tstar,Tmax,"Exercise 2.2.a")
path = os.path.join(location, "../Figures/fig-ch2-exer2a.eps")
plt.savefig(path, bbox_inches='tight')

# B: increase in population growth
pre = f.solow(alpha = .4, gl = .01, t = tall) # high inv rate
post = f.solow(alpha = .4, gl = .06, k0 = pre["KAL_ss"], t = tpost) # low inv rate
f.trifigure(pre,post,Tstar,Tmax,"Exercise 2.2.b")
path = os.path.join(location, "../Figures/fig-ch2-exer2b.eps")
plt.savefig(path, bbox_inches='tight')

# C: increase in productivity growth
pre = f.solow(alpha = .6, ga = .02, t = tall) # low productivity growth
preA = np.exp(Tstar*.02) # productivity at Tstar
preK = pre["KAL_ss"]*preA # K at Tstar given productivity
post = f.solow(alpha = .6, ga = .06, k0 = preK, a0 = preA, t = tshift) # high productivity growth
# this function is called from time zero forward, otherwise it will add in "old" productivity growth

post["time"] = post["time"] + Tstar # move up in time
f.trifigure(pre,post,Tstar,Tmax,"Exercise 2.2.c")
path = os.path.join(location, "../Figures/fig-ch2-exer2c.eps")
plt.savefig(path, bbox_inches='tight')

