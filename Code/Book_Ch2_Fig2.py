import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

##############################################
## Set up parameters - chosen to make clear figure
#############################################
gA = .02
gL = .01
delta = .06
sI = .2
alpha = .05
A0 = 1
L0 = 1

#############################################
## Calculate solutions
#############################################
krange = np.arange(1,4,.1) # range of starting values for K0

# Get solutions to Solow for all the different starting values of K0
s = f.solow(alpha,sI,delta,gA,gL,krange,A0,L0,0)

# Get solution to Solow for single starting value of K0 = 1.2 for plotting initial value
init = f.solow(alpha,sI,delta,gA,gL,1.2,A0,L0,0)

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot([1,max(s["KAL"])],[gA+gL,gA+gL],lw=3,color='gray',linestyle='dashed')
ax.plot(s["KAL"], s["gK"], lw=3, color='black')
ax.plot([s["KAL_ss"],s["KAL_ss"]],[0,gA+gL],lw=2,color='black',linestyle='dotted')
ax.plot([init["KAL_init"],init["KAL_init"]],[0,init["gK"]],lw=2,color='black',linestyle='dotted')
ax.plot(np.linspace(init["KAL_init"]+.1,init["KAL_ss"]-.1,num=5),[0,0,0,0,0],'k>')

# Add text
ax.annotate(r'$g_K = s_K\left(\frac{A_tL_t}{K_t}\right)^{1-\alpha} - \delta$', xy=(init["KAL_init"]+.1,init["gK"]), size=16)
ax.annotate(r'$g_A + g_L$', xy=(.8*max(s["KAL"]),gA+gL+.003), size=16)
ax.annotate(r'$\frac{K_t}{A_tL_t}$ is falling',xy=(.8*max(s["KAL"]),gA+gL-.01), size=16)
ax.annotate(r'$\frac{K_t}{A_tL_t}$ is rising',xy=(1.3*min(s["KAL"]),gA+gL+.01), size=16)

# Options
ax.set_xlim(min(s["KAL"])-.1,max(s["KAL"]))
ax.set_ylim(min(s["gK"])-.005,max(s["gK"])+.005)
ax.set_xlabel(r'$K_t/A_tL_t$', fontsize=16, loc='right')
ax.set_ylabel('Growth rate', fontsize=16, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))

# Format ticks
ax.set_yticks([0])
ax.set_yticklabels(['0'],size=16)
ax.set_xticks([init["KAL_init"],init["KAL_ss"]])
ax.set_xticklabels([r'$\frac{K_0}{A_0L_0}$',r'$\left(\frac{K}{AL}\right)^{ss}$'],size=16)

#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch2-fig2.eps")
plt.savefig(path, bbox_inches='tight')