import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import string
import subprocess as sys
import csv
from scipy import stats

fig=plt.figure()
ax1=fig.add_subplot(111)
wada=open("Wada_timeseries_fill.txt","r")
wadacontent=wada.read()
wada.close()
wadatext=wadacontent.split("\n")
wadatext.pop()
wada=[]
for i in range(len(wadatext)):
	wada.append(float(wadatext[0]))
	wadatext.pop(0)

#####################
seasonly=[]
for fff in range(3):
	month_name=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
	if fff==0:
		file = open("Qaseem_1966_2012.txt", 'r')
		print("Qaseem")
	if fff==1:
		file = open("Riyadh_1966_2012.txt", 'r')
		print("Riyadh")
	if fff==2:
		file = open("Hail_1966_2012.txt", 'r')
		print("Hail")
	content = file.read()
	file.close()
	Vartext=content.split('\n')
	Vartext.pop()
	numFils=len(Vartext)
	Var=[]
	for i in range(numFils):
	#		if float(Vartext[0])>-1:
			if float(Vartext[0])==999:
				Var.append(np.nan)
				Vartext.pop(0)
				continue
			if float(Vartext[0])==-1:
				Var.append(0)
				Vartext.pop(0)
				continue
			Var.append(float(Vartext[0]))
			Vartext.pop(0)
	mmonth=[1,2,3,4]
	monthly=[]
	wadamonthly=[]
	for mm in mmonth:
		month=(Var[mm:len(Var):12])
		month=np.array([float(i) for i in month])
		monthly.append(month)
		wadamonth=(wada[mm:len(wada):12])
		wadamonth=np.array([float(i) for i in wadamonth])
		wadamonthly.append(wadamonth)
	#	ax1.plot(range(1966,2013),month,'.-')
		period1=month[0:12]
		period2=month[14:30]
		#1960-2010
		wadaperiod1=wadamonth[6:18]
		wadaperiod2=wadamonth[20:36]

#print("(Pearson's correlation coefficient,  2-tailed p-value)")
#corr,pvalue=(stats.pearsonr(Var,VarExp-Var))
#print(stats.pearsonr(Var,VarExp-Var))
		period1 = period1[np.logical_not(np.isnan(period1))]
		period2 = period2[np.logical_not(np.isnan(period2))]
#		wadaperiod1 = wadaperiod1[np.logical_not(np.isnan(period1))]
#		wadaperiod2 = wadaperiod2[np.logical_not(np.isnan(period2))]
		print(month_name[mm])
		print(np.nanmean(period1))
		print(np.nanmean(period2))
		print(np.var(period1))
		print(np.var(period2))
		t, p = stats.ttest_ind(period1, period2, equal_var=False)
		print("p= "+str(p))
#		print("Period1: (Pearson's correlation coefficient,  2-tailed p-value)")
#		print(stats.pearsonr(period1,wadaperiod1))
#		print("Period2: (Pearson's correlation coefficient,  2-tailed p-value)")
#		print(stats.pearsonr(period2,wadaperiod2))
		print("-------------")

	print("season mean")
	season=(np.nanmean(monthly,axis=0))
	period1=season[0:12]
	period2=season[14:30]
	period1 = period1[np.logical_not(np.isnan(period1))]
	period2 = period2[np.logical_not(np.isnan(period2))]
	print(np.nanmean(period1))
	print(np.nanmean(period2))
	print(np.var(period1))
	print(np.var(period2))
	t, p = stats.ttest_ind(period1, period2, equal_var=False)
	print("p= "+str(p))
	seasonly.append(season)
fontsize=18
p2start=19
print("stn diff")
stndiff=seasonly[0]-seasonly[1]
print(len(stndiff))
print("len stndiff")
period1=stndiff[0:12]
period2=stndiff[p2start:47]
period1 = period1[np.logical_not(np.isnan(period1))]
period2 = period2[np.logical_not(np.isnan(period2))]
print(np.nanmean(period1))
print(np.nanmean(period2))
print(np.var(period1))
print(np.var(period2))
t, p = stats.ttest_ind(period1, period2, equal_var=False)
print("t test p= "+str(p))
F=(np.var(period1))/(np.var(period2))
p_value = stats.f.cdf(F, len(period1)-1, len(period2)-1)
print("f test p="+str(p_value))
line1=ax1.plot(range(1966,2013),stndiff,'.b-',label="Qaseem-Riyadh")
ax1.plot((1966, 1977), (np.nanmean(period1), np.nanmean(period1)), 'b-',linewidth=2)
ax1.plot((1966+p2start, 2012), (np.nanmean(period2), np.nanmean(period2)), 'b-',linewidth=2)
ax1.text(1995,70,'Difference='+str(round(np.nanmean(period2)-np.nanmean(period1),2)),fontsize=fontsize,color='b')
ax1.text(1995,60,"p="+str(round(p,4)),fontsize=fontsize,color='b')
#################

print("stn diff")
stndiff=seasonly[2]-seasonly[1]
print(len(stndiff))
print("len stndiff")
period1=stndiff[0:12]
period2=stndiff[p2start:47]
period1 = period1[np.logical_not(np.isnan(period1))]
period2 = period2[np.logical_not(np.isnan(period2))]
print(np.nanmean(period1))
print(np.nanmean(period2))
print(np.var(period1))
print(np.var(period2))
t, p = stats.ttest_ind(period1, period2, equal_var=False)
print("t test p= "+str(p))
F=(np.var(period1))/(np.var(period2))
p_value = stats.f.cdf(F, len(period1)-1, len(period2)-1)
print("f test p="+str(p_value))
line2=ax1.plot(range(1966,2013),stndiff,'.g-',label="Hail-Riyadh")
ax1.plot((1966, 1977), (np.nanmean(period1), np.nanmean(period1)), 'g-',linewidth=2)
ax1.plot((1966+p2start, 2012), (np.nanmean(period2), np.nanmean(period2)), 'g-',linewidth=2)
ax1.text(1995,45,'Difference='+str(round(np.nanmean(period2)-np.nanmean(period1),2)),fontsize=fontsize,color='g')
ax1.text(1995,35,"p="+str(round(p,4)),fontsize=fontsize,color='g')
################

#print("stn diff")
#stndiff=seasonly[2]-seasonly[0]
#print(len(stndiff))
#print("len stndiff")
#period1=stndiff[0:12]
#period2=stndiff[p2start:47]
#period1 = period1[np.logical_not(np.isnan(period1))]
#period2 = period2[np.logical_not(np.isnan(period2))]
#print(np.nanmean(period1))
#print(np.nanmean(period2))
#print(np.var(period1))
#print(np.var(period2))
#t, p = stats.ttest_ind(period1, period2, equal_var=False)
#print("t test p= "+str(p))
#F=(np.var(period1))/(np.var(period2))
#p_value = stats.f.cdf(F, len(period1)-1, len(period2)-1)
#print("f test p="+str(p_value))
#line3=ax1.plot(range(1966,2013),stndiff,'.r-',label="Hail-Qaseem")
#ax1.plot((1966, 1977), (np.nanmean(period1), np.nanmean(period1)), 'r-',linewidth=2)
#ax1.plot((1966+p2start, 2012), (np.nanmean(period2), np.nanmean(period2)), 'r-',linewidth=2)
#ax1.text(1995,30,'Difference='+str(round(np.nanmean(period2)-np.nanmean(period1),2)),fontsize=fontsize,color='r')
#ax1.text(1995,20,"p="+str(round(p,4)),fontsize=fontsize,color='r')

ax1.legend(loc='lower right')

#ax2=plt.twinx()
#ax2.plot(range(1966,2013),seasonly[0],'.-')
#ax2.plot(range(1966,2013),seasonly[1],'.-')
######################
#Qaseem=[9224.8,7768.2,29750.9,14091,10342,11953.8,10976.4,np.nan,15755.2,17563.7,45050.2,91205.9,141205.8,204639.6,201533.8,203202.2,251753.5,255284,242427,262586,276121,224158,168922,95121,63895,109064,102120,140370,133086,92624,144287,147007,130533,117957,99712,84621,45654,22792,26426,22951,17160]
#ax2=plt.twinx()
#ax2.plot(range(1972,2013),Qaseem,  'k.-')
#ax2.set_xlim([1970,2014])

#fig.suptitle("("+str(ygrid)+", "+str(xgrid)+") Precipitation")
#fig.suptitle("for 3 stations")
#ax1.grid()
#ax1.set_ylim([0,100])
#ax1.set_xticks(range(0,112,5))
#ax1.set_xticklabels(range(1901,2013,5))
#ax1.set_xlim([70,112])
#ax1.set_xticks(range(0,63,3))
#ax1.set_xticklabels(range(1948,2011,3))
#ax1.set_xlim([25,65])
ax1.set_xlabel("Year",fontsize=fontsize)
ax1.set_ylabel("Rainfall difference(mm/month)",fontsize=fontsize)
ax1.tick_params(labelsize=fontsize)
ax1.set_xticks(range(1966,2013,6))
ax1.set_xlim([1966,2013])
ax1.plot((1965.5, 1965.5), (-60, 80), 'k--',linewidth=3)
ax1.plot((1977.5, 1977.5), (-60, 80), 'k--',linewidth=3)
ax1.plot((1966+p2start-0.5, 1966+p2start-0.5), (-60, 80), 'k--',linewidth=3)


#ax1.legend([month_name[i] for i in mmonth],bbox_to_anchor=(0.9, 1.),loc='upper left',borderaxespad=0.)
figname= (raw_input('figname? '))
#figname="no"
if figname!="no":
	plt.savefig('/home/L.r02229011/fig/'+figname+'.png',bbox_inches=0)
	plt.savefig('/home/L.r02229011/fig/'+figname+'.pdf',bbox_inches=0)
plt.show()

