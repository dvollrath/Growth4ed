import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import Book_Functions as f # import my baseline functions
f.figures() # get style modifiers for figures

#############################################
## Set up time periods
#############################################
Tstar=30 # time period when shock occurs
Tmax=150 # time periods to graph

tpre  = np.arange(0,Tstar,1) # time periods before shock
tpost = np.arange(Tstar,Tmax,1) # time periods after shock

#############################################
## Set up baseline parameters
#############################################
sI = .2 # gross capital formation rate
gA = .04 # growth rate of productivity
gL = .01 # growth rate of population
delta = .05 # depreciation rate
alpha = .4 # elasticity of GDP wrt capital
A0 = 1 # initial productivity level
L0 = 1 # initial population level
phi = .1
h = 1
gamma = 1
ADss = (gA/(phi*h))**(1/gamma)
D0 = A0/ADss

KALss = (sI/(gA+gL+delta))**(1/(1-alpha)) # steady state value of K/AL given parameters
K0 = D0*L0*KALss # initial capital starts at steady state


#############################################
## Set up lists to hold values over time
#############################################
Kt = [K0] # capital, starting with K0
At = [A0] # productivity, starting with A0
Dt = [D0]
Lt = [L0] # labor, starting with L0
KALt = [K0/(D0*h*L0)] # KAL ratio
KALsst = [KALss] # steady state KAL ratio
ADt = [A0/D0]
ADsst = [ADss]
yt = [(K0/(D0*h*L0))**alpha*h*D0] # GDP per capita
ysst = [KALss**alpha*h*(1/ADss)*A0] # BGP GDP per capita
gyt = [gA] # growth rate of GDP per capita starts at s.s.
gKt = [gA+gL] # growth rate of capital starts at s.s. 

#############################################
## Loop through periods *before* shock
#############################################
for t in tpre:
	KAL = Kt[t]/(Dt[t]*h*Lt[t]) # find actual K/AL ratio
	AD = At[t]/Dt[t]
	gKcalc = sI*(1/KAL)**(1-alpha) - delta # find growth rate of capital
	gDcalc = phi*h*(AD)**gamma
	KALt.append(KAL) # save K/AL ratio
	ADt.append(AD)
	ADsst.append(ADss) # save steady state K/AL ratio
	gKt.append(gKcalc) # save growth rate of capital
	yt.append(KAL**alpha*h*Dt[t]) # save GDP per capita
	ysst.append(KALss**alpha*h*(1/ADss)*At[t]) # save BGP GDP per capita
	gyt.append(alpha*(gKcalc - gDcalc - gL) + gDcalc) # save growth rate of GDP per capita
	Kt.append(Kt[t]*(1+gKcalc)) # save capital stock
	Lt.append(Lt[t]*(1+gL)) # save pop
	At.append(At[t]*(1+gA)) # save productivity
	Dt.append(Dt[t]*(1+gDcalc))

gA = .01
ADss = (gA/(phi*h))**(1/gamma)

for t in tpost:
	KAL = Kt[t]/(Dt[t]*h*Lt[t]) # find actual K/AL ratio
	AD = At[t]/Dt[t]
	gKcalc = sI*(1/KAL)**(1-alpha) - delta # find growth rate of capital
	gDcalc = phi*h*(AD)**gamma
	KALt.append(KAL) # save K/AL ratio
	ADt.append(AD)
	ADsst.append(ADss) # save steady state K/AL ratio
	gKt.append(gKcalc) # save growth rate of capital
	yt.append(KAL**alpha*h*Dt[t]) # save GDP per capita
	ysst.append(KALss**alpha*h*(1/ADss)*At[t]) # save BGP GDP per capita
	gyt.append(alpha*(gKcalc - gDcalc - gL) + gDcalc) # save growth rate of GDP per capita
	Kt.append(Kt[t]*(1+gKcalc)) # save capital stock
	Lt.append(Lt[t]*(1+gL)) # save pop
	At.append(At[t]*(1+gA)) # save productivity
	Dt.append(Dt[t]*(1+gDcalc))

#############################################
## Create figures
#############################################

location = os.path.abspath(os.path.dirname(__file__))

# A: drop in cap investment rate

fig, (ax1, ax2, ax3) = plt.subplots(3,sharex=True,figsize=(8,8))

ax1.plot(tpre,gyt[0:Tstar], lw=3, color='black',linestyle='-') # old BGP
ax1.plot(tpost,gyt[Tstar:Tmax], lw=3, color='black',linestyle='-') # old BGP

ax2.plot(tpost,np.log(ysst[Tstar:Tmax]), lw=3, color='gray',linestyle='--') # old BGP
ax2.plot(tpre,np.log(yt[0:Tstar]), lw=3, color='black',linestyle='-') # old BGP
ax2.plot(tpost,np.log(yt[Tstar:Tmax]), lw=3, color='black',linestyle='-') # old BGP

ax3.plot(tpost,ADsst[Tstar:Tmax], lw=3, color='gray',linestyle='--') # old BGP
ax3.plot(tpre,ADt[0:Tstar], lw=3, color='black',linestyle='-') # old BGP
ax3.plot(tpost,ADt[Tstar:Tmax], lw=3, color='black',linestyle='-') # old BGP

ax1.set_ylabel(r'$g_y$', fontsize=10, rotation=0, loc='top')
ax2.set_ylabel(r'Log $y$', fontsize=10, rotation=0, loc='top')
ax3.set_ylabel(r'$A/D$', fontsize=10, rotation=0, loc='top')

ax1.set_title("Exercise 7.4b", fontsize=16)

ax3.set_xticks([Tstar])
ax3.set_xticklabels([r'$T^{\ast}$'],size=14)

path = os.path.join(location, "../Figures/fig-ch7-exer4b.eps")
plt.savefig(path, bbox_inches='tight')


#plt.show()
