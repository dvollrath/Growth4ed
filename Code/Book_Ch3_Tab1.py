import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['Times New Roman']
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'

first = 1960
last = 2019
diff = 10

alpha = .3

# Open file to write table entries
f = open('../Draft/tab_ch3_tab1.txt', 'w')
f.write('\\\\' + '\n' )

# define functions to write output
def Write(ccode,pw):
	countryname = pw.loc[(pw['countrycode']==ccode) & (pw['year']==2019),'country'].values
	f.write('\\multicolumn{7}{c}{' + countryname[0] + '} \\\\' + '\n') # write title of section

	years = [1965,1975,1985,1995,2005,2015]
	wtrans = 'Transitory ($\\alpha (g_K - g_A - g_L)$)'
	wtrend = 'Productivity ($g_A$)'
	wcap = 'Capital ($g_K$)'
	wlabor = 'Labor ($g_L$)'
	wgdppc = 'GDP per capita ($g_y$)'

	for y in years:
		wggdppc = pw.loc[(pw['countrycode']==ccode) & (pw['year']==y),'glnGDPpc'].values
		wgdppc = wgdppc + ' & ' + "{0:.2f}".format(wggdppc[0])
		wglnA = pw.loc[(pw['countrycode']==ccode) & (pw['year']==y),'glnA'].values
		wtrend = wtrend + ' & ' + "{0:.2f}".format(wglnA[0])
		wgtrans = pw.loc[(pw['countrycode']==ccode) & (pw['year']==y),'gtransition'].values
		wtrans = wtrans + ' & ' + "{0:.2f}".format(wgtrans[0])
		wgK = pw.loc[(pw['countrycode']==ccode) & (pw['year']==y),'glnK'].values
		wcap = wcap + ' & ' + "{0:.2f}".format(wgK[0])
		wgL = pw.loc[(pw['countrycode']==ccode) & (pw['year']==y),'glnpop'].values
		wlabor = wlabor + ' & ' + "{0:.2f}".format(wgL[0])

	wgdppc = wgdppc + '\\\\' + '\n'
	wtrend = wtrend + '\\\\' + '\n'
	wtrans = wtrans + '\\\\' + '\n'
	wcap = wcap + '\\\\' + '\n'
	wlabor = wlabor + '\\\\' + '\n'

	f.write(wgdppc) # write title of section
	f.write('\\\\' + '\n' )
	f.write('\\multicolumn{7}{l}{Breakdown of GDP per capita growth:} \\\\' + '\n' )
	f.write(wtrend) # write title of section
	f.write(wtrans) # write title of section
	f.write('\\\\' + '\n' )
	f.write('\\multicolumn{7}{l}{Breakdown of transitory growth:} \\\\' + '\n' )	
	f.write(wcap) # write title of section
	f.write(wtrend) # write title of section
	f.write(wlabor) # write title of section
	f.write('\\\\' + '\n' )

# read PWT dataset into pw
pw = pd.read_csv('../Data/pwt100.csv')

pw['GDPpc'] = pw['rgdpna']/pw['pop'] # create GDP per capita
pw['lnGDPpc'] = np.log(pw['GDPpc'])
pw['lnpop'] = np.log(pw['pop'])
pw['lnK'] = np.log(pw['rnna'])
pw['lnTFP'] = np.log(pw['rtfpna'])/(1-alpha)
pw['alpha'] = alpha
pw['glnGDPpc'] = 100*pw.groupby(['countrycode'])['lnGDPpc'].diff(periods=diff)/diff
pw['glnpop'] = 100*pw.groupby(['countrycode'])['lnpop'].diff(periods=diff)/diff
pw['glnK'] = 100*pw.groupby(['countrycode'])['lnK'].diff(periods=diff)/diff
pw['glnTFP'] = 100*pw.groupby(['countrycode'])['lnTFP'].diff(periods=diff)/diff
pw['glnA'] = pw['glnGDPpc']/(1-pw['alpha']) - (pw['alpha']/(1-pw['alpha']))*(pw['glnK']-pw['glnpop'])
pw['gtransition'] = pw['alpha']*(pw['glnK']-pw['glnA']-pw['glnpop'])

Write('USA',pw)
#Write('DEU',pw)
Write('JPN',pw)
#Write('CHN',pw)


f.close()