from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['Times New Roman']
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'

import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as pr # pull in common productivity functions

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

#############################################
## Calculate solutions
#############################################
r = pr.romer(phi,lam,theta,sRold,gL,A0,L0,1) # call to find s.s. ratio of L/A
L = np.arange(.01*r["LA_ss"],1.5*r["LA_ss"],.01) # range of L to create variation in A/L ratio

old = pr.romer(phi,lam,theta,sRold,gL,A0,L,1) # call for all the values of L at old sR
new = pr.romer(phi,lam,theta,sRnew,gL,A0,L,1) # call for all the values of L at new sR
init = pr.romer(phi,lam,theta,sRnew,gL,old["AL_ss"],L0,1) # call to find gA at old s.s with new sR

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot(old["LA"], old["gA"], lw=3, color='black') # plot old growth rate of A
ax.plot(new["LA"], new["gA"], lw=3, color='gray') # plot new growth rate of A
ax.plot([min(L),max(L)],[old["gA_ss"],old["gA_ss"]],lw=3,color='black',linestyle='--')
ax.plot([old["LA_ss"],old["LA_ss"]],[0,init["gA_init"]],lw=2,color='gray',linestyle='dotted')
ax.plot([new["LA_ss"],new["LA_ss"]],[0,new["gA_ss"]],lw=2,color='gray',linestyle='dotted')

# Annotate
ax.plot(old["LA_ss"],init["gA_init"],'o',markersize=10,color='gray')
ax.plot(old["LA_ss"],old["gA_ss"],'o',markersize=10,color='black')
ax.plot(new["LA_ss"],new["gA_ss"],'o',markersize=10,color='gray')

ax.annotate(r'$\lambda g_L$', xy=(.9*max(L),old["gA_ss"]-.003), size=16)
ax.annotate(r'$(1-\phi)g_A$', xy=(.65*max(L),max(new["gA"])-.01), size=16)

ax.arrow(.9*max(L),old["gA_ss"]+.01,0,.02,color='gray',head_width = 0.03,head_length=0.001)

# Options
ax.set_xlim(min(L),max(L))
ax.set_ylim(min(old["gA"]),max(new["gA"]))
ax.set_xlabel(r'$L_t^{\lambda}/A_t^{1-\phi}$', fontsize=14, loc='right', labelpad = -20)
ax.set_ylabel('Growth rate', fontsize=14, loc='top')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Format ticks
ax.set_yticks([])
ax.set_xticks([new["LA_ss"],old["LA_ss"]])
ax.set_xticklabels([r'$\left(\frac{L^{\lambda}}{A^{1-\phi}}\right)^{ss}_{new}$',r'$\left(\frac{L^{\lambda}}{A^{1-\phi}}\right)^{ss}_{old}$'],size=14)

#plt.show()

# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch5-fig2.eps")
plt.savefig(path, bbox_inches='tight')
