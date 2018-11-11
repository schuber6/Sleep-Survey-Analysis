# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:48:18 2018

@author: Scott
"""

#import packages and data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ATUS_Functions as AF
Codes=pd.read_csv("ATUS_Survey/codes.csv")
Activities=pd.read_csv("ATUS_Survey/atusact.csv")
Summary=pd.read_csv("ATUS_Survey/atussum.csv")
Respondent=pd.read_csv("ATUS_Survey/atusresp.csv")
#print(SU.head(10))
N_people=len(Summary["tucaseid"])  #Initialize all dataframes and store number of people as variable
Roster=pd.read_csv("ATUS_Survey/atusrost.csv")

#Split Times by morning sleep (from the previous night), and night sleep

SleepDict1={} 
SleepDict2={} 
for ind, row in Activities.iterrows():
    if (row["trcodep"]==10101) | (row["trcodep"]==10199):
        if (AF.Hour_Decimal(row["tustarttim"])>=4) & (AF.Hour_Decimal(row["tustarttim"])<=8):
            if row["tucaseid"] in SleepDict1.keys():
                SleepDict1[row["tucaseid"]]+=row["tuactdur24"]
            else:
                SleepDict1[row["tucaseid"]]=row["tuactdur24"]
        else:
            if row["tucaseid"] in SleepDict2.keys():
                SleepDict2[row["tucaseid"]]+=row["tuactdur24"]
            else:
                SleepDict2[row["tucaseid"]]=row["tuactdur24"]
                
AgeDict={}
for ind,row in Roster.iterrows():
    if (row["tulineno"]==1):
        AgeDict[row["tucaseid"]]=row["teage"]
        
#Combine day of week and stat weight from Respondent file with Sleep amount from above
#Use morning and night separated sleep

import math

cols=["DayOfWeek","Sleep","Weight","Age"]

SleepList1=[]
SleepList2=[]

for ind, row in Respondent.iterrows():
    if (row["tulineno"]==1 and math.isnan(row["tudiaryday"]) != True) and row["tucaseid"] in SleepDict1.keys():
        SleepList1.append([row["tudiaryday"],SleepDict1[row["tucaseid"]],row["tufnwgtp"],AgeDict[row["tucaseid"]]])
    if (row["tulineno"]==1 and math.isnan(row["tudiaryday"]) != True) and row["tucaseid"] in SleepDict2.keys():
        SleepList2.append([row["tudiaryday"],SleepDict2[row["tucaseid"]],row["tufnwgtp"],AgeDict[row["tucaseid"]]])
SleepData1=pd.DataFrame(SleepList1,columns=cols)
SleepData1["WeightXSleep"]=SleepData1["Weight"]*SleepData1["Sleep"]
print(SleepData1.head())
SleepData2=pd.DataFrame(SleepList2,columns=cols)
SleepData2["WeightXSleep"]=SleepData2["Weight"]*SleepData2["Sleep"]
print(SleepData2.head())

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


Window=2
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
#plt.savefig("SleepVsAge_W2.png")
