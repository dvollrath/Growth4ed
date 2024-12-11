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
sI = .2
gA = .02
delta = .04
alpha = .05
A0 = 1
L0 = 1

gLold = .04 # pop growth rate prior to change
gLnew = .01 # pop growth rate after the change

#############################################
## Calculate solutions
#############################################
krange = np.arange(1,5,.1) # range of starting values for K0

old = f.solow(alpha,sI,delta,gA,gLold,krange,A0,L0,0) # solution with old gL
new = f.solow(alpha,sI,delta,gA,gLnew,krange,A0,L0,0) # solution with new gL
init = f.solow(alpha,sI,delta,gA,gLnew,old["KAL_ss"],A0,L0,0) # new solution at old s.s.

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot(old["KAL"], old["gK"], lw=3, color='black') # plot growth rate of K
ax.plot([min(old["KAL"]),max(old["KAL"])],[gA+gLold,gA+gLold],lw=3,color='black',linestyle='dashed') # old gL + gA
ax.plot([min(old["KAL"]),max(old["KAL"])],[gA+gLnew,gA+gLnew],lw=3,color='gray',linestyle='dashed') # new gL + gA

# Movement from one ss to the next
ax.plot([old["KAL_ss"],old["KAL_ss"]],[0,gA+gLold],lw=2,color='black',linestyle='dotted')
ax.plot([new["KAL_ss"],new["KAL_ss"]],[0,gA+gLnew],lw=2,color='gray',linestyle='dotted')
ax.plot(np.linspace(old["KAL_ss"]+.1,new["KAL_ss"]-.1,num=5),[0,0,0,0,0],'k>')
ax.plot(init["KAL_init"],init["gK"],'o',markersize=10,color='gray') # initial growth rate
ax.plot(old["KAL_ss"],gA+gLold,'ok',markersize=10) # old growth rate
ax.plot(new["KAL_ss"],gA+gLnew,'o',markersize=10,color='gray') # new growth rate

ax.arrow(.8*max(old["KAL"]),gA+gLold-.005,0,-.02,color='gray',head_width = 0.05,head_length=0.001)

# Add text
ax.annotate(r'$g_K = s_K\left(\frac{A_tL_t}{K_t}\right)^{1-\alpha} - \delta$', xy=(old["KAL_ss"]-.2,init["gK"]+.02), size=16)
ax.annotate(r'$g_A + g_L$', xy=(.9*max(old["KAL"]),gA+gLold+.003), size=16)
ax.annotate(r'$g_A + g_L^{\prime}$', xy=(.9*max(old["KAL"]),gA+gLnew+.003), size=16)

# Options
ax.set_xlim(min(old["KAL"])-.1,max(old["KAL"]))
ax.set_ylim(-.01,.1)
ax.set_xlabel(r'$K_t/A_tL_t$', fontsize=20, loc='right')
ax.set_ylabel('Growth rate', fontsize=16, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))

# Format ticks
ax.set_yticks([0])
ax.set_yticklabels(['0'],size=16)
ax.set_xticks([new["KAL_ss"],old["KAL_ss"]])
ax.set_xticklabels([r'$\left(\frac{K}{AL}\right)^{ss}_{new}$',r'$\left(\frac{K}{AL}\right)^{ss}_{old}$'],size=16)

#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch2-fig6.eps")
plt.savefig(path, bbox_inches='tight')

