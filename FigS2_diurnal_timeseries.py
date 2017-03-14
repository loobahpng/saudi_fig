import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import string
import subprocess as sys
from scipy import stats

##########
Var='LH'
diurnal=range(24)
T2=np.array([288.823,290.881,293.214,295.387,297.244,298.654,299.773,300.664,301.342,301.771,301.887,301.612,300.426,298.818,297.473,296.252,295.151,294.123,293.211,292.391,291.654,290.99,290.389,289.866])
T2Exp=np.array([288.365,289.871,291.729,293.443,295.093,296.488,297.645,298.549,299.191,299.543,299.535,298.94,297.092,295.475,294.492,293.623,292.84,292.092,291.416,290.794,290.222,289.697,289.21,288.779])
LH=np.array([6.25917,17.5119,32.2581,47.685,62.2058,73.1844,79.7442,81.2317,77.5038,69.0099,56.513,40.5325,21.7808,12.8846,11.4085,10.5121,9.71581,8.8981,8.14939,7.4644,6.85906,6.33535,5.88891,5.50437])
LHExp=np.array([31.8919,81.4108,149.015,214.024,274.091,315.974,334.991,330.22,303.524,258.355,197.808,122.66,52.462,33.495,30.8515,28.7759,27.0862,25.3903,23.8224,22.2914,20.868,19.6204,18.5035,17.4589])
slp=np.array([1012.85,1013.27,1013.63,1013.86,1013.94,1013.29,1012.71,1012.09,1011.43,1010.8,1010.29,1010.41,1010.59,1010.87,1011.22,1011.58,1011.96,1011.69,1011.6,1011.58,1011.58,1011.6,1011.6,1012.22])
slpExp=np.array([1012.85,1013.28,1013.67,1013.95,1014.11,1013.56,1013.09,1012.57,1011.99,1011.4,1010.89,1010.96,1011.05,1011.25,1011.53,1011.85,1012.18,1011.88,1011.76,1011.71,1011.69,1011.7,1011.68,1012.29])
div=np.array([0.148771,0.114188,0.0568585,0.0188719,0.0467878,-0.0622612,-0.310535,-0.510482,-0.64535,-0.731156,-0.789153,-0.841177,-0.73511,-0.534402,-0.323964,-0.160598,-0.00677005,0.109124,0.15943,0.186638,0.193847,0.222246,0.262714,0.27814])
divExp=np.array([0.146445,0.108942,0.0339512,-0.042988,0.0593532,0.326665,0.535945,0.693215,0.812894,0.879304,0.882759,0.781806,0.606414,0.336409,0.184923,0.14105,0.183961,0.242739,0.244534,0.229718,0.190551,0.192153,0.20745,0.215097])
precip=np.array([0.0130657,0.0131581,0.0125708,0.0128277,0.0132226,0.0151204,0.0177687,0.0217272,0.0270697,0.0334522,0.0389691,0.043682,0.046199,0.0450002,0.0413208,0.0368744,0.0317002,0.0265238,0.0228066,0.0199173,0.0178654,0.0164269,0.0148949,0.0136943])
precipExp=np.array([0.0131796,0.01324,0.0126448,0.0127966,0.0131017,0.0151816,0.018374,0.0233647,0.0299205,0.037138,0.0431803,0.0474185,0.0487572,0.0467701,0.0427154,0.0374816,0.0324356,0.0270406,0.0232753,0.0205179,0.0181883,0.0168643,0.0153739,0.0142646])
#2010: CTR, IRR, IRR-half
#LHExp=np.array([7.68214,20.777,38.8642,56.5708,73.0406,85.0217,91.4888,92.0735,86.7379,76.3135,61.7635,43.2052,22.7698,13.9351,12.431,11.4301,10.5036,9.53749,8.63389,7.84274,7.27321,6.82372,6.34585,5.89265])#IRR-half
#LHExp=np.array([35.82,87.0935,159.62,228.785,290.083,332.761,351.827,345.046,315.404,267.034,203.209,124.275,55.8979,36.4537,33.7774,31.2031,29.0101,26.986,25.2274,23.3188,22.0388,21.1688,20.1022,18.8991])#IRR 95
#LH=np.array([7.42291,19.2238,35.901,52.5591,68.3192,80.1452,86.8761,88.0493,83.6039,74.2272,60.7876,43.3118,23.6389,14.6126,12.8448,11.759,10.8017,9.84999,8.99227,8.24889,7.67176,7.25009,6.7932,6.34306])#CTR
#LHExp=np.array([21.764,54.145,99.263,142.814,182.649,210.987,224.754,223.086,207.262,179.513,142.119,93.3374,46.3276,28.8401,26.4206,24.4288,22.6543,20.7439,19.1599,17.665,16.5551,15.7508,14.7774,13.8603])#IRR 75



#####################
xlabel=''
ylabel=''
#xlabel='Rainy days'
#ylabel='IRR-CTR (mm)'
#ylabel='CTR total rain on rainy days'
#xlabel='number of days with rain more than 0.56mm'
#xlabel='Averaged rain on rainy days (mm)'

#print("-------------")
#print("(Pearson's correlation coefficient,  2-tailed p-value)")
#corr,pvalue=(stats.pearsonr(Var,VarExp))
#print(stats.pearsonr(Var,VarExp))
#print("-------------")
#figtitle='r= '+str(corr)+', p-value= '+str(pvalue)

fig=plt.figure()
ax1=fig.add_subplot(111)
#ax1.plot(yearly,r_intensity, '-go')
ax1.plot(diurnal,eval(Var), '-b')
ax1.plot(diurnal,eval(Var+'Exp'), '-g')

ax2=plt.twinx()
ax2.plot(diurnal,eval(Var+'Exp')-eval(Var),'-r')
ax2.plot(diurnal,eval(Var)*0.,'--r')

ax1.set_xticks(range(0,25,3))
timelabel=[6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,1,2,3,4,5,6]
ax1.set_xticklabels(timelabel[::3])

print("Daily average:")
print(np.average(eval(Var)))
print(np.average(eval(Var+'Exp')))
print(np.average(eval(Var+'Exp'))-np.average(eval(Var)))

print("12AM to 6PM average:")
VV=eval(Var)
VVExp=eval(Var+'Exp')
print(np.average(VV[6:13]))
print(np.average(VVExp[6:13]))
print(np.average(VVExp[6:13])-np.average(VV[6:13]))

print("6AM to 6PM average:")
VV=eval(Var)
VVExp=eval(Var+'Exp')
print(np.average(VV[0:13]))
print(np.average(VVExp[0:13]))
print(np.average(VVExp[0:13])-np.average(VV[0:13]))
#fig.suptitle("("+str(ygrid)+", "+str(xgrid)+") Precipitation")
ax1.grid()
#ax1.set_xlabel(xlabel)
#ax1.set_ylabel(ylabel)
fig.suptitle(Var)
fontsize=18
ax1.legend(["CTR","IRR"],loc='upper left',fontsize=fontsize)
ax2.legend(["IRR-CTR"],loc='upper right',fontsize=fontsize)


ax1.tick_params(labelsize=fontsize)
ax2.tick_params(labelsize=fontsize)

#for i, txt in enumerate(yearly):
#    ax1.annotate(txt, (yearly[i],r_square[i]))

figname= (raw_input('figname? '))
if figname!="no":
	plt.savefig('/home/L.r02229011/wrf_fig/'+figname+'.png',bbox_inches=0)
	plt.savefig('/home/L.r02229011/wrf_fig/'+figname+'.pdf',bbox_inches=0)
plt.show()
