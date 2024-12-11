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

# A: drop in sR
pre = f.romer(sR = .05, gL = .05, t = tall)
post = f.romer(sR = .01, gL = .05, t = tpost)
ypre = f.solow(alpha = .4, a0 = np.exp(pre["lnA"])) # 
ypost = f.solow(alpha = .4, a0 = np.exp(post["lnA"])) # 
f.prodfigure(pre,post,ypre,ypost,Tstar,Tmax,"Exercise 5.2.a")

path = os.path.join(location, "../Figures/fig-ch5-exer2a.eps")
plt.savefig(path, bbox_inches='tight')


# B: increase in gL
pre = f.romer(sR = .01, gL = .01, t = tall)
post = f.romer(sR = .01, gL = .05, A0 = np.exp(pre["lnA_bgp"][Tstar]), L0 = 1.01**Tstar, t = tshift)
post["time"] = Tstar + post["time"]
ypre = f.solow(alpha = .4, a0 = np.exp(pre["lnA"])) # 
ypost = f.solow(alpha = .4, a0 = np.exp(post["lnA"])) # 
f.prodfigure(pre,post,ypre,ypost,Tstar,Tmax,"Exercise 5.2.b")

path = os.path.join(location, "../Figures/fig-ch5-exer2b.eps")
plt.savefig(path, bbox_inches='tight')

# C: increase in theta
pre = f.romer(lamb=2, theta = 1, t = tall)
post = f.romer(lamb=2, theta = 1.5, A0 = np.exp(pre["lnA_bgp"][Tstar]), L0 = 1.01**Tstar, t = tshift)
post["time"] = Tstar + post["time"]
ypre = f.solow(alpha = .4, a0 = np.exp(pre["lnA_bgp"])) # 
ypost = f.solow(alpha = .4, a0 = np.exp(post["lnA"])) # 
f.prodfigure(pre,post,ypre,ypost,Tstar,Tmax,"Exercise 5.2.c")

path = os.path.join(location, "../Figures/fig-ch5-exer2c.eps")
plt.savefig(path, bbox_inches='tight')

#plt.show()



