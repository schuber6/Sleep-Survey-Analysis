# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 19:12:59 2018

@author: Scott
"""


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
ax=plt.subplot(2,4,8)
plt.bar([1,2,3,4,5,6,7],GroupedSplit)
plt.xlabel("Night of Week")
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
plt.ylim([8.25,9.5])

plt.xticks(np.arange(7)+1,('Sun','Mon','Tues','Wed','Thurs','Fri','Sat'))
plt.ylabel("Average Sleep per Night (hrs)")
#plt.savefig("SleepVsDOW.png")