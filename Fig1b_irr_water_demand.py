import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import string
import subprocess as sys
import csv
from scipy import stats

fig=plt.figure()
ax1=fig.add_subplot(111)
#############
wada=open("Wada_timeseries_fill.txt","r")
wadacontent=wada.read()
wada.close()
wadatext=wadacontent.split("\n")
wadatext.pop()
wada=[]
for i in range(len(wadatext)):
	if float(wadatext[0])==-9999:
		wada.append(np.nan)
		wadatext.pop(0)
		continue
	wada.append(float(wadatext[0]))
	wadatext.pop(0)
################
wisser=open("Wisser_timeseries_fill.txt","r")
wissercontent=wisser.read()
wisser.close()
wissertext=wissercontent.split("\n")
wissertext.pop()
wisser=[]
for i in range(len(wissertext)):
	if float(wissertext[0])==-9999:
		wisser.append(np.nan)
		wissertext.pop(0)
		continue
	wisser.append(float(wissertext[0]))
	wissertext.pop(0)
##################

wadamonthly=[]
wissermonthly=[]
mmonth=[1,2,3,4]
for mm in mmonth:
	wadamonth=(wada[mm:len(wada):12])
	wadamonth=np.array([float(i) for i in wadamonth])
	wadamonthly.append(wadamonth)
	wissermonth=(wisser[mm:len(wisser):12])
	wissermonth=np.array([float(i) for i in wissermonth])
	wissermonthly.append(wissermonth)
wadaseason=(np.nanmean(wadamonthly,axis=0))
wisserseason=(np.nanmean(wissermonthly,axis=0))
ax1.plot(range(1960,2011),wadaseason,'-')
ax2=plt.twinx()
ax2.plot(range(1899,2001),wisserseason,'g-')
fontsize=18
fig.suptitle("Irrigation water demand by Year",fontsize=fontsize)
ax1.set_xlabel("Year",fontsize=fontsize)
ax1.set_ylabel("mm/month",fontsize=fontsize)
ax1.tick_params(labelsize=fontsize)
ax2.tick_params(labelsize=fontsize)
ax1.set_xticks(range(1966,1996,4))
ax1.set_xlim([1966,1996])
ax2.set_ylim([0,10])
ax1.plot((1965.5, 1965.5), (0, 40), 'k--',linewidth=3)
ax1.plot((1977.5, 1977.5), (0, 40), 'k--',linewidth=3)
ax1.plot((1984.5, 1984.5), (0, 40), 'k--',linewidth=3)

ax1.legend(["Wada"],loc='upper left',fontsize=fontsize)
ax2.legend(["Wisser"],loc='upper right',fontsize=fontsize)


figname= (raw_input('figname? '))
#figname="rainy_day_precipAno"
if figname!="no":
	plt.savefig('/home/L.r02229011/fig/'+figname+'.png',bbox_inches=0)
	plt.savefig('/home/L.r02229011/fig/'+figname+'.pdf',bbox_inches=0)
plt.show()
