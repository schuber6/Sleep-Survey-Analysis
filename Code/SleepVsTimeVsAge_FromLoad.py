# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 19:48:54 2018

@author: Scott
"""

import matplotlib.pyplot as plt
import numpy as np


WeightDict=np.load('Data/WeightDict.npy').item()
SleepCounts=np.load('Data/SleepCounts.npy')
times=np.load('Data/times.npy')

NSample0=sum(WeightDict.values())
NSleepCounts0=[x/NSample0*100 for x in SleepCounts]

WeightDict=np.load('Data/WeightDict.npy').item()
SleepCounts=np.load('Data/SleepCounts_Ages.npy')
times=np.load('Data/times.npy')
Ages=np.load('Data/Ages.npy')
WSum=np.load('Data/WSum.npy')

L=['15-25','26-40','41-55','56-70','70-85']
#XL=['4AM','8AM','12PM','4PM','8PM']
XL=['2AM','6AM','10AM','2PM','6PM','10PM']
XT=np.arange(2,26,4)
for ind,i in enumerate(Ages):
    if ind!=len(Ages)-1:
        NSample=WSum[ind]
        NSleepCounts=[x/NSample*100 for x in SleepCounts[ind,:]]
        ax=plt.subplot(2,3,ind+1)
        plt.subplots_adjust(wspace=0)
        plt.subplots_adjust(hspace=.4)
        plt.plot(times,NSleepCounts,'r')
        plt.plot(times,NSleepCounts0,'k--')#,alpha=.2)
        if ind==0:
            #plt.xlabel('Hour of the Day',fontsize=16)
            plt.ylabel('People Asleep (%)',fontsize=16)
            plt.legend(['This Group','Average'])
            plt.xticks(XT)
            ax.set_xticklabels(XL)
            plt.tick_params(axis='y', which='major', labelsize=16)
        else:
            if ind==3:
                plt.ylabel('People Asleep (%)',fontsize=16)
                
                plt.xticks(XT)
                ax.set_xticklabels(XL)
                plt.tick_params(axis='y', which='major', labelsize=16)
            else:
                plt.yticks([])
                plt.xticks(XT)
                ax.set_xticklabels(XL)
                plt.tick_params(axis='y', which='major', labelsize=16)
        plt.title('Ages: '+L[ind],fontsize=20)
        plt.ylim([0,100])
        plt.xlim([0,24])
        #plt.show()
    


#plt.savefig("SleepVsTime_Ages.png")


for a in Ages:
    L.append(str(a))
#plt.legend(L,title='Age Group')

plt.ylim([0,100])
plt.xlim([0,24])

import pandas as pd

SleepData1=pd.read_pickle('Data/SD1.pkl')
SleepData2=pd.read_pickle('Data/SD2.pkl')
#Pivot all data into bins by age

grouped1A = SleepData1.groupby('Age').sum()
grouped1A['wtdavg'] = grouped1A['WeightXSleep'] / grouped1A['Weight']
print(grouped1A.head())
grouped2A = SleepData2.groupby('Age').sum()
grouped2A['wtdavg'] = grouped2A['WeightXSleep'] / grouped2A['Weight']
print(grouped2A.head())

#Combine morning and night sleep
GroupedSplitA=[]
Remap=[2,3,4,5,6,7,1]
for i in grouped1A["wtdavg"].keys():
    GroupedSplitA.append((grouped1A["wtdavg"][i]+grouped2A["wtdavg"][i])/60)


Window=4
Edges=np.arange(np.ceil(65/Window))*Window+15
Sums=np.zeros((len(Edges)-1,1))
Counts=np.zeros((len(Edges)-1,1))
for ind,i in enumerate(Edges[0:len(Edges)-1]):
    for ind2,age in enumerate(grouped1A["wtdavg"].keys()):
        if (age>=i) & (age<i+Window):
            Sums[ind]+=GroupedSplitA[ind2]
            Counts[ind]+=1
Avgs=Sums/Counts   

ax=plt.subplot(2,3,6)
plt.bar(Edges[0:len(Edges)-1],Avgs[:,0],width=3)
plt.xlabel('Age',fontsize=16)
plt.ylabel('Avg. Sleep/Night (hrs)',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.xlim([12,78])
plt.ylim([8,10])
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")