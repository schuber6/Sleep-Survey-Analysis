# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 21:51:34 2018

@author: Scott
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 20:31:07 2018

@author: Scott
"""

import matplotlib.pyplot as plt
import numpy as np


WeightDict=np.load('Data/WeightDict.npy').item()
SleepCounts=np.load('Data/SleepCounts.npy')
times=np.load('Data/times.npy')

Reordered=np.concatenate((np.arange(8,49),np.arange(0,8)))


NSample0=sum(WeightDict.values())
NSleepCounts0=[x/NSample0*100 for x in SleepCounts]
NSC=np.zeros(len(NSleepCounts0))

WeightDict=np.load('Data/WeightDict.npy').item()
SleepCounts_DOW=np.load('Data/SleepCounts_DOW.npy')
times=np.load('Data/times.npy')
WSum_DOW=np.load('Data/WSum_DOW.npy')
Ages=np.load('Data/Ages.npy')

L=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
XL=['2AM','6AM','10AM','2PM','6PM','10PM']
XT=np.arange(2,26,4)
Fifs=np.zeros(2)
for ind,i in enumerate([4,7]):

    NSample=WSum_DOW[ind]
    NSleepCounts=[x/NSample*100 for x in SleepCounts_DOW[i-1,:]]
    for indri,ri in enumerate(Reordered):
        NSC[indri]=NSleepCounts[ri]
    ax=plt.subplot(1,2,1)
    ax.set_xticklabels(XL)
    #plt.subplots_adjust(wspace=0)
    #plt.subplots_adjust(hspace=.4)
    plt.plot(times,NSleepCounts)
    
    NP=np.array(NSleepCounts)
    xq=np.arange(0,24,.01)
    Idata=np.interp(xq,times,NP)
    inds=Idata<=50
    Tinds=xq[inds]
    Fifs[ind]=Tinds[0]
    
    #plt.plot(times,NSleepCounts0,'k--')#,alpha=.2)
    plt.xticks(XT)
    plt.yticks([0,20,40,60,80,100])
    #plt.plot(NSC)
    if ind==0:
        plt.xlabel('Hour of the Day',fontsize=16)
        plt.ylabel('People Asleep (%)',fontsize=16)
        
        plt.tick_params(axis='both', which='major', labelsize=16)
    else:
        if ind==4:
            plt.ylabel('People Asleep (%)',fontsize=16)
            plt.tick_params(axis='y', which='major', labelsize=16)

            
    #plt.title(L[i-1],fontsize=20)
    plt.ylim([0,100])
    plt.xlim([0,24])
    plt.legend(['Wednesday','Saturday'])
        
        #plt.show()
plt.plot(Fifs,[50,50])    


#plt.savefig("SleepVsTime_Ages.png")


for a in Ages:
    L.append(str(a))
#plt.legend(L,title='Age Group')
    
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

SleepData1=pd.read_pickle('Data/SD1.pkl')
SleepData2=pd.read_pickle('Data/SD2.pkl')

#Pivot all data into bins by day of week

grouped1 = SleepData1.groupby('DayOfWeek').sum()
grouped1['wtdavg'] = grouped1['WeightXSleep'] / grouped1['Weight']
print(grouped1.head())
grouped2 = SleepData2.groupby('DayOfWeek').sum()
grouped2['wtdavg'] = grouped2['WeightXSleep'] / grouped2['Weight']
print(grouped2.head())

#Combine morning and night sleep
GroupedSplit=[]
Remap=[2,3,4,5,6,7,1]
for i in np.arange(7)+1:
    GroupedSplit.append((grouped1["wtdavg"][Remap[i-1]]+grouped2["wtdavg"][i])/60)
    
#Plot
ax=plt.subplot(1,2,2)
plt.bar([1,2,3,4,5,6,7],GroupedSplit)
plt.xlabel("Night of the Week",fontsize=16)
#ax.yaxis.tick_right()
#ax.yaxis.set_label_position("right")
plt.ylim([8.5,9.5])
plt.tick_params(axis='y', which='major', labelsize=14)

plt.xticks(np.arange(7)+1,('Sun','Mon','Tues','Wed','Thurs','Fri','Sat'))
plt.ylabel('Avg. Sleep/Night (hrs)',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

