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

# A: Increase in population
pre = f.solow(alpha = .4, t = tall) # before
post = f.solow(alpha = .4, l0 = 1.5, t = tpost) # shock to starting population
f.trifigure(pre,post,Tstar,Tmax,"Exercise 2.3.a")
path = os.path.join(location, "../Figures/fig-ch2-exer3a.eps")
plt.savefig(path, bbox_inches='tight')

# B: decrease in capital 
pre = f.solow(alpha = .4, t = tall) # before
post = f.solow(alpha = .4, k0 = .5, t = tpost) # low inv rate
f.trifigure(pre,post,Tstar,Tmax,"Exercise 2.3.b")
path = os.path.join(location, "../Figures/fig-ch2-exer3b.eps")
plt.savefig(path, bbox_inches='tight')

# C: increase in productivity growth
pre = f.solow(alpha = .4, t = tall) # low productivity growth
preA = np.exp(Tstar*.02) # productivity at Tstar
preL = np.exp(Tstar*.01) # population at Tstar
preK = pre["KAL_ss"]*preA*preL # K at Tstar given productivity and labor
post = f.solow(alpha = .4, k0 = preK, a0 = preA*1.5, l0 = preL, t = tpost) # high productivity growth
f.trifigure(pre,post,Tstar,Tmax,"Exercise 2.3.c")
path = os.path.join(location, "../Figures/fig-ch2-exer3c.eps")
plt.savefig(path, bbox_inches='tight')

