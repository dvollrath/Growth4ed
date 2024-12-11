from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['Times New Roman']
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'

import numpy as np
import matplotlib.pyplot as plt
import os

#############################################
## Define functions
#############################################

def Outputpc(kal,A,alpha): # steady state value of K/AL
	return A*kal**alpha

#############################################
## Set up problem
#############################################
# Set range of K/AL values to graph over
kal = np.linspace(0,5,num=100)

Alow = .5
Ahigh = 1
alpha = .3 #this low to make figure look good

#############################################
## Calculate solutions
#############################################
ylow = Outputpc(kal,Alow,alpha) # growth rate of productivity and labor force
yhigh = Outputpc(kal,Ahigh,alpha)

#############################################
## Create time figure
#############################################
fig, ax = plt.subplots(figsize=(8,8))

# Main elements
ax.plot(kal, ylow, lw=3, color='black') # plot growth rate of K
ax.plot(kal, yhigh, lw=3, color='gray') # plot growth rate of K

# Add text
ax.annotate(r'$y_t = A\left(\frac{K_t}{A_tL_t}\right)^{\alpha}$', xy=(4,Outputpc(4,Alow,alpha)-.07), xytext=(4,Outputpc(4,Alow,alpha)-.07), size=16)
ax.annotate(r'$A_t^{\prime}>A_t$', xy=(4,Outputpc(4,Alow,alpha)-.07), xytext=(4,Outputpc(4,Alow,alpha)+.25), size=16)
ax.annotate(r'$y_t = A_t^{\prime}\left(\frac{K_t}{A_t^{\prime}L_t}\right)^{\alpha}$', xy=(4,Outputpc(4,Ahigh,alpha)-.07), xytext=(4,Outputpc(4,Ahigh,alpha)-.07), size=16)

# Options
ax.set_xlim(0,5)
ax.set_ylim(0,2)
ax.set_xlabel(r'$\frac{K_t}{A_tL_t}$', fontsize=20, loc='right')
ax.set_ylabel(r'$y$', fontsize=16, loc='top',rotation=0)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

#plt.show()
# Save
location = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(location, "../Figures/fig-ch2-fig1.eps")
plt.savefig(path, bbox_inches='tight')
