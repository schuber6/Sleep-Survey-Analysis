# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 19:10:42 2018

@author: Scott
"""

import matplotlib.pyplot as plt
import numpy as np
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

plt.plot(Edges[0:len(Edges)-1],Avgs)
plt.xlabel('Age')
plt.ylabel('Average Sleep per Night (hrs)')
plt.show()

#plt.savefig('SleepVsAge_W4.png')