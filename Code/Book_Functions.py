#############################################
## Import packages used by functions here
#############################################
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

#############################################
## Define functions
#############################################
def figures():
	from matplotlib import rcParams
	rcParams['font.family'] = 'serif'
	rcParams['font.sans-serif'] = ['Times New Roman']
	rcParams['mathtext.fontset'] = 'stix'
	rcParams['font.family'] = 'STIXGeneral'
	rcParams['axes.prop_cycle'] = plt.cycler(color=["black", "black", "black"],linestyle=['-', '--', '-.'])

# Solve Solow model exactly for passed parameters
# - Pass parameters/initial values in order (e.g. s = solow(.33,.2,.04,.01,.03,10,4,3,1))
# - OR pass specific parameter and use others in default (e.g. s = solow(ga = .04))
#
# - Can pass arrays of values to function and receive solution at each value
# - Example 1:
# - periods = np.arange(1,100,1) # generates array of 1 to 100
# - s = solow(t = periods) # will return values of KAL, gK, etc.. for all 100 periods
#
# - Example 2: 
# - K = np.arange(1,5,.1) # generates starting valeus of K from 1 to 5, in steps of .1
# - s = solow(k0 = K) # will return values of KAL, gK, etc.. for all initial K values
def solow(alpha = .3, si=.2, delta=.05, ga=.02, gl=.01, k0=1, a0=1, l0=1, t=1):
	kal_init = k0/(a0*l0) # initial K/AL ratio
	ky_init = kal_init**(1-alpha) # initial K/Y ratio
	ky_ss = si/(delta+ga+gl) # K/Y steady state
	kal_ss = ky_ss**(1/(1-alpha)) # K/AL steady state
	gK_init = si/ky_init - delta # initial gK
	gy_init = (1-alpha)*(gK_init - ga - gl) + ga # initial gy
	
	# Manage the time periods passed
	try:
		u = t - min(t) # resets any list of time periods to have base zero for convergence calc
	except:
		u = t # if above fails, what was passed is taken as-is (usually just a single integer)

	conv_term = (1-alpha)*(delta+ga+gl) # convergence term for exact solution
	ky_time = ky_ss*(1-np.exp(-1*conv_term*u)) + ky_init*np.exp(-1*conv_term*u) # K/Y at each t
	kal_time = ky_time**(1/(1-alpha)) # K/AL at each t
	lny_time = (alpha/(1-alpha))*np.log(ky_time) + np.log(a0) + ga*t # Log GDP pc at each t
	lny_bgp = (alpha/(1-alpha))*np.log(ky_ss) + np.log(a0) + ga*t # BGP of GDP pc at each t
	gK_time = si/ky_time - delta # growth rate of K at each t
	gy_time = (1-alpha)*(gK_time - ga - gl) + ga # growth rate of GDP pc at each t 
	
	# return all values as a dictionary to calling program
	solved = {'time': t, 'KAL': kal_time, 'KY': ky_time, 'lny': lny_time, 
		'lny_bgp': lny_bgp, 'gK': gK_time, 'gy': gy_time, 'KY_ss': ky_ss,
		'KAL_ss': kal_ss, 'KY_init': ky_init, 'KAL_init': kal_init, 'gK_init': gK_init,
		'gy_init': gy_init, 'gy_ss': ga}
	return solved

# Solve Romer model exactly for passed parameters
# - Pass parameters/initial values in order (e.g. r = romer(.8,-.2,.1,.01,.02,10,4,1))
# - OR pass specific parameter and use others in default (e.g. r = romer(phi = .8))
#
# - Can pass arrays of values to function and receive solution at each value
# - Example 1:
# - periods = np.arange(1,100,1) # generates array of 1 to 100
# - r = romer(t = periods) # will return values of lnA, gA, etc.. for all 100 periods
#
# - Example 2: 
# - A = np.arange(1,5,.1) # generates starting valeus of A from 1 to 5, in steps of .1
# - r = romer(A0 = A) # will return values of gA, etc.. for all initial A values
def romer(phi=0,lamb=1,theta=1, sR=.05, gL=.01, A0=1, L0=1,t=1):
	AL_init = A0**(1-phi)/L0**lamb # initial A/L ratio (with exponents)
	AL_ss = (1-phi)*theta*(sR**lamb)/(lamb*gL) # s.s. A/L ratio
	LA_ss = 1/AL_ss # inverted for use by calling program
	gA_init = theta*(L0**lamb)*(sR**lamb)/(A0**(1-phi)) # initial growth rate of A
	gA_ss = (lamb/(1-phi))*gL # steady state growth rate of A

	# Manage the time periods passed
	try:
		u = t - min(t) # resets any list of time periods to have base zero for convergence calc
	except:
		u = t # if above fails, what was passed is taken as-is (usually just a single integer)

	conv_term = lamb*gL # convergence term for exact solution
	AL_time = AL_ss*(1-np.exp(-1*conv_term*u)) + AL_init*np.exp(-1*conv_term*u) # A/L at each t
	gA_time = theta*(sR**lamb)/AL_time # gA at each t
	lnA_time = (lamb/(1-phi))*np.log(L0) + (1/(1-phi))*np.log(AL_time) + (lamb/(1-phi))*gL*t # log A at each t
	lnA_bgp = (lamb/(1-phi))*np.log(L0) + (1/(1-phi))*np.log(AL_ss) + (lamb/(1-phi))*gL*t # log A along a BGP
	LA_time = 1/AL_time # inverted for use by calling program

	# return all values as a dictionary to calling program
	solved = {'time': t, 'AL': AL_time, 'lnA': lnA_time, 'gA': gA_time, 
		'lnA_bgp': lnA_bgp, 'AL_ss': AL_ss, 'gA_ss': gA_ss, 'gA_init': gA_init,
		'AL_init': AL_init, 'LA': LA_time, 'LA_ss': LA_ss}
	return solved

# Function to read in Penn World Tables, calculate some common values, and return to calling program
def pwt():
	# read PWT dataset into pw
	pw = pd.read_csv('../Data/pwt100.csv') # read PWT 10 data
	ed = pd.read_csv('../Data/pwt100-labor-detail.csv') # read education data supplement from PWT
	ed = ed[['countrycode','year','yr_sch']] # subset educ data
	pw = pd.merge(pw,ed,on = ['countrycode','year'],how='inner') # merge educ data
	na = pd.read_csv('../Data/pwt100-na-data.csv') # read national accounts data
	na = na[['countrycode','year','v_x','v_m','v_gdp','q_m','q_gdp']] # subset trade data
	pw = pd.merge(pw,na,on = ['countrycode','year'],how='inner') # merge to main pw

	# Clean up some country names for use in figures
	pw.loc[(pw.countrycode == 'KOR'), 'country'] = 'South Korea'
	pw.loc[(pw.countrycode == 'VEN'), 'country'] = 'Venezuela'

	# Basic calculations
	pw['GDPpc'] = pw['rgdpo']/pw['pop'] # create GDP per capita
	pw['GDPpw'] = pw['rgdpo']/pw['emp'] # create GDP per worker
	
	pw['lnGDPpc'] = np.log(pw['GDPpc']) # log GDP per capita
	pw['lnGDPpw'] = np.log(pw['GDPpw']) # log GDP per worker
	pw['trade'] = (pw['v_m']+pw['v_x'])/pw['v_gdp'] # total trade ratio

	# Basic development accounting
	pw['lfp'] = pw['emp']/pw['pop'] # labor force participation
	pw['ky'] = (pw['cn']/pw['cgdpo'])**(.3/.7) # capital/output to alpha/1-alpha
	pw['hc'] = np.exp(.1*pw['yr_sch']) # Mincerian return of 10%
	pw['A'] = pw['GDPpc']/(pw['ky']*pw['hc']*pw['lfp']) # residual productivity

	# Create relative GDP pc to US in each year
	us = pw[pw['countrycode'].isin(['USA'])].copy() # get US data
	us['usGDPpc'] = us['GDPpc'] # copy US GDPpc to new column
	us['usA'] = us['A'] # copy US TFP level to new column
	us['usky'] = us['ky'] # copy US K/Y ratio
	us['ushc'] = us['hc'] # coyp US HC
	us['uslfp'] = us['lfp'] # copy US labor force participation 

	us = us[['year','usGDPpc','usA', 'usky', 'ushc', 'uslfp']] # subset to just year and US GDP pc
	pw = pd.merge(pw,us,on='year',how='left') # merge US GDP pc data to overall PWT
	pw['relGDPpc'] = 100*pw['GDPpc']/pw['usGDPpc'] # relative size (scaled to US = 100)
	pw['relA'] = 100*pw['A']/pw['usA'] # relative size (scaled to US = 100)
	pw['relky'] = 100*pw['ky']/pw['usky'] # relative size (scaled to US = 100)
	pw['relhc'] = 100*pw['hc']/pw['ushc'] # relative size (scaled to US = 100)
	pw['rellfp'] = 100*pw['lfp']/pw['uslfp'] # relative size (scaled to US = 100)

	pw.sort_values(by=['countrycode', 'year']) # organize by country/year
	return pw

# Function to load world governance indicators and merge with PWT
def govern():
	pw = pwt() # load PWT first

	wg = pd.read_csv('../Data/wgiraw.csv') # read World Governance indicators
	wg.rename(columns = {'code': 'countrycode'}, inplace=True) # rename to match PWT
	wg = wg[['countrycode','year','vae','pve','gee','rqe','rle','cce']] # subset only specific values
	pw = pd.merge(pw,wg,on = ['countrycode','year'],how='inner') # merge with PWT

	# Average governance indicator
	pw['gov'] = (pw['vae']+pw['pve']+pw['gee']+pw['rqe']+pw['rle']+pw['cce'])/6

	return pw

# Function to load US EIA energy indicators
def energy():
	ei = pd.read_csv('../Data/eia_table1_5.csv') # base energy data
	rn = pd.read_csv('../Data/eia_table10_1.csv') # renewables data
	ei = pd.merge(ei,rn,on = ['year'],how='left')

	ei['nom_energy'] = pd.to_numeric(ei['nom_energy'],errors='coerce')
	ei['nom_energy_gdp'] = pd.to_numeric(ei['nom_energy_gdp'],errors='coerce') # make numeric
	ei['energy_gdp'] = pd.to_numeric(ei['energy_gdp'],errors='coerce') # make numeric
	
	ei['energy_price'] = ei['nom_energy_gdp']/ei['energy_gdp'] # implied price
	base = ei.loc[(ei['year']==1970),'energy_price'].values # base price in 1970
	ei['energy_price'] = 100*ei['energy_price']/base # rebase price to 1970
	
	ei['energy'] = pd.to_numeric(ei['energy'],errors='coerce') # make numeric
	ei['energy_pop'] = pd.to_numeric(ei['energy_pop'],errors='coerce') # make numeric
	ei['co2'] = pd.to_numeric(ei['co2'],errors='coerce') # make numeric

	# Calculate renewable percent
	ei['renew_prod'] = pd.to_numeric(ei['renew_prod'],errors='coerce')
	ei['wood'] = pd.to_numeric(ei['wood'],errors='coerce')
	ei['renew_perc'] = 100*(ei['renew_prod']-ei['wood'])/(ei['energy']*1000)

	return ei

# Function to load UN fertility data
def fert():
	un = pd.read_csv('../Data/total-fertility-rate-including-un-projections-through-2100.csv')

	un = un[(un['Year']<2051)] # limit time span
	un = un.set_index(['Entity']) # set index to country
	un['tfr_proj'] = un['tfr_proj'].fillna(0) # put 0 in for NA
	un['tfr'] = un['tfr'].fillna(0) # put 0 in for NA
	un.loc[(un.Year==2020),'tfr_proj'] = 0 # add a 0 for projected TFR in 2020
	un['tfr_plot'] = un['tfr']+un['tfr_proj'] # add the two series to get single series to plot

	return un

# Function to load Maddison country data
def maddison():
	mad = pd.read_csv('../Data/mpd2020raw.csv')
	mad.sort_values(by=['countrycode', 'year']) # organize by country/year
	mad['lnGDPpc'] = np.log(mad['gdppc'])

	return mad

# Function to load Maddison world data
def world():
	md = pd.read_csv('../Data/mpdworldraw.csv')
	md['pop'] = md['pop']/1000000 # scaling
	md['gpop'] = md['gpop']*100 # in percent
	md['ggdppc'] = md['ggdppc']*100 # in percent

	return md

# Function to load OECD R&D stats
def oecd():
	df = pd.read_csv('../Data/oecd_pers_func.csv')
	countries = ['USA','JPN','CHN','DEU','GBR']

	# subset of OECD data based on measure (all sectors, R&D workers, all gender, full time equivalent)
	df = df[(df['SECTPERF']=='_T') & (df['FUNCTION']=='RSE') & (df['GENDER']=='_T')
    	& (df['MEASURE']=='FTE') & (df['COUNTRY'].isin(countries))]
	df['obsValue'] = df['obsValue']/1000 # scaling
	
	pw = pwt() # load PWT
	pw = pw[pw['countrycode'].isin(countries)]
	pw = pw[['countrycode','emp','year']] # subset just the employment
	pw.rename(columns = {'countrycode':'COUNTRY', 'emp':'employment', # rename for merging
                              'year':'obsTime'}, inplace = True)

	df = pd.merge(df,pw,on = ['COUNTRY','obsTime'],how='inner')
	df['RDpercent'] = 100000*df['obsValue']/(df['employment']*1000000) # calculate R&D percent
	#df.sort_values(by=['obsTime'],inplace=True) # sort by year

	# clean up names for figures
	df.loc[(df.COUNTRY == 'CHN'), 'COUNTRY'] = 'China'
	df.loc[(df.COUNTRY == 'USA'), 'COUNTRY'] = 'United States'
	df.loc[(df.COUNTRY == 'JPN'), 'COUNTRY'] = 'Japan'
	df.loc[(df.COUNTRY == 'DEU'), 'COUNTRY'] = 'Germany'
	df.loc[(df.COUNTRY == 'GBR'), 'COUNTRY'] = 'United Kingdom'

	return df

def trifigure(pre,post,Tstar,Tmax,title):
	fig, (ax1, ax2, ax3) = plt.subplots(3,sharex=True,figsize=(8,8))

	# Main elements
	ax1.plot(pre["time"],pre["lny_bgp"], lw=3, color='gray',linestyle='--') # old BGP
	ax1.plot(post["time"],post["lny_bgp"], lw=3, color='gray',linestyle='--') # new BGP
	ax1.plot(pre["time"][1:Tstar],pre["lny_bgp"][1:Tstar], lw=3,color='black',linestyle='-') # actual GDP pc before change
	ax1.plot(post["time"],post["lny"], lw=3,color='black',linestyle='-') # actual GDP pc after change

	ax2.plot([0,Tmax],[pre["gy_ss"],pre["gy_ss"]], lw=3, color='gray', linestyle='--') # ss growth rate prior
	ax2.plot([Tstar,Tmax],[post["gy_ss"],post["gy_ss"]], lw=3, color='gray', linestyle='--') # ss growth rate after
	ax2.plot([0,Tstar],[pre["gy_ss"],pre["gy_ss"]], lw=3, color='black') # old growth rate prior to change
	ax2.plot(post["time"], post["gy"], lw=3, color='black',linestyle='-') # growth rate after change

	ax3.plot([0,Tmax],[pre["KAL_ss"],pre["KAL_ss"]], lw=3, color='gray', linestyle='--') # KAL ss prior
	ax3.plot([Tstar,Tmax],[post["KAL_ss"],post["KAL_ss"]], lw=3, color='gray', linestyle='--') # KAL ss after change
	ax3.plot([0,Tstar-1],[pre["KAL_ss"],pre["KAL_ss"]], lw=3, color='black',linestyle='-') # KAL prior
	ax3.plot(post["time"], post["KAL"], lw=3, color='black',linestyle='-') # KAL post

	ax1.set_ylabel(r'Log $y$', fontsize=10, rotation=0, loc='top')
	ax2.set_ylabel(r'$g_y$', fontsize=10, rotation=0, loc='top')
	ax3.set_ylabel(r'$K/AL$', fontsize=10, rotation=0, loc='top')

	ax1.set_title(title, fontsize=16)

	#ax3.set_ylim(min(post["KAL"])*.9,max(post["KAL"])*1.1)
	ax3.set_yticks([pre["KAL_ss"],post["KAL_ss"]])
	ax3.set_xticks([Tstar])
	ax3.set_xticklabels([r'$T^{\ast}$'],size=14)

def prodfigure(pre,post,ypre,ypost,Tstar,Tmax,title):
	tall = np.arange(0,Tmax,1) 
	tpost = np.arange(Tstar,Tmax,1)

	fig, (ax1, ax2, ax3) = plt.subplots(3,sharex=True,figsize=(8,8))

	# Main elements
	ax1.plot([0,Tmax],[pre["gA_ss"],pre["gA_ss"]], lw=3, color='gray', linestyle='--') # ss growth rate prior
	ax1.plot([Tstar,Tmax],[post["gA_ss"],post["gA_ss"]], lw=3, color='gray', linestyle='--') # ss growth rate after
	ax1.plot([0,Tstar],[pre["gA_ss"],pre["gA_ss"]], lw=3, color='black') # old growth rate prior to change
	ax1.plot(post["time"], post["gA"], lw=3, color='black',linestyle='-') # growth rate after change

	ax2.plot(pre["time"],pre["lnA_bgp"], lw=3, color='gray',linestyle='--') # old BGP
	ax2.plot(post["time"],post["lnA_bgp"], lw=3, color='gray',linestyle='--') # new BGP
	ax2.plot(pre["time"][1:Tstar],pre["lnA_bgp"][1:Tstar], lw=3,color='black',linestyle='-') # actual GDP pc before change
	ax2.plot(post["time"],post["lnA"], lw=3,color='black',linestyle='-') # actual GDP pc after change

	ax3.plot(tall,ypre["lny_bgp"], lw=3, color='gray',linestyle='--') # old BGP
	ax3.plot(tpost,ypost["lny_bgp"], lw=3, color='black',linestyle='-') # new BGP
	ax3.plot(tall[1:Tstar],ypre["lny_bgp"][1:Tstar], lw=3,color='black',linestyle='-') # actual GDP pc before change

	ax1.set_ylabel(r'$g_A$', fontsize=10, rotation=0, loc='top')
	ax2.set_ylabel(r'Log $A$', fontsize=10, rotation=0, loc='top')
	ax3.set_ylabel(r'Log $y$', fontsize=10, rotation=0, loc='top')

	ax1.set_title(title, fontsize=16)

	ax3.set_xticks([Tstar])
	ax3.set_xticklabels([r'$T^{\ast}$'],size=14)


