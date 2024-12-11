import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

#############################################
## Set up problem
#############################################
alpha = .2
gA = .02
gL = .01
delta = .04
alpha = .05
A0 = 1
L0 = 1

sIold = .2 # capital formation share prior to change
sInew = .3 # capital formation share after the change

#############################################
## Calculate solutions
#############################################
krange = np.arange(2,5,.1) # range of starting values for K0

old = f.solow(alpha,sIold,delta,gA,gL,krange,A0,L0,0) # solutions with old si
new = f.solow(alpha,sInew,delta,gA,gL,krange,A0,L0,0) # solutions with new si
init = f.solow(alpha,sInew,delta,gA,gL,old["KAL_ss"],A0,L0,0) # new solution at old s.s.

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Plots of gK and gA+gL lines
ax.plot(old["KAL"], old["gK"], lw=3, color='black')
ax.plot(new["KAL"], new["gK"], lw=3, color='gray')
ax.plot([2,max(old["KAL"])],[gA+gL,gA+gL],lw=3,color='black',linestyle='dashed')

# Showing movement of KAL from one s.s. to another
ax.plot(np.linspace(old["KAL_ss"]+.1,new["KAL_ss"]-.1,num=5),[0,0,0,0,0],'k>') # arrows on axis
ax.plot([new["KAL_ss"],new["KAL_ss"]],[0,gA+gL],lw=2,color='black',linestyle='dotted') # new s.s.
ax.plot([init["KAL_init"],init["KAL_init"]],[0,init["gK"]],lw=2,color='black',linestyle='dotted') # old s.s
ax.plot(init["KAL_init"],init["gK"],'o',markersize=10,color='gray') # initial growth rate
ax.plot(old["KAL_ss"],gA+gL,'ok',markersize=10) # old growth rate
ax.plot(new["KAL_ss"],gA+gL,'o',markersize=10,color='gray') # new growth rate

# Arrow showing shift of gK curve
ax.arrow(old["KAL_ss"]-.2,gA+gL+.01,0,.025,color='gray',head_width = 0.05,head_length=0.001)

# Add text
ax.annotate(r'$g_K = s^{\prime}_I\left(\frac{A_tL_t}{K_t}\right)^{1-\alpha} - \delta$', xy=(old["KAL_ss"],init["gK"]+.01), size=16)
ax.annotate(r'$g_A + g_L$', xy=(min(old["KAL"]),gA+gL+.003), size=16)

# Options
ax.set_xlabel(r'$\frac{K_t}{A_tL_t}$', fontsize=20, loc='right')
ax.set_ylabel('Growth rate', fontsize=16, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))

# Format ticks
ax.set_yticks([0])
ax.set_yticklabels(['0'],size=16)
ax.set_xticks([old["KAL_ss"],new["KAL_ss"]])
ax.set_xticklabels([r'$\left(\frac{K}{AL}\right)^{ss}_{old}$',r'$\left(\frac{K}{AL}\right)^{ss}_{new}$'],size=16)

#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch2-fig3.eps")
plt.savefig(path, bbox_inches='tight')
